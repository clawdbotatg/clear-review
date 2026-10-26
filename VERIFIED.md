# Verified criticals

A second agent tried to refute every critical of every failed descriptor.
confirmed: 293 · refuted: 85 · unsure: 16


## `registry/1inch/calldata-AggregationRouterV3.json`

- **swap**: swap is payable and has no @.value field; the REQUIRES_EXTRA_ETH flag lets ETH above desc.amount leave unshown  
  When the _REQUIRES_EXTRA_ETH flag is set, swap() requires msg.value to be strictly greater than desc.amount (or greater than 0 for a token source), then forwards all of msg.value to the executor. The swap format has no @.value field and hides desc.flags with visible: never, so the extra ETH that leaves the wallet is never shown. Only desc.amount appears, as 'Amount to Send'.

## `registry/1inch/calldata-AggregationRouterV4-eth.json`

- **swap**: swap hides msg.value; with the extra-ETH flag the signer sends more ETH than the amount shown.  
  When the extra-ETH flag is set, msg.value can be any amount above desc.amount, or any non-zero amount for an ERC-20 source, and all of it goes to the executor. No field shows msg.value and the flag is hidden, so ETH leaves the wallet in an amount the screen never shows.
- **swap**: swap shows 'Minimum to Receive', but with the partial-fill flag the signer can receive less.  
  With the partial-fill flag, the code only checks a proportional rate, so the receiver can get less than the 'Minimum to Receive' value shown. The flag is hidden. The unspent source tokens come back to the signer, but the screen shows the minimum as a fixed amount, and partial fills can happen without the signer knowing.
- **uniswapV3SwapToWithPermit**: uniswapV3SwapToWithPermit names the sent token from srcToken, but the pool decides which token leaves.  
  The code uses srcToken only for the permit and never checks it against the pool. The token taken from the signer is token0 or token1 of pools[0], so the screen can name an asset that is not the one taken.

## `registry/1inch/calldata-AggregationRouterV4.json`

- **swap**: swap is payable, but msg.value is never shown and a hidden flag lets it exceed the shown amount  
  When the hidden flag bit 1 is set, the code requires msg.value to be more than desc.amount, or more than 0 for a token source. It then forwards all of msg.value to the executor, so native currency beyond the shown 'Amount to Send' leaves the wallet. The test transaction sent value 0, but this holds for any valid input with the flag, and nothing on screen shows msg.value or the flag.

## `registry/1inch/calldata-AggregationRouterV5.json`

- **swap**: swap is payable and the extra-ETH flag lets msg.value exceed the shown amount; no value field exists  
  With _REQUIRES_EXTRA_ETH set, msg.value only has to exceed desc.amount (or 0 for a token source), so the signer can send more ETH than shown. _execute forwards all of callvalue() to the executor. desc.flags is visible: never and there is no @.value field, so the extra ETH is not on screen.

## `registry/1inch/calldata-AggregationRouterV6.json`

- **permitAndCall**: permitAndCall is payable and the inner delegatecall spends msg.value, but no field shows the native value.  
  permitAndCall is payable and delegatecalls to itself, so msg.value stays live for the inner call (for example ethUnoswap, or swap with ETH). The outer screen has no @.value field. The calldata field has no amountPath, so the nested screen cannot resolve @.value either.
- **swap**: swap is payable, and with the extra-ETH flag the native value is more than the amount shown; no field shows it.  
  With the _REQUIRES_EXTRA_ETH flag, msg.value must be more than desc.amount (or more than 0 for a token source), and _execute forwards all of callvalue() to the executor. The screen shows only desc.amount; desc.flags is visible never and there is no @.value field.
- **fillContractOrder**: fillContractOrder shows `amount` as takerAsset to sell, but with the maker-amount flag it is makerAsset to receive.  
  With bit 255 of takerTraits set, amount is the makerAsset amount the signer receives, and the signer pays a computed takingAmount. The screen shows amount as 'Amount to sell' in order.takerAsset. The enum has no key for 128 or higher, so the mode is never stated.
- **fillContractOrderArgs**: fillContractOrderArgs hides the target from `args` that receives the signer's purchased makerAsset.  
  When the _ARGS_HAS_TARGET bit is set, the first 20 bytes of args become the target, and _fill sends the makerAsset (or the unwrapped ETH) to that target. args is visible never, and the enum has no key with bit 8, so the recipient is never shown.
- **fillContractOrderArgs**: fillContractOrderArgs shows `amount` in takerAsset even when the maker-amount flag makes it makerAsset.  
  This is the same isMakingAmount branch as finding 3. The amount is a makerAsset amount, but the screen shows it as 'Amount to sell' in takerAsset.
- **fillContractOrderArgs**: fillContractOrderArgs hides the threshold, the only limit on dynamic extension pricing.  
  With an extension from args, an amount getter chosen by the maker prices the fill. The hidden threshold is then the only limit on what the signer pays (maker-amount mode) or the minimum the signer receives. The screen shows only takerTraits.[:1], so the threshold is never shown.
- **fillOrder**: fillOrder is payable and spends ETH in place of WETH, but no field shows the native value.  
  fillOrder is payable. When takerAsset is WETH and msg.value > 0, the router keeps takingAmount of ETH, wraps it or forwards it to the maker, and refunds the rest. The screen shows a WETH amount and has no @.value field, so native ETH leaves the wallet unshown.
- **fillOrder**: fillOrder shows `amount` as takerAsset to sell, but with the maker-amount flag it is makerAsset to receive.  
  With bit 255 set, amount is the makerAsset amount the signer receives, not the takerAsset amount they sell. The descriptor labels it 'Amount to sell' with tokenPath order.takerAsset, and the enum has keys only 0, 16, 32, 64, 80 and 96.
- **fillOrderArgs**: fillOrderArgs hides the target from `args` that receives the signer's purchased makerAsset.  
  This is the same _parseArgs target path as finding 5, and fillOrderArgs sends the makerAsset to that target. args is visible never and no enum key covers bit 8.
- **fillOrderArgs**: fillOrderArgs is payable and spends ETH in place of WETH, but no field shows the native value.  
  fillOrderArgs is payable and goes through the same _fill msg.value branch as fillOrder. ETH replaces WETH as payment and is kept or forwarded, and no @.value field exists.
- **fillOrderArgs**: fillOrderArgs shows `amount` in takerAsset even when the maker-amount flag makes it makerAsset.  
  This is the same maker-amount mislabel as finding 9, here for fillOrderArgs: the amount is shown in takerAsset as 'Amount to sell' when it is a makerAsset amount.
- **fillOrderArgs**: fillOrderArgs hides the threshold, the only limit on dynamic extension pricing.  
  With an args extension, a getter chosen by the maker sets the price, and the hidden threshold is the only limit on the signer's payment or minimum received. Only the top byte of takerTraits is shown.

## `registry/HyperDiscipline/eip712-CommitIntent.json`

- **CommitIntent**: CommitIntent: 'Stake amount' shows the gross deposit, but the platform fee is cut before the stake is locked.  
  The code keeps the fee for the treasury and locks only totalDeposit minus the fee as the stake. That net stake is what Returned and emergency withdraw pay back, but the screen shows the gross 10 USDC as 'Stake amount' and never mentions a fee. This is the guide's amount rule: a fee rate from storage cuts the amount shown, so it is critical and not the not-critical item 3 (storage values). Also, in case 0 the fine is 10 USDC, which is more than the net stake, so that signed intent would revert with InvalidFine.

## `registry/aave/calldata-lpv2.json`

- **swapBorrowRateMode**: swapBorrowRateMode intent says 'Swap to variable', but rateMode 2 moves debt to stable on Polygon/Avalanche.  
  On Polygon and Avalanche, rateMode 2 passes validation and turns the signer's variable debt into stable-rate debt, while the title says "Swap to variable". Only mainnet forces the stable-to-variable direction. The action shown is the opposite of the one executed, so this is critical; it does depend on reserve flags in storage (not frozen, stable rate enabled) that the code itself does not rule out.

## `registry/ekubo/calldata-MEVCaptureRouter.json`

- **swap**: swap (isToken1, threshold) is payable, but the screen never shows the ETH sent (@.value).  
  No path checks msg.value. For a native token0 swap the router forwards ETH to CORE, and any extra or unrelated ETH stays in the router, where anyone can take it through refundNativeToken. No field shows the ETH sent.
- **swap**: swap (isToken1, recipient) is payable, but the screen never shows the ETH sent.  
  This is the same single-swap path as finding 0. The ETH sent is forwarded to CORE or kept in the router. It is never shown, and nothing forces it to zero.
- **swap**: swap (packed params) is payable, but the screen never shows the ETH sent.  
  It calls the public payable swap, which has no msg.value check. Native ETH is forwarded to CORE through `_swap(value, ...)`, and any excess stays in the router. The value is not shown.
- **swap**: swap (packed params, recipient) is payable, but the screen never shows the ETH sent.  
  No check forces msg.value to zero. The ETH is spent on native swaps or kept in the router. No field shows @.value.
- **swap**: swap (route node) is payable, but the screen never shows the ETH sent.  
  It sends the call to the same single-swap lock with no msg.value check. The ETH sent is forwarded to CORE or kept in the router, and it is not shown.
- **swapAllowPartialFill**: swapAllowPartialFill (isToken1) is payable, but the screen never shows the ETH sent.  
  No msg.value check exists. ETH is forwarded for native token0 swaps, and any remaining ETH stays in the router. No @.value field exists.
- **swapAllowPartialFill**: swapAllowPartialFill (isToken1, recipient) is payable, but the screen never shows the ETH sent.  
  This is the same path as finding 5. The ETH sent is spent or kept by the router, and it is never shown.
- **swapAllowPartialFill**: swapAllowPartialFill (packed) is payable, but the screen never shows the ETH sent.  
  No msg.value check exists. ETH is forwarded on native swaps or kept in the router. The format has no @.value field.
- **swapAllowPartialFill**: swapAllowPartialFill (packed, recipient) is payable, but the screen never shows the ETH sent.  
  Nothing forces msg.value to zero. The ETH is spent or kept in the router, and no field shows it.
- **swapAllowPartialFill**: swapAllowPartialFill (route node) is payable, but the screen never shows the ETH sent.  
  It sends the call to the payable swapAllowPartialFill with no value check. The ETH sent is forwarded or kept, and it is not shown.
- **multicall**: multicall is payable and is the usual way to pay ETH, but the ETH sent is never shown.  
  The ETH sent goes into the router, and inner native swaps spend it. The 'Action' calldata fields do not show a value, and the descriptor has no @.value.
- **multihopSwap**: multihopSwap is payable and spends router ETH for native input, but the ETH sent is never shown.  
  For a native input the router pays the accountant from the ETH sent. Any excess stays in the router. Neither amount is shown, because the format has no @.value field.
- **multiMultihopSwap**: multiMultihopSwap is payable and spends router ETH for native input, but the ETH sent is never shown.  
  This is the same code path as finding 11. The ETH sent is spent or kept, and nothing on screen shows it.
- **swap**: swap is payable, and no field shows the ETH sent (@.value)  
  This duplicates finding 1. There is no msg.value check, and the ETH is forwarded to CORE or kept in the router without being shown.
- **swap**: swap is payable, and no field shows the ETH sent (@.value)  
  This duplicates finding 2. The ETH sent is not shown and is not forced to zero.
- **swap**: swap is payable, and no field shows the ETH sent (@.value)  
  This duplicates finding 3. The ETH sent is not shown and is not forced to zero.
- **swap**: swap is payable, and no field shows the ETH sent (@.value)  
  This duplicates finding 4. The ETH sent is not shown and is not forced to zero.
