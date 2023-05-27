from scripts.helpful_scripts import get_account
from brownie import interface, network, config
from web3 import Web3

VALUE = 0.1 * 10**18


def main():
    get_weth()


def get_weth():
    """
    Mints WETH by depoisiting ETH
    """
    account = get_account()
    #  instantiate WETH interface
    weth = interface.WethInterface(
        config["networks"][network.show_active()]["weth_token"]
    )
    # now call deposit()
    tx = weth.deposit({"from": account, "value": VALUE})
    tx.wait(1)
    # print(f"--> Received 0.1 WETH")

    tx = weth.balanceOf(account)
    tx_balance = Web3.fromWei(tx, "ether")
    print(f"\n--> WETH balance: {tx_balance}\n")
