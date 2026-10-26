# Report

28 descriptors reviewed. Rubric v1.1.

fail: 10 · incomplete: 9 · pass: 9

Grades: A: 3 · B: 4 · C: 10 · D: 1 · F: 10

| Grade | Truth | Clarity | File | Worst finding |
|---|---|---|---|---|
| F | 0 | 64 | `registry/uniswap/calldata-UniswapV3Router02.json` | exactInput is payable but has no @.value field, so ETH sent with the swap is never shown. |
| F | 17 | 49 | `registry/1inch/calldata-AggregationRouterV3.json` | swap is payable and has no @.value field; the REQUIRES_EXTRA_ETH flag lets ETH above desc.amount leave unshown |
| F | 25 | 25 | `registry/safe/eip712-Safe-1.5.0.json` | SafeTx decodes nested data as a call to `to` and shows Value even when operation is Delegate Call. |
| F | 25 | 20 | `registry/safe/eip712-SafeL2-1.5.0.json` | SafeTx decodes the nested data as a call to `to` with `value`, also when the operation is a delegate call. |
| F | 41 | 22 | `registry/1inch/calldata-AggregationRouterV4.json` | swap is payable, but msg.value is never shown and a hidden flag lets it exceed the shown amount |
| F | 50 | 48 | `registry/ethena/calldata-ethena.json` | cooldownShares restarts the cooldown timer for all USDe the signer already has pending; nothing shown says so. |
| F | 62 | 35 | `registry/safe/calldata-SafeMigration-1.4.1.json` | migrateWithFallbackHandler also replaces the Safe's fallback handler, but shows the same "Migrate Safe" intent as migrateSingleton. |
| F | 62 | 38 | `registry/safe/calldata-SafeMigration-1.5.0.json` | migrateWithFallbackHandler replaces the Safe's fallback handler, but the screen never mentions it. |
| F | 75 | 56 | `registry/safe/calldata-Safe-1.5.0.json` | execTransaction is payable, but no field shows @.value, the native currency the signer sends. |
| F | 75 | 56 | `registry/safe/calldata-SafeL2-1.5.0.json` | execTransaction is payable, but no field shows the native value the signer sends. |
| D | 79 | 34 | `registry/midas/calldata-RedemptionVault.json` | redeemInstant does not say that part of the amount is a mToken fee sent to feeReceiver. |
| C | 80 | 23 | `registry/uniswap/eip712-UniswapX-DutchOrder.json` | Dutch order 'Spend max' shows inputStartAmount, but the input decays up to the hidden inputEndAmount. |
| C | 90 | 48 | `registry/paraswap/calldata-AugustusSwapper-v5.json` | simpleBuy hides data.partner and data.feePercent, which set the fee taken in the trade. |
| B | 90 | 69 | `registry/safe/calldata-SafeProxyFactory-1.5.0.json` | createProxyWithNonce: nested setup screen shows the setup data but not the delegatecall target `to`. |
| C | 90 | 30 | `registry/uniswap/eip712-UniswapX-ExclusiveDutchOrder.json` | 'Spend max' shows inputStartAmount, but input can rise to the hidden inputEndAmount. |
| C | 90 | 47 | `registry/uniswap/eip712-UniswapX-LimitOrder.json` | LimitOrder test messages are signatures UniswapX would reject: their nonce, deadline and spender differ from the order. |
| C | 90 | 30 | `registry/uniswap/eip712-uniswap-V2DutchOrder.json` | V2DutchOrder 'Spend max' shows baseInputStartAmount, but the input can rise to baseInputEndAmount |
| A | 100 | 98 | `registry/bedrock/calldata-uniBTC.json` |  |
| A | 100 | 92 | `registry/consensus-specs/calldata-DepositContract.json` |  |
| A | 100 | 91 | `registry/kiln/calldata-kiln-batch-exit.json` |  |
| C | 100 | 84 | `registry/layerswap/calldata-LayerswapDepository.json` | depositERC20 says "Swap token" but the call only sends tokens to a solver; nothing returns. |
| C | 100 | 42 | `registry/midas/calldata-MinterVault.json` | depositInstant shows 'Minimum to Receive' as a bare number and never names the mToken received |
| C | 100 | 48 | `registry/safe/calldata-SafeToL2Setup-1.5.0.json` | setupToL2 labels the new Safe implementation (singleton) as 'Module', which names the wrong role. |
| C | 100 | 59 | `registry/safe/eip712-Safe-Multisig.json` | DeleteRequest says "Reject transaction" but only deletes the proposal from the off-chain queue. |
| B | 100 | 74 | `registry/symbiotic/calldata-VaultV1-wstETH.json` | redeem: the share amount is shown as a raw 18-decimal integer and is hard to read |
| B | 100 | 76 | `registry/threshold/calldata-TBTCVault.json` |  |
| B | 100 | 88 | `registry/uniswap/calldata-UniswapV2Router02.json` |  |
| C | 100 | 47 | `registry/uniswap/eip712-uniswap-permit2.json` | PermitSingle shows the spender as a raw hex address, not as a named contract. |

Model cost (list price, from the CLI): $13.18.