- **swapAllowPartialFill**: swapAllowPartialFill is payable, and no field shows the ETH sent (@.value)  
  This duplicates finding 5. The ETH sent is not shown and is not forced to zero.
- **swapAllowPartialFill**: swapAllowPartialFill is payable, and no field shows the ETH sent (@.value)  
  This duplicates finding 6. The ETH sent is not shown and is not forced to zero.
- **swapAllowPartialFill**: swapAllowPartialFill is payable, and no field shows the ETH sent (@.value)  
  This duplicates finding 7. The ETH sent is not shown and is not forced to zero.
- **swapAllowPartialFill**: swapAllowPartialFill is payable, and no field shows the ETH sent (@.value)  
  This duplicates finding 8. The ETH sent is not shown and is not forced to zero.
- **swapAllowPartialFill**: swapAllowPartialFill is payable, and no field shows the ETH sent (@.value)  
  This duplicates finding 9. The ETH sent is not shown and is not forced to zero.
- **multicall**: multicall is payable, and no field shows the ETH sent (@.value)  
  This duplicates finding 10. The ETH sent goes to the router and is spent by inner swaps, and it is never shown.
- **multihopSwap**: multihopSwap is payable, and no field shows the ETH sent (@.value)  
  This duplicates finding 11. The ETH sent is spent or kept in the router, and it is not shown.
- **multiMultihopSwap**: multiMultihopSwap is payable, and no field shows the ETH sent (@.value)  
  This duplicates finding 12. The ETH sent is spent or kept in the router, and it is not shown.

## `registry/ekubo/calldata-Orders.json`

- **mintAndIncreaseSellAmount**: mintAndIncreaseSellAmount is payable and the descriptor has no @.value field, so the ETH sent is hidden.  
  For a native-token order, the ETH the signer sends pays the sell amount to the accountant. Any extra ETH stays in the contract, where anyone can take it through refundNativeToken. No field shows the native value.
- **increaseSellAmount**: increaseSellAmount is payable and the descriptor has no @.value field, so the ETH sent is hidden.  
  The function spends the msg.value on native orders and keeps any extra in the contract. Nothing forces the value to zero, and the screen never shows the ETH sent.
- **decreaseSaleRate**: decreaseSaleRate is payable and the descriptor has no @.value field; ETH sent stays in the contract.  
  ETH sent with this call stays in the Orders contract, and any caller can then take it through refundNativeToken. No field shows @.value, and nothing forces the value to zero.
- **decreaseSaleRate**: decreaseSaleRate with recipient is payable and the descriptor has no @.value field.  
  Any ETH sent stays in the contract balance, where any caller can take it through refundNativeToken. The screen does not show the native value.
- **collectProceeds**: collectProceeds is payable and the descriptor has no @.value field; ETH sent stays in the contract.  
  ETH sent stays in the contract, and any caller can take it through refundNativeToken. The screen never shows @.value.
- **collectProceeds**: collectProceeds with recipient is payable and the descriptor has no @.value field.  
  Same as finding 4: the contract keeps the ETH sent, nothing on screen shows it, and nothing forces it to zero.
- **burn**: burn is payable and the descriptor has no @.value field; ETH sent stays in the contract.  
  "Ignored" here means the contract keeps the ETH sent, and refundNativeToken lets any caller take it. No @.value field shows it.
- **multicall**: multicall is payable and the descriptor has no @.value field, so the ETH funding inner orders is hidden.  
  The override removes the zero-value guard. Inner native orders spend msg.value through the delegatecalls, and leftover ETH stays in the contract. No field shows the ETH sent.
- **approve**: approve is payable and the descriptor has no @.value field; ETH sent stays in the contract.  
  approve does not check msg.value, so the contract keeps any ETH sent, and refundNativeToken lets anyone take it. No @.value field shows it.
- **transferFrom**: transferFrom is payable and the descriptor has no @.value field; ETH sent stays in the contract.  
  The contract keeps any ETH sent, and nothing on screen shows it or forces it to zero.
- **safeTransferFrom**: safeTransferFrom is payable and the descriptor has no @.value field; ETH sent stays in the contract.  
  There is no value check, so the contract keeps any ETH sent and no field shows it.
- **safeTransferFrom**: safeTransferFrom with data is payable and the descriptor has no @.value field.  
  There is no value check, so the contract keeps any ETH sent and no field shows it.
- **mint**: mint() is payable and ignores msg.value, and the descriptor has no @.value field.  
  The contract keeps the ETH and any caller can take it through refundNativeToken. The screen shows no native value.
- **mint**: mint(bytes32) is payable and ignores msg.value, and the descriptor has no @.value field.  
  The contract keeps the ETH and any caller can take it through refundNativeToken. No @.value field shows it.
- **transferOwnership**: transferOwnership is payable and the descriptor has no @.value field.  
  ETH sent by the owner stays in the contract, and any caller can take it through refundNativeToken. No field shows it.
- **renounceOwnership**: renounceOwnership is payable and the descriptor has no @.value field.  
  There is no value check, so the contract keeps any ETH sent and the screen shows none.
- **requestOwnershipHandover**: requestOwnershipHandover is payable and the descriptor has no @.value field.  
  The contract keeps any ETH sent, where any caller can take it through refundNativeToken. The screen does not show it.
- **cancelOwnershipHandover**: cancelOwnershipHandover is payable and the descriptor has no @.value field.  
  There is no value check, so the contract keeps any ETH sent and nothing on screen shows it.
- **completeOwnershipHandover**: completeOwnershipHandover is payable and the descriptor has no @.value field.  
  There is no value check, so the contract keeps any ETH sent and nothing on screen shows it.

## `registry/ekubo/calldata-Positions.json`

- **deposit**: deposit is payable and spends msg.value in native pools, but no @.value field is shown.  
  Nothing checks msg.value. In a native pool the ETH goes to the accountant, and any extra stays in the contract, where anyone can take it with refundNativeToken. The screen shows maxAmount0 but not the ETH actually attached.
- **mintAndDeposit**: mintAndDeposit is payable and spends msg.value in native pools, but no @.value field is shown.  
  This goes through the same deposit path: ETH is forwarded to the accountant or left in the contract, with no zero check. The value attached is never shown.
- **mintAndDepositWithSalt**: mintAndDepositWithSalt is payable and spends msg.value in native pools, but no @.value is shown.  
  Same as finding 1. It is payable, nothing forces the value to zero, and the ETH is spent or kept without being shown.
- **collectFees**: collectFees is payable, ignores msg.value, and no @.value field shows ETH sent.  
  Nothing forces the value to zero. ETH sent stays in the contract balance, and any caller can then take it with refundNativeToken. The screen never shows it.
- **collectFees**: collectFees with recipient is payable, but no @.value field shows ETH sent.  
  It is payable with no msg.value check, so the ETH is kept by the contract and anyone can sweep it. It is not shown.
- **withdraw**: withdraw is payable, but no @.value field shows ETH sent with it.  
  It is payable with no zero-value check. The ETH stays in the contract, where refundNativeToken lets anyone take it, and it is not on screen.
- **withdraw**: withdraw with recipient is payable, but no @.value field shows ETH sent.  
  It is payable with no check on msg.value. The ETH is kept in the contract balance and not shown.
- **maybeInitializePool**: maybeInitializePool is payable, ignores msg.value, and no @.value field is shown.  
  It is payable and ignores msg.value without reverting, so the ETH stays in the contract, open to anyone. It is not shown.
- **burn**: burn is payable, ignores msg.value, and no @.value field is shown.  
  'Ignored' means it is kept, not refused: nothing reverts, and the ETH stays in the contract where anyone can sweep it. It is not on screen.
- **multicall**: multicall is payable and funds native deposits, but no @.value field is shown.  
  The inner delegatecalls run with the outer msg.value, and native deposits pay ETH from it to the accountant. The total ETH attached is never shown.
- **approve**: approve is payable, but no @.value field shows ETH sent.  
  It is payable with no msg.value check anywhere in the inheritance, so the ETH stays in the Positions contract, where anyone can take it with refundNativeToken. It is not shown.
- **transferFrom**: transferFrom is payable, but no @.value field shows ETH sent.  
  It is payable with no zero check. The ETH is kept by the contract, can be swept by anyone, and is not shown.
- **safeTransferFrom**: safeTransferFrom is payable, but no @.value field shows ETH sent.  
  It is payable with no check, so the ETH is kept and not shown.
- **safeTransferFrom**: safeTransferFrom with data is payable, but no @.value field shows ETH sent.  
  It is payable with no check, so the ETH is kept and not shown.
- **mint**: mint() is payable, ignores msg.value, and no @.value field is shown.  
  It does not revert on value, so the ETH stays in the contract, where anyone can take it. The screen has no fields at all.
- **mint**: mint(salt) is payable, ignores msg.value, and no @.value field is shown.  
  It is payable and ignores msg.value without reverting, so the ETH is kept and not shown.
- **transferOwnership**: transferOwnership is payable, but no @.value field shows ETH sent.  
  Nothing forces the value to zero. ETH sent by the owner stays in the contract, where anyone can sweep it, and it is not shown.
- **renounceOwnership**: renounceOwnership is payable, but no @.value field shows ETH sent.  
  It is payable with no zero check, so the ETH is kept and nothing is shown.
- **requestOwnershipHandover**: requestOwnershipHandover is payable, but no @.value field shows ETH sent.  
  It is payable with no zero check, so the ETH is kept and nothing is shown.
- **cancelOwnershipHandover**: cancelOwnershipHandover is payable, but no @.value field shows ETH sent.  
  It is payable with no zero check, so the ETH is kept and nothing is shown.
- **completeOwnershipHandover**: completeOwnershipHandover is payable, but no @.value field shows ETH sent.  
  It is payable with no zero check, so the ETH is kept and not shown.
- **withdrawProtocolFees**: withdrawProtocolFees is payable, but no @.value field shows ETH sent.  
  It is payable with no msg.value check, so the ETH stays in the contract and is not shown.

## `registry/ekubo/calldata-Ve33Periphery.json`

- **scheduleEmissions**: scheduleEmissions: the STONX transfer out of the signer's wallet and its amount are not shown  
  The signer's STONX (stakeToken 0x570c…, an ERC-20) leaves the wallet by transferFrom, in an amount the contract works out from the rate and the duration. No field shows the amount or says the signer pays, so this effect on the signer's assets is not shown. Only the raw Q32 rate is shown, and that is not the amount transferred.
- **scheduleEmissions**: scheduleEmissions is payable but @.value is not shown, and ETH sent is left in the periphery  
  No path uses or rejects msg.value: lock forwards 0 and the ERC-20 branch is the only one used. The ETH stays in the periphery and any caller can take it with refundNativeToken, and the screen never shows the value.
- **multicall**: multicall is payable but @.value is not shown  
  multicall accepts ETH and only passes the inner calls through. scheduleEmissions does not use ETH because the stake token is an ERC-20, so the ETH stays in the contract unless a refund is batched. The descriptor shows no @.value.

## `registry/ekubo/calldata-Ve33Positions.json`

- **deposit**: deposit is payable and spends msg.value for a native token0, but no @.value field exists  
  Nothing in the code checks msg.value. When token0 is native, the ETH the signer sends is forwarded to the accountant, and any unused rest stays in the contract where any caller can take it with refundNativeToken. The descriptor has no `@.value` field anywhere.
- **withdraw**: withdraw is payable but has no @.value field; sent ETH stays claimable by anyone  
  Nothing rejects a non-zero msg.value. The ETH stays in the contract and any caller can take it with refundNativeToken. No field shows `@.value`.
- **withdraw**: withdraw with recipient is payable but has no @.value field  
  There is no msg.value check, so the ETH stays in the contract where anyone can sweep it. The format has no `@.value` field.
