# Setup
from web3 import Web3

ACCOUNT = "0xF8f8269488f73fab3935555FCDdD6035699deE25"


def main():

    alchemy_url = (
        "https://eth-mainnet.g.alchemy.com/v2/Eip3WhOPyEilqfLs5xs4dZ76CZs8R43g"
    )
    w3 = Web3(Web3.HTTPProvider(alchemy_url))

    # Print if web3 is successfully connected
    print(f"\nWeb3 is connected: {w3.isConnected()}")

    # Get the latest block number
    latest_block = w3.eth.block_number
    print(f"\nLatest block is: {latest_block}")

    # Get the balance of an account
    # balance = w3.eth.get_balance("0x742d35Cc6634C0532925a3b844Bc454e4438f44e")
    balance = w3.eth.get_balance(ACCOUNT)
    balance_ether = Web3.fromWei(balance, "ether")
    print(f"\nBalance of account: {balance}")
    print(f"\nBalance of account: {balance_ether}")

    # Get the information of a transaction
    tx = w3.eth.get_transaction(
        "0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060"
    )
    print(f"\nTransaction info:\n {tx}\n")
