## Functions

1. Swap some ETH for WETH
2. Deposit WETH into Aave - lendingpool
3. Borrow some asset against the ETH collateral
    4. Sell that borrowed asset (short sell) 
5. Repay everything back

(Working in combination with a DEX (Paraswap, Uniswap etc.))


## Testing:

Unit tests:         Mainnet-fork (if using an oracle --> development with mocks)
Integration test:   Sepolia


### Aave developer docs:

https://docs.aave.com/developers/deployed-contracts/v3-testnet-addresses