- **withdrawAndClaimRewards**: withdrawAndClaimRewards is payable but has no @.value field  
  There is no msg.value check, so the ETH the signer sends stays in the contract where anyone can sweep it. The format has no `@.value` field.
- **withdrawAndClaimRewards**: withdrawAndClaimRewards with recipient is payable but has no @.value field  
  There is no msg.value check, so the ETH stays in the contract where anyone can sweep it. The format has no `@.value` field.
- **claimRewards**: claimRewards is payable but has no @.value field  
  There is no msg.value check, so the ETH stays in the contract where anyone can sweep it. The format has no `@.value` field.
- **claimRewards**: claimRewards with recipient is payable but has no @.value field  
  There is no msg.value check, so the ETH stays in the contract where anyone can sweep it. The format has no `@.value` field.
- **maybeInitializePool**: maybeInitializePool is payable but has no @.value field  
  The function never uses or rejects msg.value. The ETH stays in the contract where anyone can sweep it, and the format has no `@.value` field.
- **mintAndDeposit**: mintAndDeposit is payable and spends msg.value for native token0, but no @.value field exists  
  When token0 is native, the signer's ETH pays for the deposit, and any rest stays in the contract where anyone can sweep it. Nothing on screen shows the ETH sent.
- **mintAndDepositWithSalt**: mintAndDepositWithSalt is payable and spends msg.value, but no @.value field exists  
  This is the same path as mintAndDeposit: the ETH funds a native token0 or stays in the contract where anyone can sweep it. The format has no `@.value` field.
- **mint**: mint() is payable and ignores msg.value, but no @.value field exists  
  Nothing rejects the ETH, so it stays in the contract and any caller can take it with refundNativeToken. Nothing on screen shows it.
- **mint**: mint(bytes32) is payable and ignores msg.value, but no @.value field exists  
  There is no msg.value check, so the ETH stays in the contract where anyone can sweep it. The format has no `@.value` field.
- **burn**: burn is payable and ignores msg.value, but no @.value field exists  
  There is no msg.value check, so the ETH stays in the contract where anyone can sweep it. The format has no `@.value` field.
- **multicall**: multicall is payable and funds native deposits with msg.value, but no @.value field exists  
  The override removes Solady's revert on non-zero value. The ETH funds native deposits in the inner calls or stays in the contract. Only `data.[]` is shown, never `@.value`.
- **approve**: approve is payable but has no @.value field  
  There is no msg.value check, so the ETH stays in the Ve33Positions balance where any caller can sweep it with refundNativeToken. The format has no `@.value` field.
- **transferFrom**: transferFrom is payable but has no @.value field  
  There is no msg.value check, so the ETH stays in the contract where anyone can sweep it. The format has no `@.value` field.
- **safeTransferFrom**: safeTransferFrom is payable but has no @.value field  
  There is no msg.value check, so the ETH stays in the contract where anyone can sweep it. The format has no `@.value` field.
- **safeTransferFrom**: safeTransferFrom with data is payable but has no @.value field  
  There is no msg.value check, so the ETH stays in the contract where anyone can sweep it. The format has no `@.value` field.
- **transferOwnership**: transferOwnership is payable but has no @.value field  
  Only the owner can call it, but nothing rejects the ETH. The ETH stays in the contract where anyone can sweep it, and no `@.value` field shows it.
- **renounceOwnership**: renounceOwnership is payable but has no @.value field  
  There is no msg.value check, so the ETH stays in the contract where anyone can sweep it. The format shows no fields.
- **requestOwnershipHandover**: requestOwnershipHandover is payable but has no @.value field  
  There is no msg.value check, so the ETH stays in the contract where anyone can sweep it. The format shows no fields.
- **cancelOwnershipHandover**: cancelOwnershipHandover is payable but has no @.value field  
  There is no msg.value check, so the ETH stays in the contract where anyone can sweep it. The format shows no fields.
- **completeOwnershipHandover**: completeOwnershipHandover is payable but has no @.value field  
  There is no msg.value check, so the ETH stays in the contract where anyone can sweep it. The format has no `@.value` field.

## `registry/ekubo/calldata-VeToken.json`

- **stake**: stake is payable but no @.value field is shown, and native value sent is left in the contract.  
  stake is payable and never uses msg.value: the stake token immutable is the ERC20 0x570c…70c5, so the ACCOUNTANT.payFrom path runs. lock() calls with value 0, so the ETH stays in VeToken, and refundNativeToken sends the whole balance to any caller. No @.value field is on screen.
- **stake**: stake with salt is payable but no @.value field is shown.  
  Same as finding 0. Nothing checks msg.value, and the ERC20 stake path does not use it. The ETH stays in the contract, where anyone can take it, and no @.value is shown.
- **stakeForDuration**: stakeForDuration is payable but no @.value field is shown.  
  This function is payable and calls stake with no check on msg.value. The ETH sent stays in VeToken, where anyone can take it with refundNativeToken, and no @.value is shown.
- **stakeForDuration**: stakeForDuration with salt is payable but no @.value field is shown.  
  This function is payable, has no check on msg.value, and does not use msg.value. The ETH stays in the contract and no @.value is shown.
- **stakeMaxDuration**: stakeMaxDuration is payable but no @.value field is shown.  
  This function is payable, has no check on msg.value, and does not use msg.value. The ETH stays in the contract and no @.value is shown.
- **stakeMaxDuration**: stakeMaxDuration with salt is payable but no @.value field is shown.  
  This function is payable, has no check on msg.value, and does not use msg.value. The ETH stays in the contract and no @.value is shown.
- **stakeAndVote**: stakeAndVote is payable but no @.value field is shown.  
  This function is payable. It calls stake and vote, and neither uses msg.value. The ETH stays in the contract and no @.value is shown.
- **increaseStakeAmount**: increaseStakeAmount is payable but no @.value field is shown.  
  This function is payable and its lock settles the ERC20 by payFrom, so msg.value is unused. The ETH stays in the contract and no @.value is shown.
- **extendStake**: extendStake is payable but no @.value field is shown.  
  extendStake is payable and only calls ve33.moveStake and _setExtraData, so msg.value is unused and the ETH stays in VeToken. No @.value is shown.
- **extendStakeForDuration**: extendStakeForDuration is payable but no @.value field is shown.  
  This function is payable and does not use msg.value. The ETH stays in the contract, where anyone can take it, and no @.value is shown.
- **extendStakeMaxDuration**: extendStakeMaxDuration is payable but no @.value field is shown.  
  This function is payable and does not use msg.value. The ETH stays in the contract and no @.value is shown.
- **claimPoolFeesAndExtendStake**: claimPoolFeesAndExtendStake is payable but no @.value field is shown.  
  This function is payable. It calls claimPoolFees and extendStake, and neither uses msg.value. The ETH stays in the contract and no @.value is shown.
- **claimPoolFeesAndExtendStakeForDuration**: claimPoolFeesAndExtendStakeForDuration is payable but no @.value field is shown.  
  This function is payable and does not use msg.value. The ETH stays in the contract and no @.value is shown.
- **claimPoolFeesAndExtendStakeMaxDuration**: claimPoolFeesAndExtendStakeMaxDuration is payable but no @.value field is shown.  
  This function is payable and does not use msg.value. The ETH stays in the contract and no @.value is shown.
- **claimPoolFeesAndExtendStakeToSelf**: claimPoolFeesAndExtendStakeToSelf is payable but no @.value field is shown.  
  This function is payable and does not use msg.value. The ETH stays in the contract and no @.value is shown.
- **claimPoolFeesAndExtendStakeToSelfForDuration**: claimPoolFeesAndExtendStakeToSelfForDuration is payable but no @.value field is shown.  
  This function is payable and does not use msg.value. The ETH stays in the contract and no @.value is shown.
- **claimPoolFeesAndExtendStakeToSelfMaxDuration**: claimPoolFeesAndExtendStakeToSelfMaxDuration is payable but no @.value field is shown.  
  This function is payable and does not use msg.value. The ETH stays in the contract and no @.value is shown.
- **splitStake**: splitStake is payable but no @.value field is shown.  
  This function is payable and only mints and moves stake, so msg.value is unused. The ETH stays in the contract and no @.value is shown.
- **splitStake**: splitStake with salt is payable but no @.value field is shown.  
  This function is payable and does not use msg.value. The ETH stays in the contract and no @.value is shown.
- **mergeStakes**: mergeStakes is payable but no @.value field is shown.  
  This function is payable and does not use msg.value. The ETH stays in the contract and no @.value is shown.
- **claimPoolFeesAndMergeStakes**: claimPoolFeesAndMergeStakes is payable but no @.value field is shown.  
  This function is payable and does not use msg.value. The ETH stays in the contract and no @.value is shown.
- **claimPoolFeesAndMergeStakesToSelf**: claimPoolFeesAndMergeStakesToSelf is payable but no @.value field is shown.  
  This function is payable and does not use msg.value. The ETH stays in the contract and no @.value is shown.
- **withdrawStake**: withdrawStake is payable but no @.value field is shown.  
  This function is payable. The unstake lock only withdraws the ERC20 stake token, so msg.value stays in the contract. No @.value is shown.
- **withdrawStakeToSelf**: withdrawStakeToSelf is payable but no @.value field is shown.  
  This function is payable and does not use msg.value. The ETH stays in the contract and no @.value is shown.
- **burn**: burn says the NFT is 'empty', but the code burns any NFT and any remaining stake is lost for good.  
  burn has no check on ve33.stakeAmount, so it burns an NFT that still holds stake. After the burn, _stakeEndTime reverts with TokenDoesNotExist, so withdrawStake can no longer reach the stake. The intent tells the signer the NFT is empty.
- **burn**: burn is payable but no @.value field is shown.  
  burn is payable and does not use msg.value. The ETH stays in the contract and no @.value is shown.
- **vote**: vote is payable but no @.value field is shown.  
  vote is payable and only calls ve33.vote with no value. The ETH stays in the contract and no @.value is shown.
- **clearVote**: clearVote is payable but no @.value field is shown.  
  clearVote is payable and does not use msg.value. The ETH stays in the contract and no @.value is shown.
- **claimPoolFees**: claimPoolFees is payable but no @.value field is shown.  
  claimPoolFees is payable. The lock withdraws pool fees and does not forward msg.value, so the ETH stays in the contract. No @.value is shown.
- **claimPoolFeesToSelf**: claimPoolFeesToSelf is payable but no @.value field is shown.  
  This function is payable and does not use msg.value. The ETH stays in the contract and no @.value is shown.
- **maybeInitializePool**: maybeInitializePool is payable but no @.value field is shown.  
  maybeInitializePool is payable and calls CORE.initializePool with no value. The ETH stays in VeToken, where anyone can take it, and no @.value is shown.
- **multicall**: multicall is payable but no @.value field is shown.  
  The override removes Solady's `if (msg.value != 0) revert();`, so ETH can be sent with a batch. No inner action uses it for the ERC20 stake token, and the descriptor has no @.value field.
- **approve**: approve is payable but no @.value field is shown.  
  Solady approve is payable and does not use callvalue, so the ETH stays in VeToken. No @.value is shown.
- **transferFrom**: transferFrom is payable but no @.value field is shown.  
  Solady transferFrom is payable and does not use callvalue. The ETH stays in the contract and no @.value is shown.
- **safeTransferFrom**: safeTransferFrom is payable but no @.value field is shown.  
  This function is payable and does not use msg.value. The onERC721Received call forwards no ETH, and no @.value is shown.
- **safeTransferFrom**: safeTransferFrom with data is payable but no @.value field is shown.  
  This function is payable and does not use msg.value. The ETH stays in the contract and no @.value is shown.

## `registry/ethena/calldata-ethena.json`

