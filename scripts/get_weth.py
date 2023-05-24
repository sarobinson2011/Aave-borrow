from scripts.helpful_scripts import get_account
from brownie import interface, network, config
from web3 import Web3


def main():
    get_weth()


def get_weth():
    """
    Mints WETH by depoisiting ETH
    """
    # We need 2 things:
    #  1. ABI       -->     get WethInterface.sol
    #  2. Address   -->     xxx
    value = 0.1 * 10**18
    account = get_account()

    #  instantiate WETH interface
    weth = interface.WethInterface(
        config["networks"][network.show_active()]["weth_token"]
    )
    # now call deposit()
    tx = weth.deposit({"from": account, "value": value})
    tx.wait(1)
    print("Received 0.1 WETH")
