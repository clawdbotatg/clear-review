# Report

709 descriptors reviewed. Rubric v1.2.

fail: 68 · incomplete: 120 · pass: 521

Grades: A: 50 · B: 146 · C: 278 · D: 167 · F: 68

| Grade | Truth | Clarity | File | Worst finding |
|---|---|---|---|---|
| F | 0 | 18 | `registry/flyingtulip/eip712-LeverageRfqEngine.json` | LeveragedOrder Open action borrows sellAmount+feeAmount as new debt; nothing on screen says borrow or debt. |
| F | 0 | 55 | `registry/kyberswap/calldata-MetaAggregationRouterV2.json` | swap is payable but shows no @.value; hidden flags let msg.value exceed the amount or skip the check |
| F | 0 | 20 | `registry/lens/eip712-lens-token-handle-registry.json` | unlink_with_sig: the primary type and its members do not exist in the verifying contract. |
| F | 0 | 43 | `registry/okx/calldata-OkxDexRouterV1.0.7-multi-commission.json` | dagSwapByOrderId: a from-token commission in trailing calldata takes extra tokens beyond Amount to Send. |
| F | 0 | 34 | `registry/okx/calldata-OkxDexRouterV1.0.8-suffix-compat.json` | dagSwapByOrderId is payable but does not show @.value, and ETH sent is not bound to the shown amount |
| F | 0 | 41 | `registry/opencover/calldata-Quote.json` | submitQuote is payable but shows no @.value, and nothing forces it to zero for ERC20 payments. |
| F | 0 | 0 | `registry/rarible/eip712-rarible-exchange-v2-meta-tx.json` | MetaTransaction hides functionSignature, the call that runs in the signer's name |
| F | 0 | 2 | `registry/rarible/eip712-rarible-exchange-v2.json` | Order: `data` is hidden (visible: never), so payout recipients and origin fees that cut or add to amounts are never shown. |
| F | 0 | 35 | `registry/safe/calldata-BatchExecutor.json` | batchExecute: calls[].value (native currency leaving the Safe) is never its own field; empty-data transfers have no inner descriptor |
| F | 0 | 64 | `registry/uniswap/calldata-UniswapV3Router02.json` | exactInput is payable but has no @.value field, so ETH sent with the swap is never shown. |
| F | 5 | 58 | `registry/ekubo/calldata-VeToken.json` | stake is payable but no @.value field is shown, and native value sent is left in the contract. |
| F | 7 | 24 | `registry/ekubo/calldata-MEVCaptureRouter.json` | swap (isToken1, threshold) is payable, but the screen never shows the ETH sent (@.value). |
| F | 12 | 58 | `registry/ekubo/calldata-Positions.json` | deposit is payable and spends msg.value in native pools, but no @.value field is shown. |
| F | 12 | 56 | `registry/ekubo/calldata-Ve33Positions.json` | deposit is payable and spends msg.value for a native token0, but no @.value field exists |
| F | 17 | 57 | `registry/ekubo/calldata-Orders.json` | mintAndIncreaseSellAmount is payable and the descriptor has no @.value field, so the ETH sent is hidden. |
| F | 25 | 33 | `registry/HyperDiscipline/eip712-CommitIntent.json` | CommitIntent: 'Stake amount' shows the gross deposit, but the platform fee is cut before the stake is locked. |
| F | 25 | 36 | `registry/lido/calldata-wstETH-referral-staker.json` | stakeETH: the screen never says the signer receives wstETH. The reader expected stETH. |
| F | 25 | 68 | `registry/ondo-finance/calldata-GMTokenManager.json` | mintWithAttestation shows depositTokenAmount, but with USDon as deposit token it takes quantity times price instead. |
| F | 25 | 0 | `registry/opensea/eip712-opensea.json` | Order: maker relayer and protocol fees taken from the signer are hidden, so the price shown is not what the signer nets or pays. |
| F | 25 | 17 | `registry/paraswap/eip712-Velora-DeltaV2.json` | Order: on a cross-chain order the token received is bridge.outputToken, which is never shown |
| F | 25 | 50 | `registry/permit/eip712-permit-polygon-bridged-usdc.json` | Permit descriptor binds to domain version "2", but the contract verifies permits with version "1". |
| F | 25 | 42 | `registry/permit/eip712-permit-polygon-usdt.json` | Permit descriptor binds to domain name "Tether USD", but the contract signs under domain name "USDT0" with a salt. |
| F | 25 | 15 | `registry/safe/eip712-Safe-1.3.0.json` | SafeTx decodes data as a call to `to` even when operation 1 makes it a delegatecall in the Safe. |
| F | 25 | 0 | `registry/safe/eip712-Safe-1.4.1.json` | SafeTx decodes data as a call to `to` with the Safe as sender, even for a DelegateCall |
| F | 25 | 25 | `registry/safe/eip712-Safe-1.5.0.json` | SafeTx decodes nested data as a call to `to` and shows Value even when operation is Delegate Call. |
| F | 25 | 22 | `registry/safe/eip712-SafeL2-1.3.0.json` | SafeTx decodes `data` as a call to `to` even when operation is a delegate call. |
| F | 25 | 17 | `registry/safe/eip712-SafeL2-1.4.1.json` | SafeTx decodes `data` as a call to `to` with `value`, also when operation is Delegate Call. |
| F | 25 | 20 | `registry/safe/eip712-SafeL2-1.5.0.json` | SafeTx decodes the nested data as a call to `to` with `value`, also when the operation is a delegate call. |
| F | 25 | 0 | `registry/smartcredit/eip712-smartcredit.json` | LoanRequest is bound to the SMARTCREDIT ERC-20 token, which never verifies EIP-712 signatures or a LoanRequest type. |
| F | 31 | 52 | `registry/morpho/calldata-clearstar-CSUSDC-8453.json` | redeem shows the burned shares as CSUSDC, but the signer's shares are COUSDC. |
| F | 33 | 48 | `registry/ekubo/calldata-Ve33Periphery.json` | scheduleEmissions: the STONX transfer out of the signer's wallet and its amount are not shown |
| F | 39 | 42 | `registry/morpho/calldata-VaultBundlesV1.json` | vaultBundlesV1Deposit hides maxSharePriceE27, the only bound on how few vault shares the signer receives. |
| F | 40 | 26 | `registry/morpho/calldata-MorphoBundlerV3.json` | multicall is payable but shows no field for msg.value, and the code does not check it against inner values. |
| F | 45 | 48 | `registry/swissborg/calldata-NttManager.json` | Short transfer is payable but has no @.value field, so the ETH delivery fee is never shown. |
| D | 50 | 68 | `registry/bedrock/calldata-selini-vault.json` | mint names suniBTC as the output but does not show the suniBTC amount the signer receives. |
| F | 50 | 48 | `registry/ethena/calldata-ethena.json` | cooldownShares restarts the cooldown timer for all USDe the signer already has pending; nothing shown says so. |
| D | 50 | 75 | `registry/morpho/calldata-clearstar-CSCOREETH-v2-8453.json` | deposit: the 'Share ticker' constant CSCOREETH does not match the vault token's on-chain symbol CSRETH. |
| D | 50 | 63 | `registry/morpho/calldata-kpk-KPK_USDC_Prime_Core-v2-1.json` | mint: the shares are shown as KPK_USDC_Prime_Core but the mined share token symbol is KPK_USDC_BluechipV2 |
| D | 50 | 67 | `registry/morpho/calldata-sentora-senPYUSDmain-v2-1.json` | mint shows the minted shares as senPYUSDmain, but the on-chain symbol is senPYUSDV2. |
| D | 50 | 59 | `registry/morpho/calldata-waterline-infinifiUSDC.json` | mint shows minted shares as 'infinifiUSDC', but the token symbol is 'steakUSDCinfinifi'. |
| D | 50 | 66 | `registry/swissborg/calldata-ChsbToBorgMigrator.json` | migrate: screen promises a CHSB-to-BORG migration, but the current code always reverts with MIGRATION_CLOSED. |
| F | 62 | 53 | `registry/feral-file/calldata-feralfile-vault-v2-0.json` | payForSaleV2 shows destination as 'Recipient', but the vault sends the price to the signer. |
| F | 62 | 35 | `registry/safe/calldata-SafeMigration-1.4.1.json` | migrateWithFallbackHandler also replaces the Safe's fallback handler, but shows the same "Migrate Safe" intent as migrateSingleton. |
| F | 62 | 38 | `registry/safe/calldata-SafeMigration-1.5.0.json` | migrateWithFallbackHandler replaces the Safe's fallback handler, but the screen never mentions it. |
| F | 63 | 31 | `registry/morpho/calldata-VaultExitBundlesV1.json` | ForceWithdrawVaultV2 hides minSharePriceE27, the only slippage bound on vault shares burned |
| F | 65 | 72 | `registry/flyingtulip/calldata-PftMarketplace.json` | buy: the signer pays price plus taker fee, but the screen shows only the price and no native value. |
| F | 66 | 41 | `registry/1inch/calldata-AggregationRouterV5.json` | swap is payable and the extra-ETH flag lets msg.value exceed the shown amount; no value field exists |
| F | 67 | 49 | `registry/1inch/calldata-AggregationRouterV3.json` | swap is payable and has no @.value field; the REQUIRES_EXTRA_ETH flag lets ETH above desc.amount leave unshown |
| D | 67 | 67 | `registry/morpho/calldata-clearstar-CSRWAUSDC-v2-8453.json` | deposit shows the share ticker CSRWAUSDC, but the vault token symbol on chain is CSRUSDC. |
| D | 67 | 74 | `registry/morpho/calldata-gauntlet-uniUSDC-v2-1.json` | deposit: the constant 'Share ticker' uniUSDC differs from the vault's on-chain share symbol usdcpv. |
| D | 67 | 75 | `registry/morpho/calldata-steakhouse_financial-bitgetUSDC-v2-42161.json` | deposit: constant share ticker 'bitgetUSDC' differs from the vault token's on-chain symbol 'bbqUSDC'. |
| D | 67 | 73 | `registry/morpho/calldata-waterline-reservoirUSDC-v2-1.json` | deposit: the 'Share ticker' constant reservoirUSDC differs from the token's on-chain symbol, bbqSUDCreservoir. |
| D | 67 | 62 | `registry/morpho/calldata-waterline-reservoirUSDC.json` | deposit shows share ticker "reservoirUSDC", but the vault token symbol is "bbqUSDCreservoir". |
| F | 68 | 58 | `registry/gondi/calldata-MultiSourceLoan-v3_0.json` | refinanceFull does not show that the borrower pays the old debt above the new principal |
| F | 69 | 52 | `registry/gondi/calldata-PurchaseBundler-v3_1.json` | executeSellWithLoan pulls the flash loan repayment from the signer's wallet; the screen never says so. |
| F | 69 | 50 | `registry/safe/calldata-Safe-1.3.0.json` | execTransaction is payable, but no field shows the native value the signer sends. |
| C | 70 | 30 | `registry/permit/eip712-permit-polygon-dai.json` | Permit: expiry=0 means the signature never expires, but the field is hidden in that case. |
| F | 70 | 72 | `registry/quickswap/calldata-QuickSwap.json` | removeLiquidity hides `liquidity`, the LP token amount that leaves the signer's wallet and is burned. |
| F | 71 | 41 | `registry/1inch/calldata-AggregationRouterV6.json` | permitAndCall is payable and the inner delegatecall spends msg.value, but no field shows the native value. |
| F | 71 | 58 | `registry/gondi/calldata-MultiSourceLoan-v3_1.json` | refinanceFull never says the signer pays current lenders principal plus interest and pays protocol fees. |
| F | 71 | 58 | `registry/safe/calldata-SafeL2-1.3.0.json` | setup decodes `data` as a normal call to `to`, but the Safe delegate-calls it. |
| D | 75 | 54 | `registry/kiln/calldata-Vault-RLUSD-Euler-Yield.json` | deposit shows share ticker kEulerRLUSD, but the vault share symbol on chain is keeyRLUSD. |
| D | 75 | 56 | `registry/kiln/calldata-Vault-USDC-Euler-Yield.json` | deposit shows share ticker "kEulerUSDC", but the vault token symbol is "keeyUSDC". |
| D | 75 | 62 | `registry/kiln/calldata-Vault-USDT-Euler-Yield.json` | deposit: the 'Share ticker' constant says kEulerUSDT, but the vault's share token symbol is keeyUSDT. |
| D | 75 | 60 | `registry/kiln/calldata-Vault-USDe-Euler-Yield-USDE.json` | deposit: the constant 'Share ticker' kEulerUSDe does not match the share token's on-chain symbol keeyUSDE. |
| D | 75 | 67 | `registry/morpho/calldata-bitwise-BPRIME-v2-8453.json` | deposit: the hard-coded share ticker 'BPRIME' differs from the vault token's on-chain symbol 'jvhhUSDC'. |
| D | 75 | 63 | `registry/morpho/calldata-clearstar-YCSUSDC.json` | deposit shows share ticker 'YCSUSDC', but the vault token's symbol is HYCSUSDC on chain. |
| D | 75 | 68 | `registry/morpho/calldata-flowdesk-fcUSDT-v2-1.json` | deposit: the hard-coded 'Share ticker' fcUSDT differs from the vault's on-chain symbol fUSDTe. |
| D | 75 | 56 | `registry/morpho/calldata-gauntlet-gtUSDAcore.json` | mint shows the underlying ticker "USDA", but the token's on-chain symbol is agUSD. |
| D | 75 | 66 | `registry/morpho/calldata-gauntlet-gtusdcf-v2-1.json` | deposit: hard-coded 'Share ticker' gtusdcf does not match the vault share symbol gtUSDChy. |
| D | 75 | 68 | `registry/morpho/calldata-gauntlet-gtwethp-v2-1.json` | withdraw: the screen never says that gtwethp vault shares are burned from the owner. |
| D | 75 | 67 | `registry/morpho/calldata-mev_capital-MC-USDC-v2-1.json` | withdraw never says that MC-USDC vault shares are burned from the owner to pay for the USDC |
| D | 75 | 66 | `registry/morpho/calldata-sentora-senPYUSDPRIMEv2-v2-1.json` | withdraw: nothing on the screen says the owner's senPYUSDPRIMEv2 shares are burned. |
| D | 75 | 65 | `registry/morpho/calldata-waterline-infinifiUSDC-v2-1.json` | deposit shows the share ticker 'infinifiUSDC', but the vault token's on-chain symbol is 'bbqUSDCinfinifi'. |
| F | 75 | 56 | `registry/safe/calldata-Safe-1.5.0.json` | execTransaction is payable, but no field shows @.value, the native currency the signer sends. |
| F | 75 | 60 | `registry/safe/calldata-SafeL2-1.4.1.json` | execTransaction is payable but shows no @.value, so native currency the executor sends is never shown. |
| F | 75 | 56 | `registry/safe/calldata-SafeL2-1.5.0.json` | execTransaction is payable, but no field shows the native value the signer sends. |
| F | 75 | 41 | `registry/threshold/calldata-Bridge.json` | requestRedemption: Amount reads as BTC received, but treasury and Bitcoin tx fees are cut from it. |
| D | 76 | 46 | `registry/gondi/calldata-PurchaseBundler-v3_2.json` | sell: the screen shows the loan principal, but the signer pays principal plus interest plus a protocol fee |
| F | 77 | 66 | `registry/safe/calldata-Safe-1.4.1.json` | execTransaction is payable, but no field shows the native value the signer sends. |
| F | 78 | 37 | `registry/1inch/calldata-AggregationRouterV4-eth.json` | swap hides msg.value; with the extra-ETH flag the signer sends more ETH than the amount shown. |
| F | 78 | 22 | `registry/1inch/calldata-AggregationRouterV4.json` | swap is payable, but msg.value is never shown and a hidden flag lets it exceed the shown amount |
| D | 78 | 69 | `registry/morpho/calldata-re7_labs-Re7WETH-v2-10.json` | redeem never names WETH as the asset the receiver gets; only the shares burned are shown. |
| D | 79 | 34 | `registry/midas/calldata-RedemptionVault.json` | redeemInstant does not say that part of the amount is a mToken fee sent to feeReceiver. |
| F | 79 | 50 | `registry/yieldxyz/calldata-yieldxyz-pol-validator.json` | sellVoucher_newPOL: pending POL rewards are paid to the signer, and the screen does not say so. |
| C | 80 | 8 | `registry/1inch/eip712-1inch-limit-order.json` | Order 'Receive minimum' shows the full-fill total, but partial fills pay proportionally less. |
| C | 80 | 22 | `registry/1inch/eip712-AggregationRouterV6.json` | Order hides the expiration in makerTraits, so the signer cannot see how long the offer stays fillable. |
| B | 80 | 65 | `registry/flare/calldata-FXRP-OFT-Flare.json` | send: composeMsg is visible: never, but a non-empty one makes the destination call the recipient with hidden data. |
| C | 80 | 39 | `registry/gondi/eip712-LoanOffer-v3_2.json` | LoanOffer shows 'Collection' as the collateral, but a non-zero validator decides the collateral instead. |
| C | 80 | 51 | `registry/hyperliquid/calldata-CctpExtension.json` | The Destination DEX slice [52:53] reads only the first byte of a 4-byte DEX id in the hook. |
| D | 80 | 80 | `registry/morpho/calldata-gauntlet-uniETH-v2-1.json` | redeem: the screen never says WETH is received, though the underlying token is a known constant. |
| D | 80 | 80 | `registry/morpho/calldata-gauntlet-uniUSDT-v2-1.json` | redeem: neither the intent nor any field says USDT is received; the payout asset is unnamed. |
| D | 80 | 74 | `registry/morpho/calldata-kpk-KPK_ETH_Prime-v2-1.json` | redeem: the shares show the ticker KPK_ETH_Prime, but the token's on-chain symbol is kpk_WETH_v2. |
| C | 80 | 23 | `registry/uniswap/eip712-UniswapX-DutchOrder.json` | Dutch order 'Spend max' shows inputStartAmount, but the input decays up to the hidden inputEndAmount. |
| F | 81 | 66 | `registry/paraswap/calldata-AugustusSwapper-v6.2.json` | swapExactAmountInPro: the signer receives less than the 'Minimum to Receive' shown, because the partner fee is cut after the check. |
| F | 81 | 38 | `registry/yieldxyz/calldata-yieldxyz-usde-vault.json` | withdraw shows 'Withdraw exactly X USDe', but the receiver gets sUSDe |
| D | 83 | 83 | `registry/lido/calldata-stETH.json` | submit: the screen never says the signer receives stETH in return for the ETH. |
| D | 83 | 73 | `registry/morpho/calldata-anthias_labs-mwcbBTC-v2-8453.json` | redeem: the screen never names cbBTC as the asset the receiver gets. |
| D | 83 | 75 | `registry/morpho/calldata-architect-archGV1USDC-v2-8453.json` | redeem: the screen never names USDC as the asset paid out to the receiver. |
| D | 83 | 76 | `registry/morpho/calldata-armitage_by_wintermute-pendleUSDC-v2-1.json` | redeem: the screen never names USDC as the asset paid out to the receiver. |
| D | 83 | 81 | `registry/morpho/calldata-august_digital-augustUSDCv2-v2-1.json` | redeem: the screen never names USDC as the asset the receiver gets. |
| D | 83 | 79 | `registry/morpho/calldata-clearstar-CS3JANECO-v2-1.json` | redeem never says the receiver gets USDC; the asset received is missing from the intent and the fields. |
| D | 83 | 80 | `registry/morpho/calldata-clearstar-CSBUSDC-v2-1.json` | redeem: the asset received (USDC) is not named anywhere on the screen. |
| D | 83 | 77 | `registry/morpho/calldata-felix-feUSDEv2-v2-999.json` | redeem: the screen never says that USDe is what the receiver gets; only the shares going out are named. |
| D | 83 | 64 | `registry/morpho/calldata-felix-feUSDT0.json` | redeem: the screen never names USD₮0 as the asset paid out to the receiver. |
| D | 83 | 66 | `registry/morpho/calldata-felix-feUSDT02.json` | redeem never names USD₮0 as the asset the recipient gets; the signer must guess the token. |
| D | 83 | 64 | `registry/morpho/calldata-felix-feUSDhl.json` | redeem never names USDHL as the asset that the receiver gets. |
| D | 83 | 76 | `registry/morpho/calldata-galaxy_curation-gUSDCq-v2-8453.json` | redeem: the screen never says that USDC arrives at the receiver; only the shares redeemed are named. |
| D | 83 | 78 | `registry/morpho/calldata-galaxy_curation-gWETHq-v2-1.json` | redeem never names WETH as the asset the receiver gets, although the descriptor has the constant. |
| D | 83 | 80 | `registry/morpho/calldata-hyperithm-hypercbBTCa-v2-143.json` | redeem: the screen never names cbBTC as the asset the receiver gets. |
| D | 83 | 76 | `registry/morpho/calldata-kpk-KPK_ETH_Yield-v2-1.json` | redeem: the screen never says WETH is received; the reader could not tell which asset arrives. |
| D | 83 | 73 | `registry/morpho/calldata-kpk-KPK_USDC_Yield-v2-8453.json` | redeem: the screen never says that USDC is paid out, although the asset is a fixed constant. |
| D | 83 | 71 | `registry/morpho/calldata-kpk-KPK_wARS_Yield-v2-1.json` | redeem: the screen never says the payout is wARS, though the descriptor has it as a constant. |
| D | 83 | 81 | `registry/morpho/calldata-mev_capital-mcHYPE-v2-999.json` | redeem: the screen never names WHYPE as the asset paid out, though the descriptor has it as a constant. |
| D | 83 | 72 | `registry/morpho/calldata-mev_capital-mcHYPE.json` | redeem: the screen never names WHYPE as the asset the receiver gets, unlike the deposit and withdraw screens. |
| D | 83 | 68 | `registry/morpho/calldata-pangolins-pUSDC.json` | redeem never names USDC as the asset the receiver gets for the burned shares. |
| D | 83 | 80 | `registry/morpho/calldata-re7_labs-re7frxUSD-v2-1.json` | redeem: the screen never names frxUSD as the asset the receiver gets. |
| D | 83 | 77 | `registry/morpho/calldata-rockawayx-figrUSDC-v2-1.json` | redeem: the screen never names USDC as the asset the receiver gets. |
| D | 83 | 74 | `registry/morpho/calldata-rockawayx-roxNUVA-v2-1.json` | redeem never names USDC as the asset the receiver gets; the screen shows only the shares. |
| D | 83 | 74 | `registry/morpho/calldata-sharpbyte-sbUSDT-v2-1.json` | deposit: constant share ticker 'sbUSDT' does not match the vault's on-chain symbol 'sbUSDTx'. |
| D | 83 | 76 | `registry/morpho/calldata-sky_money-skyMoneyUsdtSavings-v2-1.json` | redeem: the screen never names USDT as the asset the receiver gets. |
| D | 83 | 81 | `registry/morpho/calldata-sparkdao-sparkUSDTbc-v2-1.json` | The redeem screen never names USDT as the asset paid out; only the share ticker hints at it. |
| D | 83 | 80 | `registry/morpho/calldata-stake_dao-sdFRXUSDv2-v2-1.json` | redeem: the screen never says the payout is frxUSD, although the descriptor has that constant. |
| D | 83 | 80 | `registry/morpho/calldata-stake_dao-sdUSDCv2-v2-1.json` | redeem: the screen never says USDC is the asset sent to the receiver. |
| D | 83 | 75 | `registry/morpho/calldata-steakhouse_financial-bbqTGBP-v2-1.json` | redeem: the asset received (tGBP) is named nowhere on the screen. |
| D | 83 | 68 | `registry/morpho/calldata-steakhouse_financial-bitgetUSDT0-v2-42161.json` | redeem never names USDT0 as the asset the receiver gets. |
| D | 83 | 72 | `registry/morpho/calldata-steakhouse_financial-steakETH-v2-1.json` | redeem: the screen never says the signer receives WETH, so the reader could not tell ETH from WETH. |
| D | 83 | 67 | `registry/morpho/calldata-steakhouse_financial-steakETH-v2-143.json` | redeem: the screen never says the signer receives WETH, though the descriptor already defines the underlying ticker constant |
| D | 83 | 68 | `registry/morpho/calldata-steakhouse_financial-steakUSDC-1.json` | redeem: the asset received (USDC) is named nowhere on the screen. The reader only guessed it. |
| D | 83 | 71 | `registry/morpho/calldata-waterline-m1USDC-v2-1.json` | redeem never names USDC as the asset the receiver gets |
| D | 83 | 71 | `registry/morpho/calldata-yearn-ymvOG-WETH.json` | redeem never names WETH as the asset the receiver gets; the reader had to guess the payout token. |
| C | 85 | 38 | `registry/flare/calldata-RewardManager-Songbird.json` | claimProxy only accepts calls from the FtsoRewardManager contract, so no signer can call it directly. |
| F | 85 | 17 | `registry/lens/eip712-lens-lenshub.json` | Act hides the action module and its data, which decide what the signer pays and to whom. |
| D | 85 | 72 | `registry/morpho/calldata-kpk-KPK_USDC_Prime-v2-1.json` | redeem: nothing on the screen names USDC as the asset that arrives, though the sibling mint format does. |
| F | 88 | 72 | `registry/aave/calldata-lpv2.json` | swapBorrowRateMode intent says 'Swap to variable', but rateMode 2 moves debt to stable on Polygon/Avalanche. |
| D | 88 | 63 | `registry/gondi/calldata-MultiSourceLoan-v3_2.json` | repayLoan shows only the loan principal; interest and protocol fee also leave the signer. |
| D | 88 | 53 | `registry/kiln/calldata-Vault-EURC-Morpho-Gauntlet-Core.json` | redeem never names EURC as the asset the receiver gets. Mint shows the underlying ticker. |
| D | 88 | 57 | `registry/kiln/calldata-Vault-USDC-Aave-v3.json` | redeem never names USDC as the asset the receiver gets back. |
| D | 88 | 58 | `registry/kiln/calldata-Vault-USDT-Morpho-Gauntlet-Prime.json` | redeem: no field names USDT as the asset the signer receives. |
| D | 88 | 60 | `registry/morpho/calldata-9summits-9SUSDC11Core.json` | redeem never names USDC as the asset the receiver gets, though mint shows it as a constant. |
| D | 88 | 68 | `registry/morpho/calldata-api3-Api3CoreUSDC-v2-1.json` | redeem: the asset the signer receives (USDC) is never named on screen. |
| D | 88 | 68 | `registry/morpho/calldata-api3-PurintaUSDC-v2-1.json` | redeem never names USDC as the asset the receiver gets; the sibling mint format names it. |
| D | 88 | 67 | `registry/morpho/calldata-armitage_by_wintermute-armUSDTp-v2-1.json` | redeem: the asset received (USDT) is never named, though mint and deposit name it via constants. |
| D | 88 | 70 | `registry/morpho/calldata-august_digital-AugustUSDCv2-v2-143.json` | redeem: the asset paid out (USDC) is never named, although sibling formats show it as a constant. |
| D | 88 | 55 | `registry/morpho/calldata-b_protocol-reUSDC.json` | redeem never names USDC as the asset the recipient receives, though the descriptor has a constant for it. |
| D | 88 | 58 | `registry/morpho/calldata-block_analitica-bbETH.json` | redeem never names WETH as the asset the receiver gets back. |
| D | 88 | 55 | `registry/morpho/calldata-block_analitica-bbUSDC.json` | redeem never names USDC as the asset paid out, unlike the deposit and mint formats. |
| D | 88 | 56 | `registry/morpho/calldata-block_analitica-bbUSDT.json` | redeem: the screen never names USDT as the asset the signer receives. |
| D | 88 | 64 | `registry/morpho/calldata-clearstar-CSETH.json` | redeem never names WETH as the asset received, so the signer cannot tell ETH from WETH. |
| D | 88 | 65 | `registry/morpho/calldata-clearstar-CSUSDCCORE-v2-1.json` | redeem: the asset received (USDC) is never named on the screen. |
| D | 88 | 67 | `registry/morpho/calldata-felix-feHYPEv2-v2-999.json` | redeem: the WHYPE paid out to the receiver is never named on the screen. |
| D | 88 | 69 | `registry/morpho/calldata-felix-feUSDCv2-v2-999.json` | redeem: the screen never names USDC as the asset paid out, though the descriptor has the constant |
| D | 88 | 64 | `registry/morpho/calldata-flowdesk-fAUSDe-v2-1.json` | redeem never names AUSD as the asset the receiver gets, though mint shows it as a constant |
| D | 88 | 69 | `registry/morpho/calldata-gauntlet-bitmxnbp-v2-8453.json` | redeem: the screen never names MXNB as the asset received, though deposit and mint show it. |
| D | 88 | 52 | `registry/morpho/calldata-gauntlet-compWETH.json` | redeem: the asset received (WETH) is never named on screen, though mint shows it as a constant. |
| D | 88 | 61 | `registry/morpho/calldata-gauntlet-exmWETH.json` | redeem does not name WETH as the asset the receiver gets, unlike the sibling mint format. |
| D | 88 | 66 | `registry/morpho/calldata-gauntlet-gtLRTcore.json` | redeem: the screen never says WETH is received; mint shows it as a constant. |
| D | 88 | 61 | `registry/morpho/calldata-gauntlet-gtUSDC.json` | redeem never names USDC as the asset the receiver gets; mint shows the underlying ticker, redeem does not. |
| D | 88 | 60 | `registry/morpho/calldata-gauntlet-gtUSDCc-999.json` | redeem never names USDC as the asset the receiver gets. |
| D | 88 | 68 | `registry/morpho/calldata-gauntlet-gtUSDCcore.json` | redeem: the screen never names USDC as the asset paid out; mint already shows it as a constant. |
| D | 88 | 55 | `registry/morpho/calldata-gauntlet-gtWBTCc.json` | redeem: the asset received (WBTC) is never named on the screen |
| D | 88 | 58 | `registry/morpho/calldata-gauntlet-gtWETHe.json` | redeem never names WETH as the asset the receiver gets, unlike deposit and mint. |
| D | 88 | 63 | `registry/morpho/calldata-gauntlet-gtcbBTCc-8453.json` | redeem never names cbBTC as the asset the receiver gets; the mint format shows it with a constant. |
| D | 88 | 57 | `registry/morpho/calldata-gauntlet-gteUSDc.json` | redeem: the screen never names eUSD as the asset received, although mint shows it as a constant. |
| D | 88 | 68 | `registry/morpho/calldata-gauntlet-gteurcb-v2-8453.json` | redeem: the screen never names EURC as the asset received; the mint format shows it as a constant. |
| D | 88 | 73 | `registry/morpho/calldata-gauntlet-gteurcc-v2-1.json` | redeem: the screen never says the signer receives EURC; only the shares are named. |
| D | 88 | 60 | `registry/morpho/calldata-gauntlet-gtmsETHc-8453.json` | redeem: the screen never names msETH, the asset the signer receives. |
| D | 88 | 69 | `registry/morpho/calldata-gauntlet-gtusdcb-v2-42161.json` | redeem: the screen never names USDC as the asset the receiver gets. |
| D | 88 | 67 | `registry/morpho/calldata-gauntlet-gtusdcp-v2-1.json` | redeem: the screen never names USDC as the asset received, though a constant field could. |
| D | 88 | 67 | `registry/morpho/calldata-gauntlet-gtusdcp-v2-42161.json` | redeem never names USDC as the asset the receiver gets back. |
| D | 88 | 66 | `registry/morpho/calldata-gauntlet-gtusdgp-v2-42161.json` | withdraw: the screen never names the gtusdgp shares burned from the owner. |
| D | 88 | 66 | `registry/morpho/calldata-gauntlet-gtusdtf-v2-1.json` | redeem: the screen never names USDT as the asset the receiver gets. |
| D | 88 | 68 | `registry/morpho/calldata-gauntlet-gtusdtp-v2-1.json` | redeem: nothing on screen names USDT as the asset the receiver gets. |
| D | 88 | 66 | `registry/morpho/calldata-gauntlet-gtwethb-v2-1.json` | redeem: the screen never says that WETH is the asset the receiver gets. |
| D | 88 | 58 | `registry/morpho/calldata-gauntlet-midasUSDC.json` | redeem never names USDC as the asset that the receiver gets. |
| D | 88 | 67 | `registry/morpho/calldata-gauntlet-vbgtWBTC.json` | redeem: the screen never names WBTC as the asset the receiver gets. |
| D | 88 | 65 | `registry/morpho/calldata-hakutora-hUSDC.json` | redeem: the screen never says that USDC is the asset paid out, though the mint format shows it. |
| D | 88 | 64 | `registry/morpho/calldata-hakutora-hUSDT.json` | redeem never names USDT as the asset the receiver gets, though the descriptor has the constant. |
| D | 88 | 67 | `registry/morpho/calldata-hyperithm-ApyxUSDC-v2-1.json` | redeem: the screen never says USDC is what the receiver gets. |
| D | 88 | 69 | `registry/morpho/calldata-hyperithm-ApyxapxUSD-v2-1.json` | redeem: the screen never says apxUSD is what the receiver gets back. |
| D | 88 | 69 | `registry/morpho/calldata-hyperithm-hyperUSDCa-v2-1.json` | redeem does not name USDC as the asset the receiver gets, unlike the mint format. |
| D | 88 | 71 | `registry/morpho/calldata-hyperithm-hyperUSDCa-v2-143.json` | redeem: the screen never names USDC as the asset paid to the receiver. |
| D | 88 | 66 | `registry/morpho/calldata-hyperithm-satUSDC-v2-1.json` | redeem: the screen never says the payout is USDC, though the token is fixed and known. |
| D | 88 | 67 | `registry/morpho/calldata-hyperithm-satUSDC-v2-143.json` | redeem never names USDC as the asset the receiver gets, though the descriptor has it as a constant. |
| D | 88 | 66 | `registry/morpho/calldata-keyrock-kUSDC-v2-1.json` | redeem: the screen never says USDC is received. The mint format names the underlying, redeem does not. |
| D | 88 | 72 | `registry/morpho/calldata-kpk-KPK_USDC_Yield-v2-1.json` | redeem: the screen never names USDC as the asset paid out to the receiver. |
| D | 88 | 57 | `registry/morpho/calldata-leadblock-USDC-RWA.json` | redeem never names USDC as the asset the receiver gets back. |
| D | 88 | 59 | `registry/morpho/calldata-mev_capital-MC_USD0.json` | redeem never names USD0 as the asset the receiver gets; only the shares appear. |
| D | 88 | 58 | `registry/morpho/calldata-mev_capital-MCcbBTC.json` | redeem: the asset received (cbBTC) is never named, though the descriptor has it as a constant. |
| D | 88 | 66 | `registry/morpho/calldata-mev_capital-MCwBTC.json` | redeem never names WBTC as the asset the receiver gets |
| D | 88 | 61 | `registry/morpho/calldata-mev_capital-MCwETH.json` | redeem never says the receiver gets WETH. The asset is a known constant, but no field shows it. |
| D | 88 | 57 | `registry/morpho/calldata-mev_capital-USUALUSDC+.json` | redeem does not name USDC as the asset the receiver gets, though mint shows it as a constant. |
| D | 88 | 53 | `registry/morpho/calldata-mev_capital-sgfEURCV.json` | redeem: the screen never names EURCV as the asset the receiver gets. |
| D | 88 | 62 | `registry/morpho/calldata-re7_labs-Re7FRAX.json` | redeem: the screen never names FRAX as the asset received, though it is a fixed constant. |
| D | 88 | 70 | `registry/morpho/calldata-re7_labs-fxUSDC.json` | redeem: the screen never says that USDC is what the recipient receives. |
| D | 88 | 65 | `registry/morpho/calldata-rockawayx-roxUSDCy-v2-1.json` | redeem never names USDC as the asset the receiver gets. A constant field could show it. |
| D | 88 | 66 | `registry/morpho/calldata-rockawayx-roxWETH-v2-1.json` | redeem: the screen never names WETH as the asset the receiver gets. |
| D | 88 | 68 | `registry/morpho/calldata-rockawayx-roxpUSDC-v2-1.json` | redeem never names USDC as the asset the receiver gets; the sibling mint format shows it. |
| D | 88 | 67 | `registry/morpho/calldata-sentora-senPYUSDPST-v2-1.json` | redeem: the screen never says PYUSD is received, though the descriptor has the underlying ticker constant. |
| D | 88 | 65 | `registry/morpho/calldata-sentora-senPYUSDmWIN-v2-1.json` | redeem never names PYUSD as the asset the receiver gets |
| D | 88 | 68 | `registry/morpho/calldata-sentora-senRLUSDv2-v2-1.json` | redeem never names RLUSD as the asset the receiver gets; the reader had to guess it. |
| D | 88 | 66 | `registry/morpho/calldata-singularv-svETH-v2-1.json` | redeem: no field or sentence names WETH as the asset the receiver gets. |
| D | 88 | 61 | `registry/morpho/calldata-singularv-svETH.json` | redeem does not name WETH as the asset received, so the reader guessed ETH or WETH. |
| D | 88 | 68 | `registry/morpho/calldata-steakhouse_financial-3F-steakUSDC-v2-1.json` | redeem: the asset paid out (USDC) is never named, although the deposit and mint screens name it with a constant. |
| D | 88 | 63 | `registry/morpho/calldata-steakhouse_financial-bbqDAI.json` | redeem never names DAI as the asset the receiver gets, though a constant for it exists. |
| D | 88 | 68 | `registry/morpho/calldata-steakhouse_financial-bbqUSD1-v2-143.json` | redeem: the screen never names USD1 as the asset received, although the descriptor has it as a constant. |
| D | 88 | 61 | `registry/morpho/calldata-steakhouse_financial-bbqUSDC-42161.json` | redeem never names USDC as the asset the receiver gets. |
| D | 88 | 61 | `registry/morpho/calldata-steakhouse_financial-bbqUSDC-8453.json` | redeem never names USDC as the asset the receiver gets; mint shows the underlying ticker, but redeem does not. |
| D | 88 | 68 | `registry/morpho/calldata-steakhouse_financial-bbqUSDC-v2-1.json` | redeem: the screen never says USDC is received; other formats show it as a constant, this one does not. |
| D | 88 | 66 | `registry/morpho/calldata-steakhouse_financial-bbqUSDC.json` | redeem: the screen never names USDC as the asset received; the reader had to guess it. |
| D | 88 | 65 | `registry/morpho/calldata-steakhouse_financial-bbqUSDG-v2-42161.json` | redeem never names USDG as the asset the receiver gets. |
| D | 88 | 69 | `registry/morpho/calldata-steakhouse_financial-bbqUSDT-v2-1.json` | redeem: the screen never names USDT as the asset the receiver gets |
| D | 88 | 63 | `registry/morpho/calldata-steakhouse_financial-bbqUSDT.json` | redeem does not name USDT as the asset the receiver gets; mint shows the same constant. |
| D | 88 | 58 | `registry/morpho/calldata-steakhouse_financial-bbqUSDT0.json` | redeem: the screen never names USDT0 as the asset the receiver gets. |
| D | 88 | 61 | `registry/morpho/calldata-steakhouse_financial-csUSDC.json` | redeem does not name USDC as the asset the receiver gets; mint shows it as a constant. |
| D | 88 | 60 | `registry/morpho/calldata-steakhouse_financial-csUSDL.json` | redeem never names wUSDL as the token the receiver gets, though mint shows the underlying ticker. |
| D | 88 | 70 | `registry/morpho/calldata-steakhouse_financial-grove-bbqAUSD-v2-1.json` | redeem: the screen never names AUSD as the asset received, so the reader only guessed it. |
| D | 88 | 68 | `registry/morpho/calldata-steakhouse_financial-grove-bbqUSDC-v2-1.json` | redeem: the screen never names USDC as the asset the receiver gets. |
| D | 88 | 61 | `registry/morpho/calldata-steakhouse_financial-steakETH-1.json` | The redeem screen never says that the receiver gets WETH. The mint format names WETH, but redeem does not. |
| D | 88 | 68 | `registry/morpho/calldata-steakhouse_financial-steakEURC-v2-1.json` | redeem: the screen never names EURC as the asset the receiver gets. |
| D | 88 | 68 | `registry/morpho/calldata-steakhouse_financial-steakEURC-v2-8453.json` | redeem: the screen never names EURC as the asset the receiver gets |
| D | 88 | 73 | `registry/morpho/calldata-steakhouse_financial-steakEURCV-v2-1.json` | redeem: the screen never says that EURCV is the asset paid out to the receiver. |
| D | 88 | 59 | `registry/morpho/calldata-steakhouse_financial-steakPYUSD.json` | redeem: the screen never names PYUSD as the token received, though mint shows it as a constant. |
| D | 88 | 55 | `registry/morpho/calldata-steakhouse_financial-steakRUSD.json` | redeem never names rUSD as the asset received. The mint format shows that constant. |
| D | 88 | 60 | `registry/morpho/calldata-steakhouse_financial-steakUSDC-8453.json` | redeem never names USDC as the asset the receiver gets, though mint shows it as a constant. |
| D | 88 | 68 | `registry/morpho/calldata-steakhouse_financial-steakUSDC-v2-1.json` | redeem: the screen never says that USDC is the asset paid out. |
| D | 88 | 69 | `registry/morpho/calldata-steakhouse_financial-steakUSDT-v2-1.json` | redeem: the payout asset (USDT) is never named, so the signer must guess what arrives. |
| D | 88 | 64 | `registry/morpho/calldata-steakhouse_financial-steakUSDT.json` | redeem does not name USDT as the asset the recipient receives, though it is a fixed constant. |
| D | 88 | 66 | `registry/morpho/calldata-steakhouse_financial-steakXSGD-v2-8453.json` | redeem: the screen never says XSGD is received; the signer only sees shares and a recipient. |
| D | 88 | 59 | `registry/morpho/calldata-steakhouse_financial-vbshUSDC.json` | redeem never names USDC as the asset the receiver gets, though the descriptor has it as a constant. |
| D | 88 | 62 | `registry/morpho/calldata-ultrayield-edgeUSDC.json` | redeem never names USDC as the asset the receiver gets back. |
| D | 88 | 73 | `registry/morpho/calldata-unified_labs-urRWA-v2-143.json` | redeem: the asset received (USDC) is never named on the screen. |
| D | 88 | 70 | `registry/morpho/calldata-yearn-yOG-USDC-V2-v2-1.json` | redeem: the screen never names USDC as the asset received, though a constant field could. |
| D | 88 | 68 | `registry/morpho/calldata-yearn-yOG-USDC-V2-v2-8453.json` | redeem: the asset received (USDC) is never named, although the descriptor has it as a constant. |
| D | 88 | 56 | `registry/morpho/calldata-yearn-ymvOG-USDC.json` | redeem: the screen never names USDC as the asset that arrives, though sibling formats show it. |
| B | 90 | 72 | `registry/1inch/calldata-NativeOrderFactory.json` | create: order expiry in makerTraits is hidden, and resolvers may cut a reward after expiry |
| C | 90 | 40 | `registry/flyingtulip/eip712-PftMarketplace-BuyOffer.json` | BuyOffer: the taker fee on top of the offer price is not shown or mentioned. |
| C | 90 | 45 | `registry/hyperliquid/eip712-withdraw.json` | Withdraw: the 1 USDC withdrawal fee is not mentioned, so the recipient may get less than 'USDC amount'. |
| C | 90 | 56 | `registry/kiln/calldata-kiln-batch-deposit-v2.json` | bigBatchDeposit: 0x00 credentials would show part of a hash as a withdrawal address. |
| B | 90 | 78 | `registry/p2p/calldata-P2pOrgUnlimitedEthDepositor.json` | addEth hides the referrer share and recipient that the new fee distributor writes into the reward split. |
| B | 90 | 79 | `registry/p2p/calldata-P2pSsvProxyFactory.json` | addEth hides the referrer basis points and recipient, a party that gets part of the rewards. |
| C | 90 | 48 | `registry/paraswap/calldata-AugustusSwapper-v5.json` | simpleBuy hides data.partner and data.feePercent, which set the fee taken in the trade. |
| C | 90 | 18 | `registry/paraswap/eip712-paraswap.json` | Order hides expiry 0, so the signer is not told that the order never expires. |
| A | 90 | 82 | `registry/permit/eip712-permit-arbitrum-bridged-usdc.json` | Permit format has no test case, so neither the normal rendering nor the "Unlimited" threshold is tested. |
| A | 90 | 80 | `registry/permit/eip712-permit-arbitrum-dai.json` | Permit has no test case, so no test covers the rendering of the amount, the Unlimited threshold or the deadline. |
| A | 90 | 80 | `registry/permit/eip712-permit-arbitrum-usdc.json` | Permit test covers only a 250 USDC amount, never the "Unlimited" threshold or a no-expiry deadline. |
| B | 90 | 63 | `registry/permit/eip712-permit-arbitrum-wsteth.json` | Permit metadata.owner names Lido's wstETH, but the contract is Axelar Wrapped wstETH (axl-wstETH). |
| B | 90 | 76 | `registry/permit/eip712-permit-base-aero.json` | Permit has no test case, so no rendering of the amount, the Unlimited message or the date is checked. |
| B | 90 | 73 | `registry/permit/eip712-permit-bsc-polkastarter-token.json` | Permit has no test case, so no rendering of the amount, token or Unlimited message is checked. |
| C | 90 | 35 | `registry/permit/eip712-permit-ethereum-dai.json` | DAI Permit hides the expiry field when expiry is 0, so a permit that never expires shows no validity limit. |
| B | 90 | 76 | `registry/permit/eip712-permit-ethereum-lido-steth.json` | The stETH Permit format has no test case, so no rendering of the amount or the Unlimited message is checked. |
| A | 90 | 84 | `registry/permit/eip712-permit-linea-lusd.json` | Permit has no test case, so no rendering of the amount, threshold or date is checked. |
| B | 90 | 75 | `registry/permit/eip712-permit-linea-usdc.json` | Permit has no test case, so no rendering of the amount, the Unlimited threshold or the date is checked. |
| A | 90 | 80 | `registry/permit/eip712-permit-linea-wbtc.json` | The Permit primary type has no test case, so no rendering of the WBTC amount, the Unlimited message or the date is checked. |
| B | 90 | 79 | `registry/permit/eip712-permit-linea-wsteth.json` | Permit has no test case, so the wstETH amount and the Unlimited threshold are never exercised. |
| B | 90 | 78 | `registry/permit/eip712-permit-optimism-usdc.json` | Permit has one test, a 250 USDC amount, so the "Unlimited" threshold path is never tested. |
| B | 90 | 79 | `registry/permit/eip712-permit-optimism-wsteth.json` | Permit: metadata.owner names Lido's wstETH, but the contract is Axelar's bridged wrapper token. |
| A | 90 | 80 | `registry/permit/eip712-permit-polygon-quick.json` | Permit test only covers a finite amount; the 'Unlimited' threshold path for uint(-1) is never tested. |
| C | 90 | 58 | `registry/poap/calldata-PoapBridge.json` | mintToken: eventId, which tells which event's POAP is minted, is hidden with visible: never. |
| C | 90 | 15 | `registry/porto/eip712-Orchestrator-0.5.5.json` | Intent tests never decode a real nested call, a self-call, or a multichain intent. |
| C | 90 | 36 | `registry/rarible/eip712-rarible-erc-721.json` | Mint721 has no test case, so the rendering of the creators and royalties arrays is never exercised. |
| B | 90 | 69 | `registry/safe/calldata-SafeProxyFactory-1.5.0.json` | createProxyWithNonce: nested setup screen shows the setup data but not the delegatecall target `to`. |
| B | 90 | 60 | `registry/tally/eip712-tally-arbitrum-arb-token.json` | Delegation has no test case, including the zero-address undelegate path. |
| C | 90 | 57 | `registry/teraswap/calldata-TeraSwapFeeCollector.json` | swapTokenWithFee: the fixed 0.1% TeraSwap fee taken from Amount In appears nowhere on the screen. |
| C | 90 | 58 | `registry/tesseract/calldata-vault-deployer-WETH.json` | deployVaultWithPermit grants the signer WHITELIST_ROLE on the new vault, and the screen does not say so. |
| B | 90 | 60 | `registry/tether/eip712-CancelAuthorization-usdt0-Flare.json` | CancelAuthorization has no test case, so no rendering of this primary type is checked. |
| C | 90 | 30 | `registry/uniswap/eip712-UniswapX-ExclusiveDutchOrder.json` | 'Spend max' shows inputStartAmount, but input can rise to the hidden inputEndAmount. |
| C | 90 | 47 | `registry/uniswap/eip712-UniswapX-LimitOrder.json` | LimitOrder test messages are signatures UniswapX would reject: their nonce, deadline and spender differ from the order. |
| C | 90 | 30 | `registry/uniswap/eip712-uniswap-V2DutchOrder.json` | V2DutchOrder 'Spend max' shows baseInputStartAmount, but the input can rise to baseInputEndAmount |
| C | 90 | 53 | `registry/zama/eip712-UserDecryptRequestVerificationV2.json` | UserDecryptRequestVerification hides publicKey, which decides who can read the decrypted data. |
| C | 90 | 52 | `registry/zkstables/calldata-ebswap.json` | atomicPublicSwap hides encryptedFlags, which change the encrypted payer's pending-balance setting after the transfer. |
| B | 90 | 65 | `registry/zkstables/eip712-executor.json` | Exec has one test only, with empty data, so the embedded calldata Action field is never decoded. |
| C | 92 | 50 | `registry/10102/calldata-TimeLockRouter.json` | createTimelock hides the swap minimum when it is 0, so a swap with no slippage bound shows no minimum |
| D | 92 | 48 | `registry/benqi/calldata-sAVAX.json` | submit(): the intent never says the signer receives sAVAX in return for the AVAX. |
| C | 92 | 39 | `registry/flare/calldata-AssetManager-FXRP-Songbird.json` | executeDirectMinting: the FXRP recipient is not shown; the memo data that can encode it is hidden. |
| C | 92 | 49 | `registry/flare/calldata-RewardManager-Flare.json` | claim: a Provider-fee proof can be partly burned, so the recipient may get less than 'Proof amount'. |
| F | 93 | 78 | `registry/feral-file/calldata-feralfile-exhibition-v4-0.json` | buyArtworks is payable with no @.value field; in the vault path the ETH sent is unchecked. |
| B | 93 | 75 | `registry/flyingtulip/calldata-EpochRewardsVault.json` | withdraw: the ftUSD token constant is hardcoded from mainnet and reused for the chain 146 deployment. |
| F | 94 | 82 | `registry/feral-file/calldata-feralfile-exhibition-v4_1-0.json` | buyArtworks is payable, has no @.value field, and on the vault path nothing ties the sent ETH to Price. |
| F | 94 | 75 | `registry/feral-file/calldata-feralfile-exhibition-v4_2-0.json` | buyBulkArtworks is payable with no @.value field; in vault mode the ETH sent is unchecked and unshown. |
| F | 94 | 71 | `registry/feral-file/calldata-feralfile-exhibition-v4_3-0.json` | buyArtworks is payable with no @.value field; on the vault path msg.value is unchecked and lost. |
| F | 94 | 81 | `registry/feral-file/calldata-feralfile-exhibition-v4_4-0.json` | buyArtworks has no @.value field, and in vault mode nothing ties the ETH sent to the Price shown. |
| F | 94 | 72 | `registry/feral-file/calldata-feralfile-exhibition-v4_5-0.json` | buyArtworks: payable with no @.value field; when paying through the vault, the ETH sent is unchecked and never shown. |
| F | 94 | 59 | `registry/lifi/calldata-LIFIDiamond.json` | Symbiosis: the calldata that decides recipient, chain and output is not on the screen at all |
| C | 95 | 48 | `registry/feral-file/calldata-feralfile-vault-0.json` | payForSale resolves artwork names against the vault (@.to), not the FFV4 artwork contract. |
| B | 95 | 65 | `registry/flyingtulip/calldata-MintAndRedeem-dev-avalanche.json` | redeem collateral may be queued by the yield wrapper rather than delivered now, and the screen does not say so. |
| B | 95 | 75 | `registry/flyingtulip/calldata-MintAndRedeem-dev.json` | redeem interpolatedIntent 'Sell {ftUSDAmount}' omits the collateral asset and its minimum. |
| C | 95 | 48 | `registry/gondi/calldata-AuctionLoanLiquidator-v3_1.json` | settleAuction: the trigger fee paid to the caller and the originator is hidden, and it is cut from the lenders' proceeds. |
| B | 95 | 76 | `registry/gondi/calldata-AuctionLoanLiquidator-v3_2.json` | settleAuction: the settler's trigger-fee reward is paid to the signer but its rate is hidden. |
| C | 95 | 50 | `registry/kiln/calldata-Vault-USDC-AAVE-Arbitrum.json` | mint intent 'Mint' does not say that USDC is pulled from the signer for vault shares. |
| C | 95 | 65 | `registry/lido/calldata-WithdrawalQueueERC721.json` | requestWithdrawalsWithPermit hides the permit value, the stETH allowance the call sets for the queue. |
| C | 95 | 50 | `registry/morpho/calldata-MidnightBundlesV2.json` | CancelAndMake interpolated intent says 'Authorize ratifier' even when newRoot is zero and nothing is authorized. |
| C | 95 | 53 | `registry/threshold/calldata-L2WormholeGateway.json` | sendTbtc chain enum lacks testnet and Solana Wormhole chain ids used by listed deployments |
| B | 96 | 76 | `registry/avvatar-labs-alia/calldata-AgentIdentityRegistry-base.json` | recordDecision intent leaves out the reputation change and the possible automatic suspension of the agent. |
| C | 97 | 76 | `registry/aave/calldata-lpv3.json` | repayWithPermit: the permit's allowance to the Pool is never stated, and with "All" it stays effectively unlimited. |
| B | 97 | 79 | `registry/corestake/calldata-coreagent.json` | undelegateCoin's label says 0 unstakes everything, but a direct call with 0 reverts. |
| C | 97 | 67 | `registry/corestake/calldata-corestake.json` | redeem: the intent "Request Redeem" does not say stCORE is burned and CORE comes only after a lock |
| C | 97 | 74 | `registry/feral-file/calldata-feralfile-exhibition-v3_3-0.json` | createArtworks hides AEAmount and PPAmount, so the mintable supply looks smaller than it is. |
| C | 97 | 30 | `registry/flare/calldata-DistributionToDelegators-Flare.json` | autoClaim does not say that it deducts an executor fee per owner and pays it to the caller. |
| B | 97 | 77 | `registry/morpho/calldata-clearstar-CSAAUSD-v2-143.json` |  |
| B | 97 | 79 | `registry/morpho/calldata-hyperithm-hyperUSDTc-v2-988.json` | redeem never names USDT0 as the asset the receiver gets; only the burned shares appear. |
| B | 98 | 80 | `registry/aave/calldata-WrappedTokenGatewayV3.json` | depositETH has no interpolatedIntent, so the intent line 'Supply' names neither the amount nor who gets the position. |
| B | 98 | 79 | `registry/avvatar-labs-alia/calldata-AssetIdentityRegistry-base.json` | addCrossChainRecord resolves the cross-chain token's name on Base, though the token lives on _chainId. |
| C | 98 | 62 | `registry/celo/calldata-locked_celo.json` | delegateGovernanceVotes: 'Fraction to Delegate' reads as an added share, but the code sets a new total for the delegatee. |
| C | 98 | 63 | `registry/feral-file/calldata-feralfile-english-auction-0.json` | registerAuctions: the bid-increment, extension rules and isSettled flag of each auction are not shown. |
| C | 98 | 75 | `registry/feral-file/calldata-feralfile-exhibition-v3-0.json` | setApprovalForAll: the raw boolean makes the sentence read 'true all tokens for X', so grant or revoke is unclear. |
| C | 98 | 73 | `registry/feral-file/calldata-feralfile-exhibition-v3_2-0.json` | createArtworks hides AEAmount and PPAmount, which raise the mint cap above the edition size shown. |
| C | 98 | 36 | `registry/gondi/calldata-PurchaseBundler-v3_1-robinhood.json` | executeSell: native value above the payment can go to the seller, not back to the signer. |
| C | 98 | 53 | `registry/kiln/calldata-Vault-USDC-Morpho-Gauntlet-Core-Base.json` | redeem does not name USDC as the asset the receiver gets; nothing on the screen states it. |
| C | 98 | 50 | `registry/kiln/calldata-Vault-USDC-Morpho-Gauntlet-USDC-Core-multisig.json` | redeem: the asset the receiver gets (USDC) is named nowhere on the screen. |
| C | 98 | 51 | `registry/kiln/calldata-Vault-USDC-Morpho-MEV-Capital.json` | redeem never names USDC as the asset the receiver gets; only the shares burned are shown. |
| C | 98 | 59 | `registry/kiln/calldata-Vault-USDC-Morpho-Re7-Base.json` | redeem never names USDC as the asset the recipient receives. |
| C | 98 | 52 | `registry/kiln/calldata-Vault-USDC-Morpho-Steakhouse-USDC-multisig.json` | redeem: the screen never names USDC as the asset the receiver gets. |
| C | 98 | 56 | `registry/kiln/calldata-Vault-USDT-Aave-v3.json` | redeem: the screen never names USDT as the asset that arrives. |
| C | 98 | 51 | `registry/kiln/calldata-Vault-USDT-Compound-v3.json` | redeem never names USDT as the asset the receiver gets |
| C | 98 | 52 | `registry/kiln/calldata-Vault-USDT-Morpho-Gauntlet-USDT-Prime.json` | redeem: the screen never names USDT as the asset received; mint shows it with a constant. |
| C | 98 | 57 | `registry/kiln/calldata-Vault-WETH-Aave-v3.json` | redeem: the WETH paid out is not named anywhere on screen |
| C | 98 | 50 | `registry/kiln/calldata-Vault-WETH-Morpho-MEV-Capital.json` | redeem never names WETH as the asset the receiver gets |
| C | 98 | 62 | `registry/morpho/calldata-9summits-9SETHc.json` | redeem never names WETH as the asset the receiver gets; only shares and addresses are shown. |
| C | 98 | 51 | `registry/morpho/calldata-9summits-9SUSDCcore.json` | redeem never names USDC as the asset the receiver gets for the burned shares. |
| C | 98 | 58 | `registry/morpho/calldata-apostro-aprUSDC.json` | redeem never names USDC as the asset the receiver gets. |
| C | 98 | 58 | `registry/morpho/calldata-b_protocol-reETH.json` | redeem never names WETH as the asset the receiver gets, though mint and deposit show it. |
| C | 98 | 56 | `registry/morpho/calldata-b_protocol-recbBTC.json` | redeem: the screen never says that cbBTC is the asset sent to the receiver. |
| C | 98 | 54 | `registry/morpho/calldata-block_analitica-mwETH.json` | redeem never shows that the receiver gets WETH; only the shares going out are shown. |
| C | 98 | 58 | `registry/morpho/calldata-fence-ERY.json` | redeem never names EURe as the asset that the receiver gets. |
| C | 98 | 60 | `registry/morpho/calldata-gauntlet-gtDAIcore.json` | redeem never names DAI as the asset the receiver gets, unlike the mint format. |
| C | 98 | 66 | `registry/morpho/calldata-gauntlet-gtEURCc.json` | redeem never names EURC as the asset the receiver gets; only the shares are shown. |
| C | 98 | 58 | `registry/morpho/calldata-gauntlet-gtUSDC-747474.json` | redeem never names vbUSDC as the asset sent to the receiver, unlike the mint format. |
| C | 98 | 54 | `registry/morpho/calldata-gauntlet-gtUSDCp.json` | redeem never names USDC as the asset the receiver gets back; only shares and addresses are shown. |
| C | 98 | 55 | `registry/morpho/calldata-gauntlet-gtUSDT-747474.json` | redeem does not name the asset that the receiver gets; nothing on screen says vbUSDT. |
| C | 98 | 61 | `registry/morpho/calldata-gauntlet-gtWETH-747474.json` | redeem: no field names vbETH as the asset the receiver gets; mint has a constant ticker field for it. |
| C | 98 | 60 | `registry/morpho/calldata-gauntlet-gtmsUSDc.json` | redeem: the asset paid out (msUSD) is not named, though a constant could show it. |
| C | 98 | 55 | `registry/morpho/calldata-gauntlet-msolvbtcbbn.json` | redeem: no field names xSolvBTC as the asset the receiver gets back. |
| C | 98 | 56 | `registry/morpho/calldata-gauntlet-sbMorphoUSDC.json` | redeem never says the receiver gets USDC: the screen names only the shares |
| C | 98 | 54 | `registry/morpho/calldata-gauntlet-smWETH.json` | redeem never names WETH as the asset the receiver gets. |
| C | 98 | 64 | `registry/morpho/calldata-llamarisk-llama-crvUSD.json` | redeem: the screen never names crvUSD as the asset the receiver gets. |
| C | 98 | 59 | `registry/morpho/calldata-mev_capital-MC.eUSDC.json` | redeem never names USDC as the asset the receiver gets, unlike the mint format, which shows the ticker. |
| C | 98 | 54 | `registry/morpho/calldata-re7_labs-Re7WETH.json` | redeem: the screen never says that WETH is what the receiver gets. |
| C | 98 | 54 | `registry/morpho/calldata-re7_labs-degenUSDC.json` | redeem never names USDC as the asset the receiver gets. |
| C | 98 | 50 | `registry/morpho/calldata-re7_labs-mDEGEN.json` | redeem does not name DEGEN as the asset the receiver gets; mint shows the ticker but redeem does not. |
| C | 98 | 62 | `registry/morpho/calldata-re7_labs-mMAI.json` | redeem never names MAI as the asset the receiver gets back; mint shows that ticker. |
| C | 98 | 63 | `registry/morpho/calldata-re7_labs-uUSDC.json` | redeem: no field or intent says the recipient gets USDC. |
| C | 98 | 56 | `registry/morpho/calldata-sparkdao-spDAI.json` | redeem: the asset received (DAI) appears nowhere on the screen, though a constant is available. |
| C | 98 | 55 | `registry/morpho/calldata-sparkdao-sparkUSDC.json` | redeem shows no field or intent that names USDC as the asset the receiver gets. |
| C | 98 | 60 | `registry/morpho/calldata-steakhouse_financial-steakEURA.json` | redeem never names EURA as the asset the receiver gets; mint shows the underlying ticker, but redeem does not. |
| C | 98 | 60 | `registry/morpho/calldata-steakhouse_financial-steakEURC.json` | redeem never names EURC as the asset the receiver gets, though sibling formats show it. |
| C | 98 | 61 | `registry/morpho/calldata-steakhouse_financial-steakPAXG.json` | redeem: no field names PAXG as the asset paid out, unlike mint's 'Deposit asset' field. |
| C | 98 | 59 | `registry/morpho/calldata-steakhouse_financial-steakUSDTlite.json` | redeem: the asset received (USDT) is not named anywhere on the screen. |
| C | 98 | 71 | `registry/morpho/calldata-yearn-ymvOG-vbUSDT.json` | The mint intent "Mint" does not say that the signer pays vbUSDT to get the shares. |
| B | 98 | 69 | `registry/ondo-finance/calldata-GMTokenLimitOrder.json` | createSellOrderExactIn: case 3 targets the BSC deployment and BSC USDT with chainId 1, so it never resolves. |
| C | 98 | 66 | `registry/serenita/calldata-EthVault.json` | multicall: inner calls to signer functions with no format here (mintOsToken, burnOsToken, redeemOsToken) cannot render. |
| B | 98 | 75 | `registry/threshold/calldata-RebateStaking.json` |  |
| C | 98 | 65 | `registry/zkstables/calldata-zkemt.json` | encryptedToPublicTransferWithAuth hides the pending-balance flags it applies to the sender EPK. |
| C | 98 | 60 | `registry/zkstables/eip712-zkemt.json` | AutoEncryptAuth intent hides that future incoming tokens go to the ZK address, and that this address can never be changed. |
| C | 99 | 61 | `registry/cofund/eip712-cofund-treasury.json` | TransferPolicyActivation with no recipients shows nothing, though an empty list allows any recipient. |
| C | 99 | 82 | `registry/feral-file/calldata-feralfile-exhibition-v2-0.json` | setApprovalForAll tests only grant (true); the revoke path (false) is not tested. |
| C | 99 | 69 | `registry/lombard/calldata-lbtc-mainnet.json` | mint shows the minted amount and recipient only inside raw payload hex, not as readable fields. |
| C | 99 | 62 | `registry/lombard/calldata-lbtc-sepolia.json` | redeem shows only the LBTC that leaves; it never says what the signer gets back or that a fee applies. |
| B | 99 | 75 | `registry/symbiotic/calldata-UniversalDelegator-USDC.json` | addAdapter also grants the Allocate and Deallocate roles to the adapter, and the screen does not say so. |
| C | 100 | 62 | `registry/10102/calldata-ShieldVault.json` | open shows vetoIndex raw, so 'no recovery' renders as a 78-digit number |
| C | 100 | 74 | `registry/10102/calldata-TransferEOALegacyRouter.json` |  |
| B | 100 | 85 | `registry/avvatar-labs-alia/calldata-ScoreEngineV2-base.json` | refreshScoreBatch: the asset list uses address types eoa/wallet, but the entries are collateral token contracts. |
| C | 100 | 46 | `registry/bedrock/calldata-selini-airdrop.json` | claim: interpolatedIntent 'Claim 225' reads as 225 whole tokens, but it is 225 base units |
| C | 100 | 73 | `registry/bedrock/calldata-selini-delayRedeemRouter.json` |  |
| A | 100 | 98 | `registry/bedrock/calldata-uniBTC.json` |  |
| A | 100 | 85 | `registry/bedrock/calldata-vault.json` |  |
| B | 100 | 78 | `registry/bedrock/calldata-vaultWithoutNative.json` |  |
| A | 100 | 92 | `registry/bureaucrawl/calldata-BureaucrawlRuns.json` |  |
| C | 100 | 55 | `registry/celo/calldata-celo_accounts.json` | authorizeAttestationSigner intent 'Authorize Signer' does not say the role is attestation. |
| C | 100 | 42 | `registry/celo/calldata-celo_election.json` | activate intent "Activate" does not say that pending votes for the group become active. |
| C | 100 | 71 | `registry/celo/calldata-celo_governance.json` | executeHotfix: 'CELO to Send' implies the signer pays; the Governance contract sends this CELO. |
| C | 100 | 61 | `registry/celo/calldata-celo_validators.json` | addFirstMember uses the same intent as addMember and does not say the group becomes eligible for election. |
| C | 100 | 51 | `registry/circle/calldata-TokenMessengerV2.json` | depositForBurn: destination domain shown as a bare CCTP number (0, 3, 6) instead of a chain name. |
| A | 100 | 85 | `registry/circle/eip712-ReceiveWithAuthorization.json` |  |
| A | 100 | 85 | `registry/circle/eip712-TransferWithAuthorization.json` |  |
| A | 100 | 92 | `registry/consensus-specs/calldata-DepositContract.json` |  |
| A | 100 | 80 | `registry/corestake/calldata-stakehub.json` |  |
| B | 100 | 85 | `registry/cosmix/calldata-PredictionMarket.json` |  |
| C | 100 | 30 | `registry/degate/eip712-degate.json` | AccountUpdate shows maxFee as a raw base-unit integer with no token decimals. |
| B | 100 | 71 | `registry/enso/calldata-EnsoRouter.json` | safeRouteSingle intent says 'Route tokens' and the sentence has no verb for receiving the output token. |
| C | 100 | 42 | `registry/ethos/calldata-EthosVouchV2.json` | vouchWithPermit: the label 'Amount, fee added' can read as a total that already includes the fee. |
| C | 100 | 77 | `registry/feral-file/calldata-feralfile-airdrop-v1-0.json` | safeBatchTransferFrom: ids and amounts are two separate lists the signer must pair by position. |
| C | 100 | 40 | `registry/figment/calldata-PoolDynamic-MUSDC-sepolia.json` | deposit has no interpolatedIntent, so the sentence names neither the amount nor the token. |
| C | 100 | 54 | `registry/figment/calldata-PoolDynamic-USDC.json` | requestRedeem intent "Redeem" suggests an immediate payout, but the call only queues a request. |
| B | 100 | 72 | `registry/figment/calldata-figment-batch-deposit.json` | deposit shows withdrawal credentials as raw 32 bytes, so the signer cannot see who controls the stake. |
| C | 100 | 49 | `registry/flare/calldata-AssetManager-FXRP-Flare.json` | redemptionPaymentDefault labels the unpaid XRP as FXRP and never says the payout is in agent collateral. |
| C | 100 | 74 | `registry/flare/calldata-ClaimSetupManager-Flare.json` | revokeDelegationAt: the intent can read as stopping the delegation, but it affects only one past block's cached reads. |
| B | 100 | 71 | `registry/flare/calldata-ClaimSetupManager-Songbird.json` |  |
| B | 100 | 81 | `registry/flare/calldata-EntityManager-Flare.json` | proposeSubmitSignaturesAddress uses the abbreviation 'sig' in its intent and label. |
| B | 100 | 78 | `registry/flare/calldata-EntityManager-Songbird.json` | proposeSubmitSignaturesAddress uses the abbreviation 'sig' in its intent and label. |
| A | 100 | 96 | `registry/flare/calldata-FAsset-FXRP-Songbird.json` |  |
| B | 100 | 82 | `registry/flare/calldata-FXRP.json` |  |
| B | 100 | 80 | `registry/flare/calldata-GovernanceVotePower-Flare.json` | delegate: zero _to means revoke, but the screen says 'Delegate all vote power to 0x000…'. |
| A | 100 | 85 | `registry/flare/calldata-GovernanceVotePower-Songbird.json` | delegate: _to = zero address reads 'Delegate all vote power to 0x000…0', but it actually undelegates. |
| C | 100 | 70 | `registry/flare/calldata-MintingTagManager-FXRP-Flare.json` | setMintingRecipient: the intent does not say that future FXRP mints for this tag go to this address. |
| B | 100 | 76 | `registry/flare/calldata-MintingTagManager-FXRP-Songbird.json` | setMintingRecipient: recipient address types eoa/wallet are narrower than the code allows. |
| C | 100 | 68 | `registry/flare/calldata-PollingFoundation-Flare.json` | propose: the label 'Accept if vote passes' with a raw true/false hides what a reject-type proposal means. |
| C | 100 | 61 | `registry/flare/calldata-PollingFoundation-Songbird.json` | propose (executable): the proposal's action calldata is shown as raw hex |
| B | 100 | 83 | `registry/flare/calldata-PollingManagementGroup-Flare.json` | proposeWithSettings: the label 'Accept if vote passes' plus a raw true/false misstates what the accept flag does. |
| B | 100 | 78 | `registry/flare/calldata-PollingManagementGroup-Songbird.json` | proposeWithSettings: the 'Accept if vote passes' label gets the accept flag's meaning wrong; false means the proposal passes unless rejected. |
| B | 100 | 70 | `registry/flare/calldata-RNat-Flare.json` |  |
| C | 100 | 47 | `registry/flare/calldata-ValidatorRewardManager-Flare.json` | claim: when wrap is true the recipient gets WFLR, but the amount reads as native FLR. |
| B | 100 | 84 | `registry/flare/calldata-WNat-Flare.json` | withdrawFrom intent 'Unwrap WFLR' does not say it spends another owner's allowance. |
| B | 100 | 81 | `registry/flare/calldata-WNat-Songbird.json` | depositTo intent says "Wrap SGB", the same as deposit(), and does not say the WSGB goes to another address. |
| A | 100 | 84 | `registry/flare/eip712-permit-FXRP.json` |  |
| B | 100 | 70 | `registry/flyingtulip/calldata-EpochRewardsVault-dev-avalanche.json` | deposit: the sentence leaves out the receiver who gets the sftUSD staking position. |
| B | 100 | 76 | `registry/flyingtulip/calldata-EpochRewardsVault-dev-bsc.json` | withdraw interpolatedIntent omits the receiver of the ftUSD and the owner whose shares burn. |
| C | 100 | 71 | `registry/flyingtulip/calldata-EpochRewardsVault-dev.json` |  |
| B | 100 | 70 | `registry/flyingtulip/calldata-MintAndRedeem-dev-bsc.json` | mint interpolatedIntent states the minimum ftUSD as the amount bought and omits the collateral paid. |
| C | 100 | 58 | `registry/flyingtulip/calldata-MintAndRedeem.json` | redeem interpolatedIntent leaves out what the signer receives in return. |
| C | 100 | 59 | `registry/flyingtulip/calldata-PftNft.json` | setApprovalForAll: interpolatedIntent does not say whether access is granted or revoked, or that it covers all positions. |
| C | 100 | 71 | `registry/flyingtulip/calldata-PositionsManager.json` | approveBorrow: 'Borrow OK {delegate}' doesn't say the delegate can create debt in your name. |
| C | 100 | 50 | `registry/flyingtulip/calldata-PutManager-dev.json` | invest: the screen never says a pFT put-position NFT is minted to Recipient |
| C | 100 | 48 | `registry/flyingtulip/calldata-PutManager.json` | invest: interpolated intent omits the recipient of the put position and does not say a position NFT is minted. |
| C | 100 | 62 | `registry/flyingtulip/calldata-SessionManager.json` | createSession intent does not say the delegate gets power to spend the signer's tokens. |
| C | 100 | 43 | `registry/flyingtulip/eip712-SessionManager-FT.json` | Session: validUntil 0 (no expiry) and maxCalls 0 (unlimited) are shown as a 1970 date and '0'. |
| C | 100 | 22 | `registry/flyingtulip/eip712-SessionManager-ftUSD.json` | Session intent does not say the delegate can spend the owner's tokens through target contracts. |
| A | 100 | 82 | `registry/flyingtulip/eip712-SpotOrderCancel.json` |  |
| C | 100 | 62 | `registry/glue/calldata-GlueHook.json` | launchPool intent never says the signer deposits both tokens into a position owned by `owner` |
| B | 100 | 86 | `registry/gondi/calldata-UserVault.json` | depositERC1155s: the collection renders as a bare address and token ids are raw. |
| C | 100 | 40 | `registry/gondi/eip712-ExecutionData-v3_1.json` | Refinance messages still read "Borrow against" and never say the old loan is repaid from the signer's wallet. |
| C | 100 | 46 | `registry/gondi/eip712-ExecutionData-v3_2.json` | Refinance: the old loan's repayment from the borrower's wallet is not stated; only a raw loan id is shown. |
| C | 100 | 55 | `registry/gondi/eip712-LoanOffer-v3_1.json` | LoanOffer interpolated intent says "Lend {principalAmount}", but with a capacity the lender can lend up to capacity in total. |
| C | 100 | 42 | `registry/gondi/eip712-RenegotiationOffer.json` | RenegotiationOffer intent does not say the signer funds the loan from their wallet |
| C | 100 | 33 | `registry/gondi/eip712-SignableRepaymentData.json` | Intent says only 'repayment' though the callback sells the signer's collateral NFT to pay for it. |
| C | 100 | 57 | `registry/kiln/calldata-Vault-USDC-Morpho-Gauntlet-Core.json` | mint: the bare "Mint" intent does not say USDC is spent to get vault shares. |
| C | 100 | 54 | `registry/kiln/calldata-Vault-USDC-Morpho-Gauntlet-Prime.json` | mint: intent "Mint" does not say USDC is spent; no interpolatedIntent. |
| C | 100 | 56 | `registry/kiln/calldata-Vault-USDC-Morpho-Gauntlet-USDC-Core-Base-multisig.json` | mint: 'Deposit asset' displays only a ticker, so it looks like an amount field with no value. |
| C | 100 | 56 | `registry/kiln/calldata-Vault-USDC-Morpho-Smokehouse-USDC-multisig.json` | mint: the intent "Mint" does not say that USDC leaves the wallet to buy vault shares. |
| C | 100 | 62 | `registry/kiln/calldata-Vault-USDT-Morpho-Gauntlet-USDT-Core-multisig.json` | mint: the intent 'Mint' does not say USDT is paid from the wallet. |
| C | 100 | 52 | `registry/kiln/calldata-Vault-USDT-Morpho-Smokehouse-USDT-multisig.json` | mint: intent 'Mint' does not say that USDT is spent to get vault shares. |
| C | 100 | 54 | `registry/kiln/calldata-Vault-USDT-Morpho-Steakhouse-USDT-multisig.json` | mint: the bare intent "Mint" does not say that USDT is spent to get vault shares. |
| C | 100 | 56 | `registry/kiln/calldata-Vault-WBTC-Morpho-Gauntlet-Core.json` | mint shows 'Deposit asset: WBTC' with no amount, which reads like a complete deposit line. |
| C | 100 | 55 | `registry/kiln/calldata-Vault-WETH-Morpho-Gauntlet-Core.json` | mint: the intent 'Mint' does not say that WETH leaves the wallet. |
| C | 100 | 50 | `registry/kiln/calldata-Vault-cbBTC-Morpho-Gauntlet-Core.json` | deposit: the intent 'Deposit' gives no amount, no asset and no vault, and there is no interpolatedIntent. |
| A | 100 | 91 | `registry/kiln/calldata-kiln-batch-exit.json` |  |
| B | 100 | 76 | `registry/kiln/calldata-kiln-fee-splitter-factory.json` | createOperator shows recipients and percentages as two separate lists the signer must pair by position. |
| C | 100 | 84 | `registry/layerswap/calldata-LayerswapDepository.json` | depositERC20 says "Swap token" but the call only sends tokens to a solver; nothing returns. |
| A | 100 | 92 | `registry/ledgerquest/eip712-ledgerquest.json` |  |
| B | 100 | 76 | `registry/lido/calldata-stETH-L2.json` | approve: interpolatedIntent omits the spender, so the sentence does not say who may spend. |
| B | 100 | 80 | `registry/lido/calldata-wstETH-L2-bnb.json` | approve: the interpolated intent leaves out who gets the allowance. |
| B | 100 | 85 | `registry/lido/calldata-wstETH-L2-linea.json` | transferFrom sentence 'Send {amount} to {to}' omits the source address and reads as the signer sending. |
| B | 100 | 82 | `registry/lido/calldata-wstETH-L2.json` | approve: the interpolated intent leaves out the spender, so the sentence does not say who may spend. |
| C | 100 | 71 | `registry/lido/calldata-wstETH.json` |  |
| C | 100 | 48 | `registry/lombard/eip712-network-fee-authorization-mainnet.json` | feeApproval intent does not say the fee comes out of the LBTC minted to the signer. |
| C | 100 | 47 | `registry/lombard/eip712-network-fee-authorization-sepolia.json` | feeApproval intent does not say the fee is taken from the signer's minted LBTC |
| C | 100 | 42 | `registry/midas/calldata-MinterVault.json` | depositInstant shows 'Minimum to Receive' as a bare number and never names the mToken received |
| C | 100 | 57 | `registry/morpho/calldata-9summits-9SETHcore.json` | mint: the intent 'Mint' does not say that WETH is paid for vault shares, and there is no interpolatedIntent. |
| C | 100 | 64 | `registry/morpho/calldata-9summits-9SUSR.json` |  |
| B | 100 | 73 | `registry/morpho/calldata-9summits-pikuUSDC-v2-1.json` |  |
| C | 100 | 70 | `registry/morpho/calldata-BlueBundlesV1.json` | RepayAndWithdrawCollateral intent says repay and withdraw also when only one of the two happens. |
| B | 100 | 73 | `registry/morpho/calldata-BlueBuyCallbackFactory.json` | createBlueBuyCallback intent "Create buy callback" does not say it deploys a contract owned by owner. |
| C | 100 | 81 | `registry/morpho/calldata-Midnight.json` | take: neither intent line says whether the signer pays now (lend) or receives now and owes (borrow). |
| B | 100 | 68 | `registry/morpho/calldata-MidnightBundlesV1.json` | BuyWithUnitsTarget intent leaves out the amount paid and the collateral withdrawal. |
| C | 100 | 75 | `registry/morpho/calldata-MorphoBlue.json` | withdraw by shares says 'Withdraw 0 USDC' while the signer receives 500437.145758 USDC |
| C | 100 | 49 | `registry/morpho/calldata-PriceRatifierV1.json` | setIsRootRatified: the intent reads like approving the maker address, not enabling a batch of orders to be filled. |
| B | 100 | 78 | `registry/morpho/calldata-RateRatifierV1.json` |  |
| C | 100 | 66 | `registry/morpho/calldata-api3-Api3-dCOMP-USDC-v2-1.json` | mint: the intent 'Mint' hides that the signer pays USDC. |
| C | 100 | 64 | `registry/morpho/calldata-apostro-aprUSR.json` |  |
| C | 100 | 63 | `registry/morpho/calldata-armitage_by_wintermute-armUSDCp-v2-1.json` | mint: the intent 'Mint' does not say USDC leaves the signer's wallet to pay for the shares. |
| C | 100 | 66 | `registry/morpho/calldata-armitage_by_wintermute-armUSDCs-v2-1.json` | mint: the intent and the interpolated intent do not say the signer pays USDC. |
| B | 100 | 74 | `registry/morpho/calldata-armitage_by_wintermute-armUSDTs-v2-1.json` |  |
| C | 100 | 58 | `registry/morpho/calldata-b_protocol-reGOLD.json` | mint: the 'Deposit asset' field shows only a ticker, which can read as if nothing or an unknown amount is paid. |
| B | 100 | 74 | `registry/morpho/calldata-bitwise-PAPY-v2-1.json` |  |
| C | 100 | 63 | `registry/morpho/calldata-block_analitica-mwEURC.json` |  |
| C | 100 | 62 | `registry/morpho/calldata-block_analitica-mwUSDC.json` | mint: the intent 'Mint' does not say USDC leaves the wallet, and 'Deposit asset' shows a ticker without an amount. |
| B | 100 | 69 | `registry/morpho/calldata-block_analitica-mwcbBTC.json` |  |
| C | 100 | 66 | `registry/morpho/calldata-clearstar-CSUSDC.json` | redeem: the screen never names USDC as the payout asset, so the reader could not tell what arrives. |
| B | 100 | 75 | `registry/morpho/calldata-clearstar-NOONECOUSDC-v2-8453.json` |  |
| B | 100 | 80 | `registry/morpho/calldata-clearstar-REECOUSDC-v2-1.json` |  |
| B | 100 | 66 | `registry/morpho/calldata-felix-feUSDC.json` | deposit labels the USDC amount 'Deposit asset' and shows the share ticker as a separate field with no amount. |
| B | 100 | 72 | `registry/morpho/calldata-felix-feUSDT0v2-v2-999.json` |  |
| B | 100 | 75 | `registry/morpho/calldata-galaxy_curation-gUSDCq-v2-1.json` |  |
| B | 100 | 78 | `registry/morpho/calldata-galaxy_curation-gUSDTq-v2-1.json` |  |
| B | 100 | 64 | `registry/morpho/calldata-gauntlet-compUSDC.json` | deposit labels the amount 'Deposit asset' and shows a constant 'Share ticker' line instead of saying what the signer receives. |
| C | 100 | 64 | `registry/morpho/calldata-gauntlet-compUSDT.json` |  |
| C | 100 | 56 | `registry/morpho/calldata-gauntlet-elixirUSDC.json` | mint intent "Mint" does not say USDC leaves the wallet to pay for the shares. |
| C | 100 | 52 | `registry/morpho/calldata-gauntlet-gtAUSDc.json` | deposit: the intent is a bare 'Deposit' with no interpolatedIntent naming the amount, the asset or the vault shares. |
| C | 100 | 62 | `registry/morpho/calldata-gauntlet-gtLBTCc.json` | mint: the intent is just 'Mint', which hides that LBTC is deposited. There is no interpolatedIntent. |
| B | 100 | 64 | `registry/morpho/calldata-gauntlet-gtUSDCc-42161.json` | deposit intent "Deposit" names neither the asset nor the vault shares received |
| C | 100 | 55 | `registry/morpho/calldata-gauntlet-gtUSDCmkr.json` | mint intent "Mint" does not say the signer pays USDC for the shares. |
| C | 100 | 58 | `registry/morpho/calldata-gauntlet-gtUSDT.json` | mint intent 'Mint' does not say that the signer pays USDT for the vault shares. |
| C | 100 | 63 | `registry/morpho/calldata-gauntlet-gtWETH.json` | mint intent "Mint" does not say that the signer pays WETH for the shares |
| C | 100 | 61 | `registry/morpho/calldata-gauntlet-gtcbBTCc.json` | mint intent 'Mint' does not say that the signer pays cbBTC to get vault shares. |
| C | 100 | 55 | `registry/morpho/calldata-gauntlet-gtmsETHc.json` | deposit: the bare intent "Deposit" and the stand-alone ticker field leave out what is deposited and what comes back. |
| C | 100 | 70 | `registry/morpho/calldata-gauntlet-gtusdtb-v2-988.json` | mint: the intent 'Mint' and its sentence omit that the signer pays USDT0. |
| C | 100 | 66 | `registry/morpho/calldata-gauntlet-gtwethb-v2-8453.json` | mint: the intent 'Mint X gtwethb for <addr>' does not say the signer pays WETH for it. |
| C | 100 | 62 | `registry/morpho/calldata-gauntlet-ionicUSDC.json` | mint intent 'Mint' does not say the signer pays USDC into the vault. |
| C | 100 | 61 | `registry/morpho/calldata-gauntlet-ionicWETH.json` | mint label 'Deposit asset' shows the ticker 'WETH', and a reader can take it for an amount field |
| C | 100 | 58 | `registry/morpho/calldata-gauntlet-mhyETH.json` | mint: the intent 'Mint' does not say the signer pays WETH, and there is no interpolatedIntent. |
| C | 100 | 50 | `registry/morpho/calldata-gauntlet-resolvUSDC.json` | mint shows only the intent 'Mint', which does not say the signer pays USDC. |
| C | 100 | 60 | `registry/morpho/calldata-gauntlet-sbMorphotBTC.json` | mint intent 'Mint' does not say the signer pays tBTC into the vault. |
| C | 100 | 58 | `registry/morpho/calldata-gauntlet-smUSDC.json` | mint intent "Mint" does not say that the signer pays USDC to get vault shares. |
| C | 100 | 60 | `registry/morpho/calldata-gauntlet-smcbBTC.json` | mint intent 'Mint' does not say cbBTC leaves the signer's wallet. |
| B | 100 | 63 | `registry/morpho/calldata-hyperithm-hyperUSDCa.json` | deposit: the intent is only "Deposit", with no amount, asset, vault or share recipient and no interpolatedIntent. |
| B | 100 | 71 | `registry/morpho/calldata-k3_capital-K3USDC-v2-999.json` |  |
| C | 100 | 66 | `registry/morpho/calldata-kpk-KPK_USDT_Prime-v2-1.json` | redeem: the screen never says the signer receives USDT. |
| C | 100 | 61 | `registry/morpho/calldata-mev_capital-MC-USR.json` | mint: the 'Deposit asset' label shows only a ticker, so the reader may think the deposit amount is missing. |
| C | 100 | 60 | `registry/morpho/calldata-mev_capital-pWBTC.json` | mint: the intent 'Mint' does not say WBTC is paid in exchange. |
| C | 100 | 62 | `registry/morpho/calldata-re7_labs-Re7RWA.json` |  |
| C | 100 | 49 | `registry/morpho/calldata-re7_labs-Re7USDA.json` |  |
| C | 100 | 59 | `registry/morpho/calldata-re7_labs-Re7USDC-v2-8453.json` | redeem: the asset paid out (USDC) is never named on the screen |
| C | 100 | 61 | `registry/morpho/calldata-re7_labs-Re7USDC.json` | mint: 'Deposit asset: USDC' looks like a complete line yet carries no amount; the intent 'Mint' is vague. |
| C | 100 | 58 | `registry/morpho/calldata-re7_labs-Re7USDT.json` | mint intent 'Mint' does not say that the signer pays USDT for the shares. |
| C | 100 | 63 | `registry/morpho/calldata-re7_labs-Re7WBTC.json` | mint has the intent "Mint", which hides that it takes the signer's WBTC. Its "Deposit asset" field has no amount. |
| B | 100 | 73 | `registry/morpho/calldata-re7_labs-Re7WETH-1.json` |  |
| C | 100 | 62 | `registry/morpho/calldata-re7_labs-Re7cbBTC.json` | The mint intent 'Mint' does not say that the signer pays cbBTC for the shares. |
| C | 100 | 60 | `registry/morpho/calldata-re7_labs-Re7cdxUSD1.1.json` | mint has the bare intent 'Mint' and does not say the signer pays cdxUSD to get vault shares. |
| C | 100 | 60 | `registry/morpho/calldata-re7_labs-Re7wstETH.json` |  |
| B | 100 | 67 | `registry/morpho/calldata-re7_labs-meUSD.json` |  |
| C | 100 | 64 | `registry/morpho/calldata-re7_labs-pythETH.json` |  |
| C | 100 | 60 | `registry/morpho/calldata-re7_labs-pythUSDC.json` | mint: the intent 'Mint' does not say that USDC is paid, and there is no interpolatedIntent. |
| B | 100 | 73 | `registry/morpho/calldata-rockawayx-humaUSDC-v2-1.json` |  |
| B | 100 | 72 | `registry/morpho/calldata-rockawayx-roxFX-v2-1.json` |  |
| C | 100 | 59 | `registry/morpho/calldata-rockawayx-roxTORI-v2-1.json` | redeem: the screen never says the signer receives USDC, and the blind reader guessed TORI. |
| B | 100 | 73 | `registry/morpho/calldata-sharpbyte-sbAUSD-Tori-Mon-v2-143.json` |  |
| B | 100 | 74 | `registry/morpho/calldata-sky_money-skyMoneyUsdcRiskCapital-v2-1.json` | withdraw: the intent does not say that the owner's shares are burned or allowance is spent when the owner is not the signer. |
| B | 100 | 79 | `registry/morpho/calldata-sky_money-skyMoneyUsdsFlagship-v2-1.json` |  |
| B | 100 | 78 | `registry/morpho/calldata-sky_money-skyMoneyUsdsRiskCapital-v2-1.json` |  |
| B | 100 | 79 | `registry/morpho/calldata-sky_money-skyMoneyUsdtRiskCapital-v2-1.json` |  |
| C | 100 | 57 | `registry/morpho/calldata-sparkdao-sparkUSDCbc.json` | mint: the intent 'Mint' does not say that USDC leaves the signer's wallet. |
| C | 100 | 67 | `registry/morpho/calldata-steakhouse_financial-bbqAUSD-v2-1.json` | mint: the intent never says the signer pays AUSD |
| B | 100 | 72 | `registry/morpho/calldata-steakhouse_financial-bbqAUSD-v2-143.json` |  |
| B | 100 | 71 | `registry/morpho/calldata-steakhouse_financial-bbqUSDC-v2-143.json` |  |
| C | 100 | 57 | `registry/morpho/calldata-steakhouse_financial-bbqWSTETH.json` |  |
| B | 100 | 74 | `registry/morpho/calldata-steakhouse_financial-ethenaUSDC-v2-8453.json` |  |
| B | 100 | 65 | `registry/morpho/calldata-steakhouse_financial-grove-bbqAUSD.json` | deposit: the intent "Deposit" has no interpolatedIntent naming the amount, the asset or the share recipient. |
| B | 100 | 73 | `registry/morpho/calldata-steakhouse_financial-steakETH-v2-8453.json` |  |
| C | 100 | 58 | `registry/morpho/calldata-steakhouse_financial-steakETH.json` | mint intent 'Mint' does not say that the signer pays WETH for the shares. |
| C | 100 | 66 | `registry/morpho/calldata-steakhouse_financial-steakPYUSD-v2-1.json` | mint: the intent never says that PYUSD is paid. 'Mint X steakPYUSD for addr' reads like a free mint. |
| C | 100 | 60 | `registry/morpho/calldata-steakhouse_financial-steakSUSDS.json` | mint intent 'Mint' does not say that the signer pays sUSDS for the shares. |
| B | 100 | 68 | `registry/morpho/calldata-steakhouse_financial-steakUSDA.json` |  |
| C | 100 | 59 | `registry/morpho/calldata-steakhouse_financial-steakUSDC-747474.json` | The mint intent 'Mint' does not say the signer pays vbUSDC for the shares. |
| C | 100 | 54 | `registry/morpho/calldata-steakhouse_financial-steakUSDC.json` | mint intent "Mint" does not say that the signer pays USDC for the shares. |
| C | 100 | 60 | `registry/morpho/calldata-steakhouse_financial-steakUSDCrwa.json` | The mint intent 'Mint' does not say the signer pays verUSDC. The 'Deposit asset' field shows no amount. |
| C | 100 | 60 | `registry/morpho/calldata-steakhouse_financial-steakUSDM.json` |  |
| C | 100 | 64 | `registry/morpho/calldata-steakhouse_financial-steakUSDQ.json` | mint: the 'Deposit asset' field shows a bare ticker, and the 'Mint' intent does not say USDQ is paid. |
| C | 100 | 59 | `registry/morpho/calldata-steakhouse_financial-steakUSDR.json` |  |
| C | 100 | 60 | `registry/morpho/calldata-steakhouse_financial-steakUSDTBethena.json` |  |
| C | 100 | 57 | `registry/morpho/calldata-steakhouse_financial-steakWBTC.json` | The mint intent "Mint" does not say that the signer pays WBTC for the shares. |
| B | 100 | 63 | `registry/morpho/calldata-touchstone-tsXAUT-v2-1.json` |  |
| B | 100 | 65 | `registry/ocarina-trade/calldata-OTCRegistry.json` | registerOrder: the intent 'Publish offer' does not say the order becomes fillable immediately without further consent. |
| C | 100 | 59 | `registry/ocarina-trade/eip712-OTCRegistry.json` |  |
| B | 100 | 72 | `registry/ondo-finance/calldata-OUSGInstantManager.json` | subscribe interpolatedIntent adds a trailing '+' that renders as 'OUSG+', which is the name of another Ondo token. |
| A | 100 | 89 | `registry/ondo-finance/calldata-USDYInstantManager.json` | subscribe: the trailing '+' in interpolatedIntent makes the token read as 'USDY+', a name that looks like another token |
| B | 100 | 76 | `registry/ophis/calldata-Ophis-CoWSwapEthFlow.json` | createOrder has no interpolatedIntent; the intent names neither the token bought nor the amounts. |
| C | 100 | 52 | `registry/ophis/calldata-Ophis-GPv2Settlement.json` | setPreSignature: the static intent does not say whether this call authorizes or revokes the order. |
| C | 100 | 58 | `registry/ophis/eip712-Ophis-GPv2Settlement.json` | Order intent "Swap order" names no tokens or amounts, and there is no interpolatedIntent. |
| A | 100 | 96 | `registry/p2p/calldata-EigenPodManager.json` |  |
| C | 100 | 63 | `registry/p2p/calldata-NativeTokenVault.json` | claimExitedAssets intent does not name ETH or say the claim can be partial. |
| B | 100 | 70 | `registry/p2p/calldata-P2pMessageSender.json` | send: the intent and label assume a withdraw action, but the text is free-form and unchecked. |
| B | 100 | 76 | `registry/permit/eip712-permit-arbitrum-arb.json` |  |
| B | 100 | 74 | `registry/permit/eip712-permit-arbitrum-link.json` |  |
| B | 100 | 74 | `registry/permit/eip712-permit-arbitrum-usds.json` |  |
| B | 100 | 65 | `registry/permit/eip712-permit-arbitrum-usdt.json` | Permit shows the spender as a raw hex address, so the signer cannot see who it is. |
| A | 100 | 80 | `registry/permit/eip712-permit-arbitrum-wbtc.json` |  |
| A | 100 | 82 | `registry/permit/eip712-permit-arbitrum-weth.json` |  |
| B | 100 | 73 | `registry/permit/eip712-permit-avalanche_c_chain-pangolin.json` | Permit has no interpolatedIntent, so the intent line names neither the spender nor the amount. |
| A | 100 | 80 | `registry/permit/eip712-permit-avalanche_c_chain-usdc.json` |  |
| A | 100 | 80 | `registry/permit/eip712-permit-avalanche_c_chain-usdt.json` |  |
| A | 100 | 82 | `registry/permit/eip712-permit-avalanche_c_chain-yetiswap.json` |  |
| B | 100 | 78 | `registry/permit/eip712-permit-base-degen.json` |  |
| B | 100 | 70 | `registry/permit/eip712-permit-base-usdc.json` | Permit test covers only a finite amount; the "Unlimited" threshold and no-expiry deadline paths are untested. |
| B | 100 | 77 | `registry/permit/eip712-permit-base-usds.json` | Permit test covers only a finite amount, not the 'Unlimited' threshold that the code treats as infinite allowance |
| A | 100 | 82 | `registry/permit/eip712-permit-bsc-1inch-token.json` |  |
| A | 100 | 80 | `registry/permit/eip712-permit-ethereum-aave.json` |  |
| B | 100 | 75 | `registry/permit/eip712-permit-ethereum-lido-wsteth.json` |  |
| A | 100 | 82 | `registry/permit/eip712-permit-ethereum-usdc.json` |  |
| B | 100 | 76 | `registry/permit/eip712-permit-ethereum-usds.json` | Permit has no interpolatedIntent, so the intent names no token, amount or spender. |
| B | 100 | 79 | `registry/permit/eip712-permit-fantom-mimatic.json` |  |
| A | 100 | 84 | `registry/permit/eip712-permit-fantom-wootrade.json` |  |
| A | 100 | 82 | `registry/permit/eip712-permit-linea-dai.json` |  |
| A | 100 | 82 | `registry/permit/eip712-permit-linea-frax.json` |  |
| B | 100 | 76 | `registry/permit/eip712-permit-linea-usdt.json` |  |
| B | 100 | 76 | `registry/permit/eip712-permit-optimism-bob.json` |  |
| A | 100 | 81 | `registry/permit/eip712-permit-optimism-dai.json` |  |
| B | 100 | 75 | `registry/permit/eip712-permit-optimism-op.json` | Permit test only covers a finite amount; the "Unlimited" threshold message is never exercised. |
| B | 100 | 73 | `registry/permit/eip712-permit-optimism-velo.json` | Permit has no interpolatedIntent, so the intent line names no token, amount or spender. |
| B | 100 | 67 | `registry/permit/eip712-permit-polygon-aave-dai.json` | Permit has no interpolatedIntent, so the intent line leaves out the token, amount and spender. |
| A | 100 | 80 | `registry/permit/eip712-permit-polygon-aave-weth.json` |  |
| A | 100 | 84 | `registry/permit/eip712-permit-polygon-usdc.json` |  |
| C | 100 | 75 | `registry/puddleswap/calldata-StakingRewards.json` | exit(): the screen names neither the LP token withdrawn nor the reward token claimed. |
| C | 100 | 45 | `registry/rarible/eip712-rarible-erc-1155.json` | Mint1155 has no interpolatedIntent, so the sentence never gives the supply or the royalty terms being fixed. |
| A | 100 | 84 | `registry/safe/calldata-SafeProxyFactory-1.3.0.json` |  |
| A | 100 | 81 | `registry/safe/calldata-SafeProxyFactory-1.4.1.json` |  |
| C | 100 | 48 | `registry/safe/calldata-SafeToL2Setup-1.4.1.json` | setupToL2 labels the new Safe singleton (implementation) as "Module", which is a different kind of right. |
| C | 100 | 48 | `registry/safe/calldata-SafeToL2Setup-1.5.0.json` | setupToL2 labels the new Safe implementation (singleton) as 'Module', which names the wrong role. |
| C | 100 | 59 | `registry/safe/eip712-Safe-Multisig.json` | DeleteRequest says "Reject transaction" but only deletes the proposal from the off-chain queue. |
| C | 100 | 64 | `registry/sky/calldata-sUSDS.json` | mint: the intent says only 'Mint' and does not say the signer pays USDS to get sUSDS. |
| B | 100 | 76 | `registry/starkgate/calldata-StarkGate-STRK.json` | deposit shows the Starknet recipient as a long decimal integer labelled only "Recipient". |
| C | 100 | 75 | `registry/swell/calldata-swell.json` | depositViaDepositManager shows the minimum rswETH minted as a raw integer. |
| C | 100 | 25 | `registry/swissborg/calldata-WormholeTransceiver.json` | receiveMessage: the incoming BORG amount is visible only inside the raw VAA hex, never as an amount. |
| A | 100 | 80 | `registry/symbiotic/calldata-DefaultStakerRewards.json` |  |
| A | 100 | 94 | `registry/symbiotic/calldata-Reactor.json` |  |
| C | 100 | 69 | `registry/symbiotic/calldata-RewardsV2.json` | claimRewards: 'Claim data' shows 200–330 bytes of hex that a signer cannot read. |
| C | 100 | 71 | `registry/symbiotic/calldata-VaultV1-0G-OFT.json` | redeem: share count is shown as an 18-decimal raw integer that people can't read. |
| C | 100 | 68 | `registry/symbiotic/calldata-VaultV1-AA_FalconXUSDC.json` | redeem: share amount shown as a raw 18-decimal integer in the intent and the field |
| C | 100 | 75 | `registry/symbiotic/calldata-VaultV1-BARD.json` | redeem: the share amount is a raw 18-decimal integer when a unit format could show it. |
| C | 100 | 63 | `registry/symbiotic/calldata-VaultV1-BGBTC.json` | redeem shows the shares as a raw integer, but shares use the collateral's 8 decimals. |
| C | 100 | 72 | `registry/symbiotic/calldata-VaultV1-BaseTHQInternal.json` | redeem: the share amount is shown as a raw integer, although shares use the collateral's 18 decimals. |
| C | 100 | 71 | `registry/symbiotic/calldata-VaultV1-CYC-OFT.json` | redeem: the share amount is shown as a raw 18-digit integer without decimals. |
| C | 100 | 66 | `registry/symbiotic/calldata-VaultV1-ENA.json` | redeem: the share amount is shown as a raw 18-decimal integer, so a person cannot read it. |
| C | 100 | 75 | `registry/symbiotic/calldata-VaultV1-ETHFI.json` | redeem: share amount is shown as a raw 18-decimal integer instead of a readable share count. |
| C | 100 | 75 | `registry/symbiotic/calldata-VaultV1-IBTC.json` | redeem: the share amount is shown as an 18-digit raw integer in the intent and the field. |
| B | 100 | 72 | `registry/symbiotic/calldata-VaultV1-LBTC.json` |  |
| C | 100 | 68 | `registry/symbiotic/calldata-VaultV1-LINK.json` | redeem: the share count is a raw 18-decimal integer when a unit format could make it readable. |
| B | 100 | 73 | `registry/symbiotic/calldata-VaultV1-MANTA.json` | redeem: the share amount is a raw 18-digit integer that a person cannot read. |
| C | 100 | 69 | `registry/symbiotic/calldata-VaultV1-POND.json` | redeem: the share amount is shown as an 18-decimal raw integer in both the intent and the field. |
| C | 100 | 70 | `registry/symbiotic/calldata-VaultV1-SIS.json` | redeem: the share amount is shown as a raw 18-decimal integer that people cannot read. |
| C | 100 | 69 | `registry/symbiotic/calldata-VaultV1-SOLV-OFT.json` | redeem: share amount shown as raw 18-decimal integer though shares have collateral decimals. |
| C | 100 | 72 | `registry/symbiotic/calldata-VaultV1-SWELL.json` | redeem: shares are shown as a raw 18-decimal integer, but a unit format could render them readably. |
| C | 100 | 65 | `registry/symbiotic/calldata-VaultV1-SolvBTC.json` | redeem: share amount is shown as a raw 18-digit integer instead of a scaled unit. |
| C | 100 | 69 | `registry/symbiotic/calldata-VaultV1-TANSSI.json` | redeem shows the share amount as a raw 18-digit integer, but shares use the collateral's 12 decimals. |
| C | 100 | 66 | `registry/symbiotic/calldata-VaultV1-USBD.json` | redeem: shares appear as a raw 18-digit integer, in a field and in the interpolated intent. |
| C | 100 | 68 | `registry/symbiotic/calldata-VaultV1-WBTC.json` | redeem: the share amount is shown as a raw integer with no decimals, so the signer cannot judge its size. |
| C | 100 | 65 | `registry/symbiotic/calldata-VaultV1-XAUM.json` | redeem shows the shares as a raw 18-decimal integer that a signer cannot read. |
| C | 100 | 65 | `registry/symbiotic/calldata-VaultV1-ZKL.json` | redeem: the share amount is a raw 18-decimal integer, but a unit format could render it. |
| C | 100 | 71 | `registry/symbiotic/calldata-VaultV1-cbETH.json` | redeem: the share amount is an unscaled 18-digit integer; a non-expert cannot read how much is being queued. |
| C | 100 | 64 | `registry/symbiotic/calldata-VaultV1-lskETH-OFT.json` | redeem: shares are shown as a raw 18-decimal integer in both the intent and the field. |
| C | 100 | 67 | `registry/symbiotic/calldata-VaultV1-lvlwaUSDC.json` | redeem shows the vault share amount as a raw integer without decimals or unit. |
| C | 100 | 71 | `registry/symbiotic/calldata-VaultV1-lvlwaUSDT.json` | redeem: the share amount is a raw integer, though shares use the collateral's 6-decimal scale. |
| C | 100 | 64 | `registry/symbiotic/calldata-VaultV1-mETH.json` | redeem: the share amount is shown as a raw 18-decimal integer, which nobody can read. |
| C | 100 | 67 | `registry/symbiotic/calldata-VaultV1-osETH.json` | redeem: the share amount is shown as a raw 18-decimal integer in the intent and the field. |
| C | 100 | 69 | `registry/symbiotic/calldata-VaultV1-rETH.json` | redeem: shares are shown as a raw 18-decimal integer in both the intent and the field. |
| C | 100 | 71 | `registry/symbiotic/calldata-VaultV1-rsLSK-OFT.json` | redeem: the share amount is shown as a raw integer with no decimals, though shares use the collateral's scale. |
| C | 100 | 71 | `registry/symbiotic/calldata-VaultV1-rsM-BTC-OFT.json` | redeem: the share amount is a raw 18-decimal integer that a person cannot read. |
| C | 100 | 71 | `registry/symbiotic/calldata-VaultV1-rstFRAX-OFT.json` | redeem shows the vault shares as a raw 18-decimal integer in the field and the intent. |
| C | 100 | 68 | `registry/symbiotic/calldata-VaultV1-sUSDe.json` | redeem: the shares are shown as a raw integer (987654321123456789), which a person cannot read. |
| C | 100 | 71 | `registry/symbiotic/calldata-VaultV1-sfrxETH.json` | redeem: shares are shown as a raw 18-decimal integer when a unit format could scale them. |
| C | 100 | 74 | `registry/symbiotic/calldata-VaultV1-sfrxUSD.json` | redeem: the share amount is shown as a raw 18-decimal integer in the intent and the field. |
| C | 100 | 70 | `registry/symbiotic/calldata-VaultV1-tBTC.json` | claim: the screen never says the claimed asset is tBTC; intent and fields name only an epoch. |
| C | 100 | 68 | `registry/symbiotic/calldata-VaultV1-uniBTC.json` |  |
| C | 100 | 74 | `registry/symbiotic/calldata-VaultV1-wOETH.json` | redeem: the shares are shown as an 18-digit raw integer that a signer cannot read. |
| C | 100 | 75 | `registry/symbiotic/calldata-VaultV1-weETH.json` | redeem shows the vault shares as a raw 18-decimal integer that is hard to read. |
| B | 100 | 74 | `registry/symbiotic/calldata-VaultV1-wstETH.json` | redeem: the share amount is shown as a raw 18-decimal integer and is hard to read |
| C | 100 | 70 | `registry/symbiotic/calldata-VaultV1-wstUSR.json` | redeem shows the vault share amount as a raw 18-decimal integer, which is hard to read. |
| B | 100 | 78 | `registry/symbiotic/calldata-VaultV1Tokenized-GROVE.json` |  |
| B | 100 | 75 | `registry/symbiotic/calldata-VaultV1Tokenized-HYPER.json` |  |
| B | 100 | 74 | `registry/symbiotic/calldata-VaultV1Tokenized-LsETH.json` |  |
| B | 100 | 72 | `registry/symbiotic/calldata-VaultV1Tokenized-SPK.json` |  |
| B | 100 | 71 | `registry/symbiotic/calldata-VaultV1Tokenized-cbETH.json` |  |
| B | 100 | 74 | `registry/symbiotic/calldata-VaultV1Tokenized-mETH.json` |  |
| B | 100 | 77 | `registry/symbiotic/calldata-VaultV1Tokenized-rETH.json` |  |
| C | 100 | 70 | `registry/symbiotic/calldata-VaultV1Tokenized-sUSDe.json` | claim: the screen never says sUSDe is sent to the recipient; only the epoch number appears. |
| C | 100 | 68 | `registry/symbiotic/calldata-VaultV1Tokenized-sfrxETH.json` | claim: no part of the screen names sfrxETH as the asset sent to the recipient. |
| B | 100 | 77 | `registry/symbiotic/calldata-VaultV1Tokenized-swETH.json` |  |
| C | 100 | 70 | `registry/symbiotic/calldata-VaultV1Tokenized-wBETH.json` | claim never names the asset; the signer does not see that the recipient receives wBETH. |
| B | 100 | 70 | `registry/symbiotic/calldata-VaultV1Tokenized-wstETH.json` |  |
| C | 100 | 81 | `registry/symbiotic/calldata-VaultV2-USDC.json` | setManagementFee interpolated intent leaves out the new fee recipient |
| C | 100 | 66 | `registry/symbiotic/calldata-WithdrawalQueue-CSWUSDC.json` | claim does not name the asset paid out; 'Asset recipient' leaves the token the receiver gets unstated. |
| C | 100 | 60 | `registry/symbiotic/calldata-WithdrawalQueue-KPK_USDC_LL.json` | claim: the screen never names the asset paid out (the vault's underlying, e.g. USDC). |
| B | 100 | 70 | `registry/symbiotic/calldata-WithdrawalQueue-LLCassaUSDC.json` | requestRedeem: 'NFT recipient' does not say the NFT is the only right to claim the withdrawn assets. |
| C | 100 | 70 | `registry/symbiotic/calldata-WithdrawalQueue-ifUSDC.json` | claim: neither the intent nor any field names the asset that is paid out. |
| C | 100 | 62 | `registry/symbiotic/calldata-WithdrawalQueue-krfUSDC.json` | claim: the screen never names the asset that is paid out. |
| B | 100 | 65 | `registry/symbiotic/calldata-WithdrawalQueue-prestoUSDCv.json` | requestRedeem labels receiver 'NFT recipient' but never says that address alone can claim the withdrawn assets |
| B | 100 | 66 | `registry/symbiotic/calldata-WithdrawalQueue-vUSDC.json` | requestRedeem: the 'NFT recipient' label does not say the NFT holds the right to claim the withdrawn assets. |
| B | 100 | 76 | `registry/symbiotic/eip712-Reactor.json` | Request: the intent sentence leaves out the output recipients, who may not be the signer. |
| A | 100 | 81 | `registry/symbiotic/eip712-VaultV2Permit-CSWUSDC.json` | Permit intent says the approval lasts 'until {deadline}', but only the signature expires; the allowance stays forever. |
| B | 100 | 73 | `registry/symbiotic/eip712-VaultV2Permit-KPK_USDC_LL.json` | Permit interpolatedIntent says 'until {deadline}', which suggests the allowance expires, but it never does. |
| B | 100 | 79 | `registry/symbiotic/eip712-VaultV2Permit-LLCassaUSDC.json` | Permit interpolated intent says the approval lasts "until {deadline}", but the allowance never expires. |
| A | 100 | 83 | `registry/symbiotic/eip712-VaultV2Permit-ifUSDC.json` | Permit: the sentence 'Approve X for spender until deadline' suggests the allowance expires, but it does not. |
| A | 100 | 83 | `registry/symbiotic/eip712-VaultV2Permit-krfUSDC.json` | Permit interpolated intent says 'until {deadline}', which suggests the allowance expires; only the signature does. |
| B | 100 | 77 | `registry/symbiotic/eip712-VaultV2Permit-prestoUSDCv.json` | Permit: the 'until {deadline}' wording suggests the allowance expires, but only the signature does. |
| A | 100 | 90 | `registry/symbiotic/eip712-VaultV2Permit-vUSDC.json` |  |
| B | 100 | 77 | `registry/tally/eip712-tally-arbitrum-core-governor.json` | Ballot: the intent leaves out the vote choice, and there is no interpolatedIntent to carry it. |
| B | 100 | 75 | `registry/tally/eip712-tally-arbitrum-treasury-governor.json` | Ballot: no interpolatedIntent, so the vote choice (For/Against/Abstain) is missing from the one-line summary. |
| B | 100 | 75 | `registry/tally/eip712-tally-ethereum-bitcoin-governor.json` | Ballot has no interpolatedIntent, so the glance line hides the vote direction and the proposal id. |
| B | 100 | 73 | `registry/tally/eip712-tally-ethereum-bravo-governor.json` | Ballot has no interpolatedIntent, so the intent line does not say which way or on which proposal. |
| B | 100 | 73 | `registry/tally/eip712-tally-ethereum-ens-governor.json` | Ballot: the intent leaves out the vote direction and the proposal; no interpolatedIntent. |
| C | 100 | 57 | `registry/tally/eip712-tally-ethereum-ens-token.json` | Delegation expiry is shown as a raw Unix timestamp instead of a date. |
| B | 100 | 61 | `registry/tally/eip712-tally-ethereum-gtk-token.json` | Delegation: expiry is shown as a raw Unix timestamp, not as a date. |
| A | 100 | 86 | `registry/tally/eip712-tally-ethereum-hop-governor.json` |  |
| B | 100 | 64 | `registry/tally/eip712-tally-ethereum-hop-token.json` | Delegation: expiry is shown as a raw unix number instead of a date. |
| C | 100 | 59 | `registry/tally/eip712-tally-ethereum-pool-token.json` | Delegation: expiry is shown as a raw Unix timestamp, not as a date. |
| A | 100 | 84 | `registry/tally/eip712-tally-ethereum-pooltogether-governor.json` |  |
| B | 100 | 61 | `registry/tally/eip712-tally-ethereum-uni-token.json` | Delegation shows expiry as a raw Unix number, not a date |
| C | 100 | 43 | `registry/tesseract/calldata-vault-deployer-USDC.json` | deployVault intent 'Deploy Vault' leaves out the USDC deposit and the shares the signer receives. |
| C | 100 | 47 | `registry/tesseract/calldata-vault-deployer-WBTC.json` | deployVault intent "Deploy Vault" leaves out the WBTC deposit and the shares the signer receives. |
| A | 100 | 89 | `registry/tether/calldata-usdt-polygon.json` | transfer: recipient addressName types limited to eoa, though the code lets any non-zero, non-token address receive. |
| A | 100 | 90 | `registry/tether/calldata-usdt.json` | transfer field 'To' limits addressName types to eoa, but the code accepts contract recipients too. |
| B | 100 | 78 | `registry/tether/calldata-usdt0-Flare.json` | approve has one test with 100 USDT0, so the 'Unlimited' threshold path is never tested. |
| C | 100 | 55 | `registry/tether/calldata-usdt0-OFT-Flare.json` | send: recipient shown as a 32-byte padded hex word, not as an address. |
| A | 100 | 84 | `registry/tether/eip712-ReceiveWithAuthorization-usdt0-Flare.json` |  |
| B | 100 | 77 | `registry/tether/eip712-TransferWithAuthorization-usdt0-Flare.json` | TransferWithAuthorization has no interpolatedIntent, so the intent line leaves out the amount and the recipient. |
| A | 100 | 81 | `registry/tether/eip712-permit-usdt0-Flare.json` |  |
| C | 100 | 52 | `registry/threshold/calldata-L1BitcoinDepositor-address.json` | initializeDeposit: the intent does not name who receives the minted tBTC; no interpolatedIntent. |
| C | 100 | 33 | `registry/threshold/calldata-L1BitcoinDepositor-bytes32.json` | initializeDeposit shows the tBTC recipient (destinationChainDepositOwner) only as a raw 32-byte hex value. |
| C | 100 | 38 | `registry/threshold/calldata-L1BitcoinRedeemer.json` | requestRedemption: 'Main UTXO value' in BTC can be read as the amount being redeemed. |
| B | 100 | 65 | `registry/threshold/calldata-L2BitcoinDepositor.json` | initializeDeposit has no interpolatedIntent naming who will receive the minted tBTC. |
| B | 100 | 74 | `registry/threshold/calldata-L2BitcoinRedeemer.json` |  |
| C | 100 | 15 | `registry/threshold/calldata-TBTC.json` | approveAndCall shows the redemption data as raw hex, so the BTC destination and redeemer are unreadable |
| B | 100 | 76 | `registry/threshold/calldata-TBTCVault.json` |  |
| B | 100 | 88 | `registry/uniswap/calldata-UniswapV2Router02.json` |  |
| C | 100 | 47 | `registry/uniswap/eip712-uniswap-permit2.json` | PermitSingle shows the spender as a raw hex address, not as a named contract. |
| C | 100 | 61 | `registry/walletconnect/calldata-stakeweight.json` | depositFor intent "Lock tokens" hides that the tokens go to another address's lock for good. |
| C | 100 | 49 | `registry/walletconnect/calldata-wct.json` | transfer: the screen shows the amount as a raw 18-decimal integer without the WCT ticker |
| A | 100 | 96 | `registry/weth/calldata-weth.json` |  |
| C | 100 | 74 | `registry/wormhole/calldata-CircleIntegration.json` |  |
| C | 100 | 60 | `registry/wormhole/calldata-TokenBridge.json` | transferTokensWithPayload: the wormholeChain enum lists only 8 chains, so other destinations have no name. |
| B | 100 | 72 | `registry/zama/calldata-ACL.json` | delegateForUserDecryption: wildcard contract 0xFFFF…FFFF shows as a plain 'For contract' address, not 'all contracts'. |
| C | 100 | 69 | `registry/zama/calldata-ConfidentialWrapper.json` | wrap shows the underlying amount as a raw integer with no token name or decimals. |
| B | 100 | 78 | `registry/zama/eip712-DelegatedUserDecryptRequestVerificationV1.json` |  |
| B | 100 | 65 | `registry/zama/eip712-UserDecryptRequestVerificationV1.json` | The intent and the 'Authorized contracts' label suggest the contracts get a permission. In fact a key holder gets to read the signer's data. |
| B | 100 | 63 | `registry/zkstables/calldata-executor.json` | exec labels the Safe's outgoing ETH only "Value", so the signer may think the ETH comes from their own wallet. |
| C | 100 | 72 | `registry/zkstables/calldata-parswappool-base-sepolia.json` |  |
| C | 100 | 75 | `registry/zkstables/calldata-parswappool-base.json` |  |
| C | 100 | 77 | `registry/zkstables/calldata-zkhub.json` | initialize hides trcPk_ and totalSupplyPk_, the keys that decide who decrypts compliance and supply data. |
| C | 100 | 28 | `registry/zkstables/eip712-ebswap.json` |  |
| B | 100 | 73 | `registry/zkstables/eip712-zkhub.json` | ChangeControllerAuth intent does not say the signer hands over control of their ZK address. |

Model cost (list price, from the CLI): $294.18.