- **cooldownShares**: cooldownShares restarts the cooldown timer for all USDe the signer already has pending; nothing shown says so.  
  Each account has one cooldown record. The new USDe is added to it and the single end time is reset to now plus the full duration, so USDe already pending cannot be claimed until the new end time. This is like the calibrated 'existing stake folded into new delegation' critical. The screen shows only the intent and the new amount, and nothing on the not-critical list covers the change to the existing pending position.
- **cooldownAssets**: cooldownAssets restarts the cooldown timer for all USDe the signer already has pending; nothing shown says so.  
  This has the same code as cooldownShares. Any pending USDe joins the same record, and its end time is pushed back to now plus cooldownDuration (max 90 days). The intent and the Amount field do not say that USDe already in cooldown gets locked again.

## `registry/feral-file/calldata-feralfile-exhibition-v4-0.json`

- **buyArtworks**: buyArtworks is payable with no @.value field; in the vault path the ETH sent is unchecked.  
  When payByVaultContract is true, buyArtworks never checks msg.value. The contract pays out only `price`, using funds that come from the vault, so any ETH the signer sends stays in the contract. The exhibition contract has no withdraw function. The descriptor has no `@.value` field, and only the non-vault path ties msg.value to the price that is shown.

## `registry/feral-file/calldata-feralfile-exhibition-v4_1-0.json`

- **buyArtworks**: buyArtworks is payable, has no @.value field, and on the vault path nothing ties the sent ETH to Price.  
  When payByVaultContract is true, the vault pays the price and nothing checks msg.value or forces it to zero. Any ETH the signer attaches is kept in the exhibition contract on top of the price: payouts and the leftover transfer are computed from saleData_.price, not from msg.value. The descriptor has no @.value field, and 'Pay via vault: true' plus 'Price' make it look as if no ETH leaves the wallet. The severity guide lists this case as critical: 'A payable function ... has no @.value field and nothing forces the value to zero'. On the direct-pay path msg.value must equal Price, and Price is shown, so only the vault path is affected.

## `registry/feral-file/calldata-feralfile-exhibition-v4_2-0.json`

- **buyBulkArtworks**: buyBulkArtworks is payable with no @.value field; in vault mode the ETH sent is unchecked and unshown.  
  When payByVaultContract is true, nothing checks msg.value. The vault call forwards no value, and every payout is computed from saleData_.price, so any ETH the signer sends stays in the exhibition contract. The 'Price' field only matches the value sent in the non-vault branch, and no field shows the native value in vault mode, which matches the guide's 'payable function with no @.value and nothing forces the value to zero' example.

## `registry/feral-file/calldata-feralfile-exhibition-v4_3-0.json`

- **buyArtworks**: buyArtworks is payable with no @.value field; on the vault path msg.value is unchecked and lost.  
  When payByVaultContract is true, the vault pays and nothing checks msg.value, so any ETH the signer sends stays in the contract. The payout only uses saleData_.price, and the screen has no @.value field. 'Price' and 'Pay via vault' are shown, but neither gives the ETH actually sent on this path.

## `registry/feral-file/calldata-feralfile-exhibition-v4_4-0.json`

- **buyArtworks**: buyArtworks has no @.value field, and in vault mode nothing ties the ETH sent to the Price shown.  
  Without the vault, msg.value must equal the Price shown, so that path is covered. With payByVaultContract=true, nothing checks msg.value, so any ETH the signer attaches is accepted. Payouts use saleData_.price, not msg.value, and no withdraw or sweep function exists in the source here, so the extra ETH is either spent on the sale or stuck in the contract, and the screen never shows the amount.

## `registry/feral-file/calldata-feralfile-exhibition-v4_5-0.json`

- **buyArtworks**: buyArtworks: payable with no @.value field; when paying through the vault, the ETH sent is unchecked and never shown.  
  When payByVaultContract is true, the vault pays the price, and nothing checks or refunds msg.value. Any ETH the buyer sends stays in the exhibition contract, which has no withdraw function, and the descriptor has no @.value field. The 'Pay via vault' and 'Price' fields do not show the ETH that leaves the wallet; test case 6 only covers the non-vault branch, where msg.value must equal the price.

## `registry/flyingtulip/calldata-PftMarketplace.json`

- **buy**: buy: the signer pays price plus taker fee, but the screen shows only the price and no native value.  
  For native listings the contract keeps price plus taker fee from the value sent, and refunds only the excess. The screen shows only `expectedPrice` (0.123 S) and no native value, so 0.000369 S more leaves the wallet than the screen says. This is a storage fee rate that changes the amount the signer pays, so the amount rule makes it critical.
- **acceptBuyOffer**: acceptBuyOffer: the seller gets the offer price minus the maker fee, but the full price is shown.  
  The signer is the seller (msg.sender), and they receive the offer price minus the maker fee. The rest goes to the fee recipient. The screen shows the full `offer.price` as the only amount and says nothing about a fee. The maker fee is not zero in practice: case 7 shows 0.1% taken. This matches the 'recipient receives the amount minus a fee; full amount shown' critical.

## `registry/flyingtulip/eip712-LeverageRfqEngine.json`

- **LeveragedOrder**: LeveragedOrder Open action borrows sellAmount+feeAmount as new debt; nothing on screen says borrow or debt.  
  A signed OPEN order makes the PositionsManager borrow sellAmount+feeAmount against the user and deposit the bought token as collateral, so the signer takes on new debt. The screen calls it a spot sale and shows only the bare label "Open". Nothing mentions a borrow, debt or leverage, and the domain name is not displayed. No not-critical case covers this, so it is critical.
- **LeveragedOrder**: LeveragedOrder Close action is shown as a spot sale; it withdraws position collateral and uses the bought token to repay debt.  
  A CLOSE order takes the sold tokens out of the signer's position collateral, not from the wallet. The bought tokens repay the signer's debt instead of reaching the wallet. The screen shows a spot sale with a "Minimum buy" as if it were received, so the positions that change are shown differently. One caveat: the PositionsManager source is not in the directory, so the repay behaviour rests on the function name and this contract's own doc comment.

## `registry/gondi/calldata-MultiSourceLoan-v3_0.json`

- **repayLoan**: repayLoan shows only the principal; the interest the borrower pays is not shown and its inputs are hidden  
  The borrower pays principal plus stored and new interest, and the interest inputs in calldata are hidden. In case 0, 2.872705764840182649 WETH left the signer, but the screen only shows 'Loan principal 2.5 WETH' and no field gives the total or the APR.
- **refinanceFull**: refinanceFull does not show that the borrower pays the old debt above the new principal  
  The borrower pays the old principal plus interest beyond the new principal, and in case 1 that was 1.159932 USDC sent to the lender. The screen shows no payment from the signer, and it hides the interest inputs. Because the new principal is larger than the old one, it suggests the signer receives about 36,100 USDC.
- **refinancePartial**: refinancePartial shows the tranche principal, but the signer also pays accrued interest and a protocol fee  
  The signer, who is the new lender, pays the tranche principal plus accrued interest, split between the old lender and the protocol fee recipient. In case 2 that was 18.825612652173051329 WETH, but only 18.768606224568360647 WETH is shown. No field states the extra amount or its inputs.
- **refinanceFromLoanExecutionData**: refinanceFromLoanExecutionData hides the old-loan repayment the borrower pays, including accrued interest  
  The borrower pays the old lender principal plus about 42,464 USDC of stored interest plus new interest, which was 348,509.143734 USDC in case 4. The screen shows only the 300,000 USDC principal. The signer's net was -1,870 USDC, while the shown fields suggest a gain of about 46,600 USDC.

## `registry/gondi/calldata-MultiSourceLoan-v3_1.json`

- **refinanceFull**: refinanceFull never says the signer pays current lenders principal plus interest and pays protocol fees.  
  When the lender calls refinanceFull, the signer pays the old lender principal plus accrued interest minus the fee, and pays the protocol fee too. That came to 20.303 WETH in case 2. The screen only shows 20 WETH principal, and the calldata that sets the interest and fee is hidden. So more leaves the wallet than any shown value, and none of the not-critical cases covers this.
- **refinancePartial**: refinancePartial does not show the signer's payment to current lenders and the protocol fee.  
  The signer of refinancePartial is always the new lender. They pay the protocol fee on accrued interest out of their own wallet. They also pay the old lenders principal plus interest. The screen states none of this: the fee fraction and the tranche interest inputs are hidden calldata. Case 3 shows a real WETH transfer from the signer that nothing on screen states.

## `registry/gondi/calldata-PurchaseBundler-v3_1.json`

- **executeSellWithLoan**: executeSellWithLoan pulls the flash loan repayment from the signer's wallet; the screen never says so.  
  I could not refute this. In executeOperation, any shortfall between the flash-loan debt and the bundler's balance is pulled from the signer's wallet by transferFrom. In case 3 this pulled 29.828106748804350315 WETH, which is the 29.8132 WETH flash loan plus its premium. Nothing on the screen says this. The screen shows only the flash-loan amount from the pool, without the premium, and says the signer receives the new loan ("Principal receiver: 0x8463…33f2"). It does not say that WETH then leaves the signer's wallet. No item on the not-critical list covers this. The amount is not unreadable or shown through another field, the payer is not the contract, and the amount pulled is not capped by the new loan's principal.

## `registry/kyberswap/calldata-MetaAggregationRouterV2.json`

- **swap**: swap is payable but shows no @.value; hidden flags let msg.value exceed the amount or skip the check  
  swap is payable, and no path forces msg.value to equal the amount shown. With _SIMPLE_SWAP set, swap returns through swapSimpleMode before _collectExtraETHIfNeeded runs. swapSimpleMode only requires a non-ETH srcToken and never checks msg.value or refunds it, so any ETH sent stays in the router. With _REQUIRES_EXTRA_ETH set, the check is only msg.value > amount. For an ETH srcToken, _takeFee then starts from msg.value, so the whole msg.value goes to the fee receivers and callTarget, which is more than the amount shown. The descriptor has no @.value field and keeps flags at visible: never, so the screen never shows how much ETH leaves the wallet.

## `registry/lens/eip712-lens-lenshub.json`

- **Comment**: Comment hides the action modules and init data installed on the signer's new comment.  
  The comment path enables every listed action module on the signer's new publication and calls each one with the signer as executor and the hidden init data. The screen shows only the profile, content URI, pointed ids and nonce, so nothing states which modules now govern the signer's publication. Case 2 enables two modules that are not on the screen.
- **Post**: Post hides the action modules and init data installed on the signer's new post.  
  post() enables each hidden action module on the signer's new post and initializes it with the signer as executor and the hidden init data. The Post screen shows only the profile id, the post URI and the nonce. Nothing on the screen states which modules govern the signer's post.

## `registry/lens/eip712-lens-token-handle-registry.json`

- **unlink_with_sig**: unlink_with_sig: the primary type and its members do not exist in the verifying contract.  
  The verifying contract hashes only the Unlink(handleId,profileId,nonce,deadline) type. The descriptor key unlink_with_sig(handle_id,profile_id,signatureDeadline) uses a different type name and different member names, and it has no nonce. The guide lists a type the verifier does not use as critical.
- **unlink_with_sig**: unlink_with_sig: the EIP-712 domain name and version differ from the ones TokenHandleRegistry uses.  
  The proxy 0xd4f2…8844 resolves to the TokenHandleRegistry implementation. Its domain separator uses the name 'TokenHandleRegistry' and version '1', but the descriptor declares 'Lens Protocol Profiles' version '2'. The guide lists a domain the verifier does not use as critical.
- **unlink**: unlink: the EIP-712 domain name and version differ from the ones TokenHandleRegistry verifies.  
  The domain is shared by both formats, so the unlink format also declares a domain the contract does not use. A real Unlink message under name TokenHandleRegistry, version 1, never matches this descriptor.
