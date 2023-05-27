from brownie import network, config, interface
from scripts.aave_borrow import (
    get_account,
    get_lending_pool,
    get_borrowable_data,
    approve_erc20,
)
from scripts.get_weth import get_weth
from scripts.helpful_scripts import get_account
from web3 import Web3

AMOUNT = 100000000000000000  # 0.1 ether


def main():
    erc20_address = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
    account = get_account()
    print(f"\naccount: {account}")
    # account_balance = account.balance()
    account_balance = Web3.fromWei(account.balance(), "ether")
    print(f"\nbalance of account: {account_balance} ETH\n")

    if network.show_active() in ["mainnet-fork"]:
        get_weth()

    lending_pool = get_lending_pool()
    print(f"Lending pool = {lending_pool}")  # TODO

    approve_tx = approve_erc20(AMOUNT, lending_pool.address, erc20_address, account)
    # print(approve_tx)

    tx = lending_pool.supply(erc20_address, AMOUNT, account, 0, {"from": account})
    tx.wait(1)

    (
        data1,
        data2,
        data3,
        data4,
        data5,
        data6,
    ) = get_borrowable_data(account)
