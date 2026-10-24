// The review key: P-256, made in and never leaving this Mac's Secure Enclave. The file it writes is the key
// wrapped by the Enclave: useless on any other machine, and every signature asks for Touch ID (or the password).
//
//   clear-review-signer create <file> [--no-touch]   new key (--no-touch: no Touch ID, for tests only); prints the public key
//   clear-review-signer pub <file>                   the public key: 04 || x || y, hex
//   clear-review-signer sign <file> <hex message>    ECDSA P-256 over SHA-256(message): r || s, hex
import CryptoKit
import Foundation
import LocalAuthentication

func die(_ s: String) -> Never { FileHandle.standardError.write((s + "\n").data(using: .utf8)!); exit(1) }
func hex(_ d: Data) -> String { d.map { String(format: "%02x", $0) }.joined() }
func unhex(_ s: String) -> Data {
    var d = Data(), i = s.startIndex
    while i < s.endIndex { let j = s.index(i, offsetBy: 2); guard let b = UInt8(s[i..<j], radix: 16) else { die("bad hex") }; d.append(b); i = j }
    return d
}

let a = CommandLine.arguments
guard a.count >= 3, SecureEnclave.isAvailable else { die("usage: clear-review-signer create|pub|sign <file> ... (needs a Secure Enclave)") }
let file = URL(fileURLWithPath: a[2])
do {
    switch a[1] {
    case "create":
        if FileManager.default.fileExists(atPath: file.path) { die("\(file.path) exists: not overwriting a key") }
        var flags: SecAccessControlCreateFlags = [.privateKeyUsage]
        if !a.contains("--no-touch") { flags.insert(.userPresence) }
        guard let ac = SecAccessControlCreateWithFlags(nil, kSecAttrAccessibleWhenUnlockedThisDeviceOnly, flags, nil) else { die("access control") }
        let k = try SecureEnclave.P256.Signing.PrivateKey(accessControl: ac)
        try k.dataRepresentation.write(to: file, options: .withoutOverwriting)
        print(hex(k.publicKey.x963Representation))
    case "pub":
        print(hex(try SecureEnclave.P256.Signing.PrivateKey(dataRepresentation: Data(contentsOf: file)).publicKey.x963Representation))
    case "sign":
        guard a.count == 4 else { die("usage: clear-review-signer sign <file> <hex message>") }
        let ctx = LAContext()
        ctx.localizedReason = "sign a clear-review round"
        let k = try SecureEnclave.P256.Signing.PrivateKey(dataRepresentation: Data(contentsOf: file), authenticationContext: ctx)
        print(hex(try k.signature(for: unhex(a[3])).rawRepresentation))
    default:
        die("unknown command \(a[1])")
    }
} catch { die("\(error)") }