- **unlink**: unlink: the format key uses primary type "unlink", but the contract hashes type "Unlink".  
  The members match in order and type, but the descriptor names the primary type 'unlink' and the contract hashes 'Unlink'. encodeType is case-sensitive, so the type hash differs; cases/1.json uses primaryType "unlink".

## `registry/lido/calldata-wstETH-referral-staker.json`

- **stakeETH**: stakeETH: the screen never says the signer receives wstETH. The reader expected stETH.  
  stakeETH always wraps the stETH it gets and sends the signer wstETH, never stETH. The case 0 trace shows the signer receives 12.597855047834535196 WSTETH for 15.49 ETH. The screen shows only "Stake ETH", "Stake 15.49 ETH" and "Amount to stake". The descriptor's contractName mentions wstETH, but the case screen does not show it, and nothing on screen says which token arrives. The blind reader expected about 15.49 stETH. The guide calls a different asset critical even when the value is the same. No item on the not-critical list covers this: the wrap is not stated anywhere, so it is not the prerequisite of a named action.

## `registry/lifi/calldata-LIFIDiamond.json`

- **startBridgeTokensViaSymbiosis**: Symbiosis: the calldata that decides recipient, chain and output is not on the screen at all  
  On the MetaRouter path the facet sends the signer's deposited minAmount to metaRoute. Where it lands is decided by callTo/callData and the swap calldata, and the facet never checks them against _bridgeData. callData, firstSwapCalldata and secondSwapCalldata are not fields in the format. The screen admits the recipient and chain are 'not enforced; Symbiosis calldata decides' but never shows the real recipient, chain or output token. This matches the guide's critical example of inner router calls that decide the recipient while nothing shown states them. Case 33 is synthetic (no txHash), so there is no mined effect to check against.
- **swapAndStartBridgeTokensViaSymbiosis**: Swap & Symbiosis: the calldata that decides recipient, chain and output is not shown  
  The swap entrypoint sets minAmount to the swap output, then calls the same _startBridge → _startBridgeViaMetaRouter. That path forwards _symbiosisData.callData and the two swap calldatas verbatim, and they decide where the principal is delivered. None of them is a field. The screen only labels the shown receiver and chain as not enforced, so the actual recipient, chain and output token are never shown. Case 63 is synthetic (no txHash), so there is no mined effect to check against.

## `registry/morpho/calldata-MorphoBundlerV3.json`

- **multicall**: multicall is payable but shows no field for msg.value, and the code does not check it against inner values.  
  multicall is payable and nothing checks msg.value against the bundle. Each inner call forwards only `bundle[i].value`, and the contract has no refund, so any surplus stays in Bundler3, where the next caller can take it. The descriptor has no `@.value` field. The per-call `amountPath` shows what each inner call receives, not what leaves the wallet, so this is not covered by not-critical item 2. The severity guide's own example puts a payable batch with no `@.value` field and no zero-value check in critical.

## `registry/morpho/calldata-VaultBundlesV1.json`

- **vaultBundlesV1Deposit**: vaultBundlesV1Deposit hides maxSharePriceE27, the only bound on how few vault shares the signer receives.  
  The signer chooses maxSharePriceE27 in calldata, and it is the only check on how few shares the vault mints to them. The descriptor hides it with `visible: never`, and no field shows the shares or a minimum. This matches the guide's critical example "how little may come back, is not shown". It is not covered by not-critical #6 (that case is `visible: optional`) or #3 (this is a calldata bound, not a value read from storage).
- **vaultBundlesV1Migrate**: vaultBundlesV1Migrate hides destMaxSharePriceE27, the only bound on how few destination shares the signer receives.  
  destMaxSharePriceE27 is the only calldata bound on how many destination-vault shares the signer receives, and the descriptor hides it with `visible: never`. No field shows the shares received or a minimum, so the screen does not state how little may come back. This is critical under the severity guide, and no not-critical case applies.

## `registry/okx/calldata-OkxDexRouterV1.0.7-multi-commission.json`

- **dagSwapByOrderId**: dagSwapByOrderId: a from-token commission in trailing calldata takes extra tokens beyond Amount to Send.  
  dagSwapByOrderId calls dagSwapTo. When the trailing calldata carries a from-token commission flag, the router pulls an extra amount from the signer on top of fromTokenAmount. No field shows this commission. _validateCommissionInfo only blocks it for the NO_TRANSFER, BY_INVEST and PERMIT2 modes, not for the legacy mode.
- **dagSwapByOrderId**: dagSwapByOrderId is payable but has no @.value field, so the native value sent is not shown.  
  The ERC20 branch forces the value to zero, but the ETH branch never compares msg.value with fromTokenAmount. Any ETH commission is paid on top of that amount from the router's balance. So the native value can be larger than the amount shown, and the excess stays in the router or goes out as commission.
- **dagSwapTo**: dagSwapTo shows 12.817259 USDT sent, but a hidden dual commission took 12.855826 USDT.  
  In the mined transaction the signer paid 12.855826 USDT. The screen shows 12.817259 USDT. Two referrers received the 0.038567 USDT difference, which _claimToken pulled from the signer, and nothing on the screen states it.
- **dagSwapTo**: dagSwapTo is payable but has no @.value field for the native value sent.  
  For an ETH input, msg.value is not tied to the amount shown. A from-token ETH commission is paid on top of it, and any excess value stays in the router. The value sent is never shown.
- **smartSwapByOrderId**: smartSwapByOrderId: a from-token commission in trailing calldata takes extra tokens beyond Amount to Send.  
  smartSwapByOrderId goes through _smartSwapTo with payer = msg.sender. A from-token commission pulls inputAmount*rate/(1e9-totalRate) more from the signer than the Amount to Send shown. No field shows it.
- **smartSwapByOrderId**: smartSwapByOrderId is payable with no @.value field and no check on msg.value.  
  Neither branch ties msg.value to the amount or forces it to zero for ERC20 inputs. Native value sent with the call stays in the router, or a commission or the receiver takes it. The screen does not show the value.
- **smartSwapTo**: smartSwapTo: a from-token commission in trailing calldata takes extra tokens beyond Amount to Send.  
  This is the same code path as smartSwapByOrderId with payer = msg.sender. A from-token commission pulls extra tokens beyond the Amount to Send shown, and the screen does not state it.
- **smartSwapTo**: smartSwapTo is payable with no @.value field and no check on msg.value.  
  The native value is neither shown nor bounded to the amount or zero. Excess ETH stays in the router, or the commission or the receiver takes it.
- **swapWrap**: swapWrap: the amount uses the mainnet WETH constant on all 24 chains.  
  The wallet resolves the constant on the transaction's chain. On Optimism, Mantle and the other non-mainnet deployments, that address is not the wrapped native token the router uses. So the asset shown is wrong there.
- **swapWrap**: swapWrap: the enum labels first byte 0x01 as WETH to ETH, but the code wraps ETH.  
  A first byte of 0x01 sets bit 248, not bit 255. The code ignores bit 248, so reversed is false and the code runs ETH→WETH. The screen labels that input 'WETH --> ETH'. Only 0x80 (128) maps correctly.
- **swapWrap**: swapWrap: a hidden commission changes the amount received or sent, and no @.value field exists.  
  With a from-token commission, the msg.value check is skipped and the ETH commission is paid on top of the amount. A to-token commission or trim cuts what the receiver gets below the Amount shown. Neither the value sent nor the commission is shown.
- **swapWrapToWithBaseRequest**: swapWrapToWithBaseRequest: a hidden commission changes the amount, and no @.value field exists.  
  This function uses the same _swapWrap code. Hidden from-token or to-token commissions change what the signer sends or what the receiver gets, and msg.value is not shown.
- **uniswapV3SwapTo**: uniswapV3SwapTo: the amount sent, minimum received and native value have no field.  
  No field shows the amount sent, the minimum received or the native value. The `amount` and `minReturn` parameters are not in the format at all, while sibling formats show sendAmount and minReceiveAmount.
- **uniswapV3SwapTo**: uniswapV3SwapTo: a hidden from-token commission took 0.0000085 ETH of the 0.001 ETH sent.  
  The router sent 0.0000085 ETH of the signer's 0.001 ETH to a referrer as commission. The screen shows nothing about the amount or the commission.
- **uniswapV3SwapToWithBaseRequest**: uniswapV3SwapToWithBaseRequest: a hidden from-token commission takes more than Amount to Send.  
  A from-token commission takes tokens or ETH from the signer on top of baseRequest.fromTokenAmount, which is shown as Amount to Send. The commission is not shown.
- **uniswapV3SwapToWithBaseRequest**: uniswapV3SwapToWithBaseRequest is payable with no @.value field.  
  The code only requires value ≥ amount. An ETH from-token commission is paid on top from the router balance, so msg.value is larger than the amount shown, and that value is not displayed.
- **unxswapByOrderId**: unxswapByOrderId shows 0.03966 ETH sent, but the signer sent 0.04 ETH.  
  The signer sent 0.04 ETH and the screen shows 0.03966 ETH. The 0.00034 ETH difference went to a commission referrer, and nothing on the screen states it.
- **unxswapTo**: unxswapTo is payable with no @.value field, and the code accepts value above amount.  
  Only value < amount reverts, so the signer can send more than the amount shown. A from-token ETH commission uses that excess, and any remaining excess stays in the router. The value is not shown.
- **unxswapTo**: unxswapTo: a hidden from-token commission takes more than Amount to Send.  
  A from-token commission set in the trailing calldata pulls tokens from the signer beyond the `amount` shown as Amount to Send. The screen does not show it.
- **unxswapToWithBaseRequest**: unxswapToWithBaseRequest is payable with no @.value field.  
  The code accepts any value ≥ amount for an ETH input, and an ETH commission is paid on top. So msg.value differs from the amount shown and is never displayed.
- **unxswapToWithBaseRequest**: unxswapToWithBaseRequest: a hidden from-token commission takes more than Amount to Send.  
  This is the same from-token commission path as unxswapTo. The signer pays more than baseRequest.fromTokenAmount, and no field states it.
- **smartSwapByInvest**: smartSwapByInvest is payable, never uses msg.value, and has no @.value field.  
  The function is payable and nothing forces msg.value to zero. ETH sent with the call stays in the router, or goes to `to` when toToken is ETH, and the screen never shows the value.
- **smartSwapByInvestWithRefund**: smartSwapByInvestWithRefund is payable, never uses msg.value, and has no @.value field.  
  No path forces the value to zero, so native value the signer sends is kept or forwarded without being shown.
- **unxswapByOrderId**: unxswapByOrderId is payable, and no field shows the ETH sent (@.value)  
  The function is payable, accepts value ≥ amount and pays an ETH commission from it. No field shows the 0.04 ETH that actually left the wallet.

## `registry/okx/calldata-OkxDexRouterV1.0.8-suffix-compat.json`

- **dagSwapByOrderId**: dagSwapByOrderId is payable but does not show @.value, and ETH sent is not bound to the shown amount  
  Only the ERC-20 branch forces msg.value to 0. On the ETH branch, the router wraps only fromTokenAmount and keeps any ETH sent above it, and the screen never shows msg.value.
- **dagSwapByOrderId**: dagSwapByOrderId hides a from-token commission that the signer pays on top of 'Amount to Send'  
  When the signed calldata carries a from-token commission suffix, the router pulls up to 3% extra from the signer and sends it to a referrer named in that suffix. No field shows the extra amount or the referrer, and the rate does not come from storage.
- **dagSwapTo**: dagSwapTo is payable but does not show @.value, and ETH sent is not bound to the shown amount  
  When the source is ETH, any ETH sent above fromTokenAmount stays in the router. The screen does not show the value sent.
