## Extra checks (second-opinion review)

These come from what descriptor generators (portdeveloper/clear-signing-helper, austintgriffith/clear-signing-skill) enforce. Report them with the checks above, same format and severity scale.

- A payable function must show the native value `@.value`. A payable format that hides it, or has no field for it, lets the signer send ETH without seeing it: `hidden-values`, critical when the code forwards or keeps that value.
- A recipient, spender, amount or limit (minimum out, maximum in, deadline) must never be hidden. Hiding one is `hidden-values`.
- A `tokenAmount` whose token is fixed (`token` or a constant) must be the token the code actually moves, with the right decimals. A wrong token or wrong decimals misstates the amount: critical.
- A deployment added to an existing descriptor must run the same code as the other deployments of that descriptor. A fork or a different protocol's contract added to someone else's file is `binding-context`.
- Nested calldata (`execute(bytes)`, `multicall(bytes[])`) that the descriptor shows as a plain intent with the payload hidden lets any action pass under a harmless screen: `hidden-values`, critical unless the function can only call this contract with a fixed effect.
