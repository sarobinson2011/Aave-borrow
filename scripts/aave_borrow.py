from brownie import network, config, interface
from scripts.get_weth import get_weth
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_NETWORKS


def main():
    account = get_account()
    erc20_address = config["networks"][network.show_active()]["weth_token"]

    #  call get_weth() if needed
    if network.show_active() in ["mainnet-fork"]:
        get_weth()

    # ABI
    # Address
    lending_pool = get_lending_pool()
    print(lending_pool)


def get_lending_pool():
    lending_pool_addresses_provider = interface.IPoolAddressesProvider(
        config["networks"][network.show_active()]["pool_addresses_provider"]
    )
    lending_pool_address = lending_pool_addresses_provider.getPool()
    lending_pool = interface.IPool(lending_pool_address)
    return lending_pool