- **dagSwapTo**: dagSwapTo hides a from-token commission that the signer pays on top of 'Amount to Send'  
  The suffix in the signed calldata sets a from-token commission that the signer pays on top of the amount shown. It goes to a referrer address that is never displayed.
- **smartSwapByOrderId**: smartSwapByOrderId is payable, does not show @.value, and never checks msg.value  
  Nothing forces msg.value to equal fromTokenAmount, or to be 0 on the ERC-20 path. ETH sent above the wrapped amount stays in the router, and the screen does not show it.
- **smartSwapByOrderId**: smartSwapByOrderId hides a from-token commission that the signer pays on top of 'Amount to Send'  
  In the default legacy transfer mode, the signer pays a from-token commission on top of 'Amount to Send' to a referrer set in the calldata suffix. No field shows it.
- **smartSwapTo**: smartSwapTo is payable, does not show @.value, and never checks msg.value  
  ETH sent above fromTokenAmount stays in the router. On an ERC-20 source with an ETH output, the ETH goes to the receiver through _transferTokenToUser. In both cases the value sent is not shown.
- **smartSwapTo**: smartSwapTo hides a from-token commission that the signer pays on top of 'Amount to Send'  
  The signer pays the extra from-token commission on top of the amount shown, and it goes to a referrer from the calldata suffix. Neither appears on the screen.
- **swapWrap**: swapWrap enum labels first byte 0x01 'WETH --> ETH', but the code wraps ETH then  
  A first byte of 0x01 leaves the top bit clear, so reversed = false and the code wraps ETH into WETH. The enum labels this value as the opposite action.
- **swapWrap**: swapWrap prices the amount as mainnet WETH on all 25 chains, where the router uses each chain's wrapped native token  
  The router wraps each chain's own native token, but the amount is priced as mainnet WETH on 24 of the 25 deployments. Only mainnet matches, so the claim of 'all 25' overstates it slightly.
- **swapWrap**: swapWrap hides a commission that adds to the amount paid or cuts the amount received, with no minimum  
  A from-token commission takes extra WETH or ETH from the signer beyond 'Amount' and skips the msg.value equality check. A to-token commission or trim cuts what the signer receives, with no minimum bound. Nothing on screen shows either.
- **swapWrapToWithBaseRequest**: swapWrapToWithBaseRequest hides a commission that adds to the amount paid or cuts what the receiver gets  
  The commission set in the calldata suffix either adds to what the signer pays or cuts what the receiver gets below the amount shown. Nothing bounds or shows it.
- **uniswapV3SwapTo**: uniswapV3SwapTo shows no amount spent, while its sibling formats show it  
  The amount spent has no field at all, while sibling formats such as uniswapV3SwapToWithBaseRequest show 'Amount to Send'. This matches the calibrated critical example.
- **uniswapV3SwapTo**: uniswapV3SwapTo shows no minimum received, so the slippage bound is hidden  
  The slippage bound is enforced but never shown, while sibling formats show 'Minimum to Receive'. The signer cannot see how little may come back.
- **uniswapV3SwapTo**: uniswapV3SwapTo is payable and hides @.value, and extra ETH above amount stays in the router  
  The code checks only callvalue >= amount and wraps only `amount`, so any extra ETH stays in the router. No ETH value is shown for this format at all.
- **uniswapV3SwapTo**: uniswapV3SwapTo hides a from-token commission that the signer pays on top of the amount  
  A from-token commission set in the calldata suffix makes the signer pay extra to a referrer. Neither the commission nor even the base amount is shown.
- **uniswapV3SwapToWithBaseRequest**: uniswapV3SwapToWithBaseRequest is payable and hides @.value, and extra ETH stays in the router  
  Only callvalue >= fromTokenAmount is enforced, so ETH above the amount shown stays in the router and is never displayed.
- **uniswapV3SwapToWithBaseRequest**: uniswapV3SwapToWithBaseRequest hides a from-token commission that the signer pays on top of 'Amount to Send'  
  The signer pays a from-token commission on top of 'Amount to Send' to a referrer from the calldata suffix. Nothing on screen shows it.
- **unxswapByOrderId**: unxswapByOrderId is payable and hides @.value, and ETH above amount stays in the router  
  On the ETH path, msg.value only has to be at least `amount`, and ETH above the amount stays in the router. The screen shows only `amount`.
- **unxswapByOrderId**: unxswapByOrderId hides a from-token commission that the signer pays on top of 'Amount to Send'  
  The signer pays a from-token commission beyond 'Amount to Send' to a referrer named only in the calldata suffix. It is not shown.
- **unxswapTo**: unxswapTo is payable and hides @.value, and ETH above amount stays in the router  
  On the ETH path, any value above `amount` is kept by the router and never shown.
- **unxswapTo**: unxswapTo hides a from-token commission that the signer pays on top of 'Amount to Send'  
  An extra from-token commission leaves the signer to a referrer from the calldata suffix, on top of the amount shown. No field shows it.
- **unxswapToWithBaseRequest**: unxswapToWithBaseRequest is payable and hides @.value, and ETH above the amount stays in the router  
  ETH sent above fromTokenAmount stays in the router, and the screen does not show the value sent.
- **unxswapToWithBaseRequest**: unxswapToWithBaseRequest hides a from-token commission that the signer pays on top of 'Amount to Send'  
  The signer pays a from-token commission on top of 'Amount to Send' to a referrer that is never displayed.
- **smartSwapByInvest**: smartSwapByInvest is payable, hides @.value, and never uses or refunds ETH sent  
  Any ETH sent stays in the router, or goes to `to` through _transferTokenToUser when the output is ETH. Nothing forces it to zero, and it is not shown.
- **smartSwapByInvestWithRefund**: smartSwapByInvestWithRefund is payable, hides @.value, and never uses or refunds ETH sent  
  The router keeps ETH sent with the call, or forwards it to `to` when the output is ETH. It is never refunded to refundTo, and it is never shown.
- **swapWrap**: swapWrap is payable, and no field shows the ETH sent (@.value)  
  On the unwrap path with a to-token commission or trim, and on the wrap path with a from-token commission, nothing binds msg.value to the amount shown. The router keeps the extra ETH or pays it out as commission.
- **swapWrapToWithBaseRequest**: swapWrapToWithBaseRequest is payable, and no field shows the ETH sent (@.value)  
  On the unwrap path, the ETH the signer sends is forwarded to `receiver` (possibly a third party), or kept when there is a commission or trim. On the wrap path with a from-token commission, the amount is not bound. The value sent is never shown.

## `registry/ondo-finance/calldata-GMTokenManager.json`

- **mintWithAttestation**: mintWithAttestation shows depositTokenAmount, but with USDon as deposit token it takes quantity times price instead.  
  When the deposit token is USDon, the contract ignores depositTokenAmount and takes quantity*price USDon from the signer. Both values come from calldata, and the price is hidden. So the screen states the amount that leaves the wallet as a different value from the one the code moves. This is not in the not-critical list: the price is a calldata value, not a storage value, and the shown amount is not an unused zero alternative.
- **redeemWithAttestation**: redeemWithAttestation shows a minimum received that the code does not check when receiveToken is USDon.  
  On the USDon path, the code never checks minimumReceiveAmount. The signer receives quantity*price, which comes from the hidden quote.price, and this can be less than the minimum the screen promises. The screen states a minimum received that the code does not enforce, and the real amount is not shown anywhere. That means how little may come back is shown wrong.

## `registry/opencover/calldata-Quote.json`

- **submitQuote**: submitQuote is payable but shows no @.value, and nothing forces it to zero for ERC20 payments.  
  On the ERC20 payment path msg.value is never checked, so any ETH sent stays in the contract. It is not added to pendingAmounts, so the operator's collect() can send it to the collector. The screen never shows the native value, which matches the guide's example of a payable function with no @.value.
- **submitQuoteV15**: submitQuoteV15 is payable but shows no @.value, and nothing forces it to zero for ERC20 payments.  
  This is the same code path as submitQuote. With an ERC20 payment asset, nothing stops a non-zero msg.value, and that ETH can be swept by collect(). The screen never shows the native value.

## `registry/opensea/eip712-opensea.json`

- **Order**: Order: maker relayer and protocol fees taken from the signer are hidden, so the price shown is not what the signer nets or pays.  
  The maker fee rate and the fee recipient are fields of the signed order, not values from storage. On the SplitFee path, executeFundsTransfer sends price*makerRelayerFee/10000 of the payment token from the signer (the maker) to feeRecipient. In case 0 (feeMethod 1 = SplitFee, side Sell, makerRelayerFee 250, WETH) that is 0.1875 WETH, so the signer nets 7.3125 WETH, not the 7.5 WETH shown. The descriptor marks makerRelayerFee, makerProtocolFee and feeRecipient `visible: never`, and no other field or the intent mentions a fee. The guide's examples list 'amount minus a fee, full amount shown' as critical, and not-critical item 3 does not apply because the fee rate comes from the signed order, not from storage.

## `registry/paraswap/calldata-AugustusSwapper-v6.2.json`

- **swapExactAmountInPro**: swapExactAmountInPro: the signer receives less than the 'Minimum to Receive' shown, because the partner fee is cut after the check.  
  The minimum check runs on the gross output before the fees and the 1-wei dust are cut, so the signer can receive less than the 'Minimum to Receive' shown. Case 7 shows this: the signer got 2.119879 USDC against 2.127035 shown. The fee comes from the hidden `partnerAndFee` and cuts the amount shown, which is the amount-rule exception, so it stays critical.
- **swapExactAmountOutOnUniswapV3**: swapExactAmountOutOnUniswapV3: the signer received 299.999999 USDC while the screen says exactly 300 USDC.  
  The screen states an exact 300 USDC, but the contract keeps 1 wei of dust and the signer receives 299.999999 USDC. The guide says size does not matter. The UniswapV3 facet source is not in the directory, but the mined transfer establishes the effect.

## `registry/permit/eip712-permit-polygon-bridged-usdc.json`

- **Permit**: Permit descriptor binds to domain version "2", but the contract verifies permits with version "1".  
  The only domain this contract checks against is built with version "1". It also puts the chain ID in a salt field, not in a chainId field. The descriptor binds to version "2", so it is tied to a domain the verifying contract never uses. The severity guide lists this as critical: "An EIP-712 domain or type that the verifying contract does not use". Neither the screen nor anything else in the descriptor fixes it. The claim about the name ("USD Coin" vs "USD Coin (PoS)") rests on storage set at initialize and can't be checked from the source, but the version mismatch is enough on its own.

## `registry/permit/eip712-permit-polygon-usdt.json`

- **Permit**: Permit descriptor binds to domain name "Tether USD", but the contract signs under domain name "USDT0" with a salt.  
  The proxy 0xc2132D…8F points to UChildUSDT0, and the screen's own "250 USDT0" shows the USDT0 upgrade is live. Its permit checks signatures against a domain named "USDT0" that uses a salt and has no chainId field, so the descriptor's "Tether USD" domain (and the chainId domain in the case) is not one the contract uses. The severity guide lists this case as critical: "An EIP-712 domain or type that the verifying contract does not use". None of the not-critical items cover it.

## `registry/quickswap/calldata-QuickSwap.json`

- **removeLiquidity**: removeLiquidity hides `liquidity`, the LP token amount that leaves the signer's wallet and is burned.  
  The code pulls `liquidity` LP tokens from the signer and burns them. The removeLiquidity format has no `liquidity` field, only amountAMin, amountBMin, to and deadline. Case 9's mined effects show 37.4166 UNI-V2 leaving the signer, and the screen never states that amount. The guide's example 'the amount spent ... has no field at all' covers this, and no not-critical case applies.
