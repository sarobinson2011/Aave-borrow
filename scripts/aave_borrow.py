from brownie import network, config, interface
from scripts.get_weth import get_weth
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_NETWORKS
from web3 import Web3

# AMOUNT = Web3.toWei(0.1, "ether")
AMOUNT = 100000000000000000


def main():
    account = get_account()
    erc20_address = config["networks"][network.show_active()]["weth_token"]

    if network.show_active() in ["mainnet-fork"]:
        get_weth()

    lending_pool = get_lending_pool()

    approve_tx = approve_erc20(AMOUNT, lending_pool.address, erc20_address, account)

    tx = lending_pool.supply(erc20_address, AMOUNT, account, 0, {"from": account})
    tx.wait(1)

    print("\n--> Successfully deposited!")

    borrowable_eth, total_debt = get_borrowable_data(lending_pool, account)
    # print(f"\n--> available to borrow: {borrowable_eth} WETH")
    # print(f"\n--> already borrowed: {total_debt} WETH")


def get_borrowable_data(lending_pool, account):
    (
        total_collateral_base,
        total_debt_base,
        available_borrows_base,
        current_liquidation_threshold,
        ltv,
        health_factor,
    ) = lending_pool.getUserAccountData(account)

    available_borrows_base = Web3.fromWei(available_borrows_base, "ether")
    # total_collateral_base = Web3.fromWei(total_collateral_base, "ether")
    total_debt_base = Web3.fromWei(total_debt_base, "ether")
    print(f"\n--> You have {total_collateral_base} worth of ETH deposited")
    print(f"\n--> You have {total_debt_base} worth of ETH borrowed")
    print(f"\n--> You have {available_borrows_base} worth of ETH available to borrow\n")
    return (available_borrows_base, total_debt_base)


def approve_erc20(AMOUNT, spender, erc20_address, account):
    # Approve sending out erc20 tokens
    print("\n--> Approving ERC20 token...")
    erc20 = interface.IERC20(erc20_address)
    tx = erc20.approve(spender, AMOUNT, {"from": account})
    tx.wait(1)
    print("--> Token approved\n")
    return tx


def get_lending_pool():
    lending_pool_addresses_provider = interface.IPoolAddressesProvider(
        config["networks"][network.show_active()]["pool_addresses_provider"]
    )
    lending_pool_address = lending_pool_addresses_provider.getPool()
    lending_pool = interface.IPool(lending_pool_address)
    return lending_pool