- **removeLiquidityETH**: removeLiquidityETH hides `liquidity`, the LP token amount the signer gives up.  
  removeLiquidityETH passes `liquidity` to removeLiquidity, which pulls that LP amount from msg.sender. The format shows only amountTokenMin, amountETHMin, to and deadline. Case 10's mined effects show 6.2093 UNI-V2 leaving the signer, and no field shows it.
- **removeLiquidityWithPermit**: removeLiquidityWithPermit hides `liquidity`, the LP amount permitted, taken and burned.  
  When approveMax is false, the permit grants exactly `liquidity`, and removeLiquidity then takes and burns `liquidity`. The screen shows 'Unlimited LP permit' as a raw bool but never shows the LP amount. So the amount that leaves the wallet is absent from the screen.
- **removeLiquidityETHWithPermit**: removeLiquidityETHWithPermit hides `liquidity`, the LP amount permitted, taken and burned.  
  The function permits `liquidity` LP tokens (or the maximum) and then calls removeLiquidityETH with `liquidity`, which pulls and burns that amount from the signer. The descriptor has no `liquidity` field, so the LP amount given up is not shown.
- **removeLiquidityETHSupportingFeeOnTransferTokens**: removeLiquidityETHSupportingFeeOnTransferTokens hides `liquidity`, the LP amount the signer burns.  
  This function calls removeLiquidity(token, WETH, liquidity, ...), which pulls `liquidity` LP tokens from msg.sender into the pair and burns them. The format shows only the two minimums, the beneficiary and the deadline. The LP amount is not shown.
- **removeLiquidityETHWithPermitSupportingFeeOnTransferTokens**: removeLiquidityETHWithPermitSupportingFeeOnTransferTokens hides `liquidity`, the LP amount permitted and burned.  
  The permit grants `liquidity` (or the maximum), and the inner call takes and burns `liquidity` LP tokens from the signer. The descriptor shows the approveMax bool but no field for the LP amount.

## `registry/rarible/eip712-rarible-exchange-v2-meta-tx.json`

- **MetaTransaction**: MetaTransaction is bound to a Polygon RoyaltiesRegistry that has no meta-transaction verification  
  The bound address is a non-proxy RoyaltiesRegistry (exact match). Its source and ABI have no meta-transaction, EIP-712 or ecrecover code, so this contract does not verify the MetaTransaction type or the 'Rarible' domain the descriptor declares. The severity guide lists 'An EIP-712 domain or type that the verifying contract does not use' as critical.

## `registry/rarible/eip712-rarible-exchange-v2.json`

- **Order**: Order: `data` is hidden (visible: never), so payout recipients and origin fees that cut or add to amounts are never shown.  
  `data` is hidden, and LibOrderData.parse decodes the payouts and origin fees from it. The seller's origin fees come out of the seller's proceeds. In case 0, the data holds originFees [(0x1cf0df2a…e18a, 0x1db = 475 bp)] with empty payouts, so 4.75% of the 0.075 ETH goes to a third party. Nothing on screen states this fee. Not-critical item 5 does not apply, because these hidden bytes move the signer's assets.
- **Order**: Order: 'Take asset amount' reads as what the seller gets, but royalties and fees are deducted first.  
  For a sell order, the ETH take side is the fee side. Before the seller's payout, doTransfersWithFees takes out the protocol fee (only the buyer's share for these V2 orders), the royalties from the registry, and the seller's origin fees. The screen shows only the full 'Take asset amount' (75000000000000000 and 4100000000000000000) and says nothing about these deductions. The guide's amount rule makes this critical: royalties are read from storage, but they cut the amount shown. In case 0, the 4.75% origin fee makes the cut a fact.

## `registry/safe/calldata-BatchExecutor.json`

- **batchExecute**: batchExecute: calls[].value (native currency leaving the Safe) is never its own field; empty-data transfers have no inner descriptor  
  The contract runs in the Safe through delegatecall and sends `calls[i].value` of the Safe's native currency to `calls[i].to`. Nothing in the code limits that value. The descriptor has no field for `calls.[].value`. `amountPath` only passes the value to an inner descriptor, which under the spec 'MAY reference' `@.value`, and the spec's fallback when no inner descriptor matches shows only a calldata hash and the callee. A plain transfer with empty data has no selector, so no inner descriptor exists and nothing on screen shows the amount. This matches the guide's critical example of native currency leaving in an amount never shown, and the not-critical cases do not cover it: the amount is not shown anywhere else, and it is a fact, not a possibility.

## `registry/safe/calldata-Safe-1.3.0.json`

- **setup**: setup decodes `data` as a normal call to `to`, but the Safe runs it as a delegate call.  
  setup always runs `data` as a delegate call, so `to`'s code runs in the Safe's own context and storage. The descriptor decodes `data` as a plain call to `to`, labels it "Module", and no field or intent says it is a delegate call. The severity guide's examples name this exact pattern as critical.
- **execTransaction**: execTransaction is payable, but no field shows the native value the signer sends.  
  execTransaction is payable and no check forces msg.value to zero. The Safe keeps any ETH the signer sends, and `execute` can forward it. No field shows `@.value`, so ETH leaves the signer's wallet in an amount the screen never shows.
- **execTransaction**: execTransaction shows no field for the recipient `to` or the native `value` the Safe sends.  
  `to` and `value` are only passed as parameters to the nested call. They are not fields of their own, and the spec only lets the nested descriptor show the amount ("MAY"). For a plain ETH transfer with empty `data` there is no nested descriptor, so nothing shows the amount. The spec fallback only "MAY" show the target, so the recipient is not guaranteed either.
- **execTransaction**: execTransaction decodes `data` as a call to `to`, but operation 1 runs it as a delegate call.  
  With operation 1 the Safe runs `to`'s code in its own context. The nested rendering still describes a normal call to `to`, such as a token transfer, which does not happen as shown. The "Operation type: Delegate Call" enum is shown, but it does not correct the nested call's stated outcome. The severity guide lists this exact pattern as critical.

## `registry/safe/calldata-Safe-1.4.1.json`

- **execTransaction**: execTransaction is payable, but no field shows the native value the signer sends.  
  No path reverts on a non-zero msg.value, so ETH the signer sends stays in the Safe. The amount is never shown. This matches the guide's example of a payable function with no `@.value` and nothing forcing it to zero.
- **execTransaction**: execTransaction never shows the `value` ETH that the Safe sends to `to`. A plain ETH transfer shows no amount.  
  The Safe sends `value` ETH to `to`, and no field in the format shows it. For a plain ETH transfer, `data` is empty and no nested descriptor exists, so the amount never appears. Not-critical case 5 does not apply, because the amount is not shown anywhere else.
- **execTransaction**: execTransaction decodes `data` as a call to `to`, even when `operation` makes it a delegate call.  
  When operation is 1, the nested data still renders as a normal call to `to`, but the code runs `to`'s code inside the Safe, so the outcome shown does not happen. The 'Operation type' field shows 'Delegate Call', but the guide lists this exact pattern as critical even with `operation` present.

## `registry/safe/calldata-Safe-1.5.0.json`

- **setup**: setup decodes `data` as a call to `to`, but the Safe delegate-calls `to` with it.  
  setup always delegate-calls `to` with `data`, so `to`'s code runs in the Safe with the Safe's balances and storage. The descriptor decodes `data` as an ordinary call to `to`, and no operation field, intent or label on the screen says it is a delegate call. This is the calibrated embedded-calldata critical.
- **execTransaction**: execTransaction is payable, but no field shows @.value, the native currency the signer sends.  
  No path reverts on non-zero msg.value. Native currency the executing signer sends stays in the Safe, which can then forward it through `execute`. No field shows @.value: the calldata field's amountPath is the inner `value` parameter, not the outer transaction's value.

## `registry/safe/calldata-SafeL2-1.3.0.json`

- **setup**: setup decodes `data` as a normal call to `to`, but the Safe delegate-calls it.  
  setup always delegate-calls `data` at `to`, so the code runs in the Safe's own context. The descriptor decodes `data` as a normal call to `to` and labels it 'Module', so the nested rendering states an outcome that does not occur. The severity guide lists this exact pattern as critical.
- **setup**: setup never shows the delegate-call target `to`; the screen shows only the 'Module' bytes.  
  The address whose code the new Safe runs by delegate call is never shown as a field. The calldata field only uses `to` as calleePath, and case 0 shows that the screen gives raw bytes with no target address. Arbitrary code that runs in the Safe can enable modules or set a guard, so a hidden target is a hidden effect on the account's rights.
- **execTransaction**: execTransaction is payable but shows no @.value; ETH sent by the signer is never displayed.  
  No path checks or refunds msg.value, so the ETH the executing signer sends stays in the Safe balance. The Safe can then forward it through `value` in the inner call. The screen never shows the amount of native currency that leaves the signer's wallet.
- **execTransaction**: execTransaction never shows the target `to` or the ETH `value` as fields; raw nested data hides them.  
  The Safe sends `value` ETH to `to` and runs `data` there, but neither one is a displayed field. In case 1 the screen does not show which token (USDC) moves. For a plain ETH send (data 0x), the screen shows neither the recipient nor the amount that leaves the Safe.
- **execTransaction**: execTransaction decodes `data` as a call to `to` even when operation makes it a delegate call.  
  When operation is 1, `to`'s code runs in the Safe's context, but the nested data is still decoded as a call to `to`. That rendering states an outcome that does not occur. The 'Operation type' enum shows 'Delegate Call', but this does not correct the wrong nested decoding. The severity guide's examples name this exact pattern as critical.

## `registry/safe/calldata-SafeL2-1.4.1.json`

- **setup**: setup decodes `data` as a plain call to `to`, but the Safe always delegate-calls it.  
  setupModules always delegate-calls `to` with `data`, so `to`'s code runs in the new Safe's own context and can change its owners, modules and storage. The descriptor decodes `data` as a plain call to `to`. The label is only 'Module', `to` has no field of its own, and nothing on screen says delegate call. The guide's examples list exactly this as critical: calldata decoded as a call to `to` while it actually runs as a delegate call.
- **execTransaction**: execTransaction is payable but shows no @.value, so native currency the executor sends is never shown.  
  Both Safe.execTransaction and the SafeL2 override are payable, and no path checks msg.value. The ETH the executor sends stays in the Safe, and the inner call can forward it through `value`. The format has no `@.value` field, and FORMATS.md lists none. The guide names an unchecked payable function with no `@.value` field as critical.
- **execTransaction**: execTransaction has no field for `value`, the native currency the Safe sends to `to`.  
  For a Call, execute sends `value` of the Safe's native currency to `to`. The descriptor uses `value` only as amountPath of the nested call, and the spec says the inner descriptor only MAY read it as @.value. With empty `data` (a plain ETH send), or with an inner ERC-20 descriptor that never reads @.value, no field shows the amount, and `to` has no field of its own either. This is not the 'value field next to a nested call' case in not-critical item 2, because there is no such field.
- **execTransaction**: execTransaction decodes `data` as a call to `to` even when operation 1 makes it a delegate call.  
  When operation == 1, execute delegate-calls `to`, which runs `to`'s code against the Safe's balances and storage and ignores `value`. The 'Transaction' field still resolves and shows the nested call as a normal call to `to`, with the amount from `value`, and no condition depends on `operation`. The 'Delegate Call' enum label sits next to a nested rendering that states an outcome that does not happen. The guide's examples name this exact pattern as critical.

## `registry/safe/calldata-SafeL2-1.5.0.json`

- **setup**: setup decodes the `data` field as a normal call to `to`, but the code always delegatecalls it.  
  Whenever `to` is non-zero, setup always delegatecalls `to`, so `to`'s code runs in the Safe's own context. The descriptor decodes `data` as a plain call to `to`. The only label is "Module", and no field or intent says the call is a delegate call. The guide's examples list exactly this case as critical: nested calldata decoded as a call when it actually runs as a delegate call.
- **execTransaction**: execTransaction is payable, but no field shows the native value the signer sends.  
  execTransaction is payable and no require forces msg.value to zero. Any ETH the signer sends goes into the Safe, and the same call can pass it on through `execute(to, value, ...)`. No field shows @.value, so this matches the guide's payable-function critical.
- **execTransaction**: execTransaction never shows the inner `to` and `value` as fields, so a plain ETH send shows nothing.  
  The inner `value` only reaches the screen if a nested descriptor chooses to show it. When `data` is empty there is no selector and no nested descriptor, so nothing shows the ETH that leaves the Safe. No outer field shows `value` either, and at best the spec's MAY fallback shows the callee. Not-critical case 2 needs a separate value field and case 5 needs the amount shown elsewhere; neither is present here.
- **execTransaction**: execTransaction decodes nested calldata as a call to `to`, even when the operation is a delegate call.  
  When operation is 1, the code runs `to`'s code in the Safe's own context. The nested rendering still describes a call to `to`, with the Safe as sender, so it states an outcome that does not happen. The guide's example table lists this pattern as critical, and the 'Delegate Call' enum label does not correct what the nested screen says.

## `registry/safe/calldata-SafeMigration-1.4.1.json`

- **migrateWithFallbackHandler**: migrateWithFallbackHandler also replaces the Safe's fallback handler, but shows the same "Migrate Safe" intent as migrateSingleton.  
  The function runs by delegatecall in the Safe. It changes the singleton and also replaces the Safe's fallback handler with the immutable SAFE_FALLBACK_HANDLER, which overwrites any custom handler and changes EIP-1271 and fallback behaviour. The screen is the same as for migrateSingleton, which does not touch the handler. So the intent cannot cover the handler swap by its meaning (not-critical #12 does not apply), and nothing on screen states this permanent change to the Safe's settings.
- **migrateL2WithFallbackHandler**: migrateL2WithFallbackHandler also replaces the Safe's fallback handler, but shows the same intent as migrateL2Singleton.  
  This is the same issue on the L2 path. The Safe's fallback handler is replaced along with the L2 singleton, but the screen is the same as for migrateL2Singleton, which keeps the existing handler. Nothing on screen tells the signer that the handler changes.

## `registry/safe/calldata-SafeMigration-1.5.0.json`

- **migrateWithFallbackHandler**: migrateWithFallbackHandler replaces the Safe's fallback handler, but the screen never mentions it.  
  The function runs by delegatecall in the Safe. It changes the singleton and also overwrites the Safe's fallback handler with the immutable SAFE_FALLBACK_HANDLER (0x3EfC…77f4). That handler controls EIP-1271 signature checks, token callbacks and 4337 handling. Nothing on screen says the handler changes, and the screen is the same as for the singleton-only migration. The contract offers a singleton-only path, so the handler change is not a required step of 'Migrate Safe' (not-critical item 12 does not apply). The function is non-payable, so no value issue.
- **migrateL2WithFallbackHandler**: migrateL2WithFallbackHandler replaces the Safe's fallback handler, but the screen never mentions it.  
  This is the same issue on the L2 path. The call sets the L2 singleton and replaces the Safe's fallback handler with the fixed SAFE_FALLBACK_HANDLER. The intent and the single `@.to` field never mention the handler change. The screen is the same as for migrateL2Singleton(), which leaves the handler as it is. Nothing in the code or the descriptor makes this change visible.

## `registry/safe/eip712-Safe-1.3.0.json`

- **SafeTx**: SafeTx decodes data as a call to `to` even when operation 1 makes it a delegatecall in the Safe.  
  For operation 1, Executor.execute runs a delegatecall: `to`'s code runs in the Safe's context with the Safe's balances, and `value` is not sent. The `data` field still decodes the nested call as a call to `to` with `value` as its amount. The enum line 'Delegate Call' does not fix the nested rendering, which states an outcome that does not happen. The severity guide lists this exact case as a critical.

## `registry/safe/eip712-Safe-1.4.1.json`

- **SafeTx**: SafeTx decodes data as a call to `to` with the Safe as sender, even for a DelegateCall  
  Executor.execute runs a delegatecall when operation is 1, so `to`'s code runs in the Safe's own context. The descriptor still decodes `data` as a plain call to `to` for any operation, with no condition. The screen does show 'Operation type: Delegate Call', but the nested decode does not change to match it. The severity guide lists this exact pattern as a calibrated critical, and test case 1 uses operation 1 to MultiSend.

## `registry/safe/eip712-Safe-1.5.0.json`

- **SafeTx**: SafeTx decodes nested data as a call to `to` and shows Value even when operation is Delegate Call.  
  When operation is 1, execTransaction delegatecalls into `to`, so `to`'s code runs against the Safe's own storage and balances and `value` is never sent. The screen still decodes the nested data as an ordinary call to `to` and shows Value as if it moves. The 'Operation type' enum only says 'Delegate Call' and does not correct the nested call's stated outcome. The severity guide lists this exact pattern as critical, and none of the not-critical cases covers it.

## `registry/safe/eip712-SafeL2-1.3.0.json`

- **SafeTx**: SafeTx decodes `data` as a call to `to` even when operation is a delegate call.  
  I confirmed this one. The `data` field always decodes the nested call as a call to `to`, and nothing checks `operation`. Executor.execute does a delegatecall when operation is 1, so `to`'s code runs with the Safe's storage and balances. The decoded nested call then states an outcome that does not happen. This matches a critical example in the severity guide almost word for word, and no item on the not-critical list covers it. The 'Operation type' enum row only names the mode; it does not correct the decoded call. Both test cases use operation 0 with empty data, so they never exercise this path.

## `registry/safe/eip712-SafeL2-1.4.1.json`

- **SafeTx**: SafeTx decodes `data` as a call to `to` with `value`, also when operation is Delegate Call.  
  When operation is 1, the code of `to` runs in the Safe's own storage, using the Safe's balances, and `value` is never sent. The calldata field still shows the nested call as a call to `to` with `value`, which is an outcome that does not happen. The descriptor does show an 'Operation type' enum that reads 'Delegate Call', but the severity guide lists this exact pattern as critical, and none of the not-critical cases cover a nested rendering that states a wrong outcome.

## `registry/safe/eip712-SafeL2-1.5.0.json`

- **SafeTx**: SafeTx decodes the nested data as a call to `to` with `value`, also when the operation is a delegate call.  
  When operation is 1, the Safe runs `to`'s code in its own account with its own balances and sends no value. The nested screen still describes a normal call to `to` that carries `value`, which is not what happens. The 'Operation type' enum row does show 'Delegate Call', but prompt.md's calibrated criticals cover this exact case: 'Embedded calldata is decoded as a call to `to` while `operation` can make it a delegate call', because the nested display states an outcome that does not occur.

## `registry/smartcredit/eip712-smartcredit.json`

- **LoanRequest**: LoanRequest is bound to the SMARTCREDIT ERC-20 token, which never verifies EIP-712 signatures or a LoanRequest type.  
  The descriptor binds LoanRequest to 0x72e9…, but that contract is a plain OpenZeppelin ERC-20. Its only addition is a constructor that mints, and it has no ecrecover, DOMAIN_SEPARATOR, typehash or LoanRequest handling. The token's name is 'SMARTCREDIT Token', not the domain name 'Credit Line'. So the domain and type the descriptor states are not used by the contract it names as verifier. The guide's examples list 'An EIP-712 domain or type that the verifying contract does not use' as critical. Whatever really consumes the signature is not in this directory, so nothing here proves the screen matches its effect.

## `registry/swissborg/calldata-NttManager.json`

- **transfer**: Short transfer is payable but has no @.value field, so the ETH delivery fee is never shown.  
  The short transfer overload is payable, and nothing forces msg.value to zero. _prepareForTransfer keeps msg.value up to totalPriceQuote and refunds only the excess. _sendMessageToTransceivers then forwards that amount to the transceivers, so ETH leaves the signer's wallet. The descriptor's short `transfer` format shows only amount, destinationChain and encodedDestinationAddress. It has no `@.value` field, while the 6-argument sibling format has `relayingFee`. This is the calibrated 'payable function without @.value' critical, and no case on the not-critical list covers it.

## `registry/threshold/calldata-Bridge.json`

- **requestRedemption**: requestRedemption: Amount reads as BTC received, but treasury and Bitcoin tx fees are cut from it.  
  The deployed Bridge.sol natspec says `amount` is the Bank balance taken from the signer, and that the BTC paid to the redeemer script is always lower: the treasury fee and the Bitcoin tx fee come out of it. The screen shows only "Amount 0.5BTC" under the intent "Request tBTC redemption". No field, label or intent mentions the fee cut. The prompt's amount rule covers this case: a storage fee rate that cuts what the signer receives from the amount shown is critical, not the info case for storage values. One limit: the Redemption library that computes the fees is not in the directory, and case 2 was not mined ("tx not found"). So this rests on the natspec of the deployed contract, not on the fee code or on a mined effect.

## `registry/uniswap/calldata-UniswapV3Router02.json`

- **exactInput**: exactInput is payable but has no @.value field, so ETH sent with the swap is never shown.  
  exactInput is payable and nothing checks msg.value. When the input token is WETH9, pay() wraps the signer's ETH and the screen shows it as WETH. For any other input token the ETH stays in the router, and anyone can take it with refundETH. The format has no @.value field. The guide's examples list this as critical, and it is not on the not-critical list.
- **exactInputSingle**: exactInputSingle is payable but has no @.value field, so ETH paid for a WETH swap is hidden.  
  exactInputSingle is payable and no path checks or rejects msg.value. With tokenIn == WETH9, the ETH is wrapped and spent, but the screen shows only 'Send … WETH'. With another tokenIn, the ETH stays in the router and anyone can claim it. The format has no @.value field.
- **exactOutput**: exactOutput is payable but has no @.value field, so ETH paid for the input is hidden.  
  exactOutput is payable with no msg.value check. The last callback calls pay(tokenOut, data.payer, …), and this wraps the sent ETH when the input token is WETH9. Any ETH not used, including all of it for a non-WETH input, stays in the router, and anyone can call refundETH to take it. No field shows @.value.
- **exactOutputSingle**: exactOutputSingle is payable but has no @.value field, so ETH paid for the input is hidden.  
  exactOutputSingle is payable with no msg.value check, and it pays through pay(). pay() wraps the router's ETH balance when the input is WETH9. Leftover ETH stays in the router, and anyone can claim it with refundETH. No field shows @.value.
- **swapExactTokensForTokens**: swapExactTokensForTokens is payable but has no @.value field, so ETH paid for WETH input is hidden.  
  swapExactTokensForTokens is payable and calls pay(path[0], …) with no msg.value check. Sent ETH is wrapped and spent when path[0] is WETH9. Otherwise it stays in the router, where anyone can take it. The format shows only amountIn, amountOutMin and to.
- **swapTokensForExactTokens**: swapTokensForExactTokens is payable but has no @.value field, so ETH paid for WETH input is hidden.  
  swapTokensForExactTokens is payable and calls pay(path[0], msg.sender, …) with no msg.value check. Sent ETH is wrapped when path[0] is WETH9, and any excess ETH stays in the router where anyone can claim it. No @.value field exists.

## `registry/yieldxyz/calldata-yieldxyz-usde-vault.json`

- **withdraw**: withdraw shows 'Withdraw exactly X USDe', but the receiver gets sUSDe  
  The screen says the receiver gets exactly X USDe. With hasCooldown on, which the mined redeem shows, the receiver instead gets previewWithdraw(X) sUSDe, a different asset and a different number, and no USDe at all. The storage-value exception in the severity guide applies: the stored flag changes what the signer receives against the amount shown, so this is critical.

