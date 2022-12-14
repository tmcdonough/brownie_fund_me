from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        req_confirms = 1
        acc = accounts[0]
    else:
        req_confirms = 1
        acc = accounts.add(config["wallets"]["from_key"])
    return acc, req_confirms


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying mocks...")
    if len(MockV3Aggregator) <= 0:
        account, req_confirms = get_account()
        MockV3Aggregator.deploy(
            DECIMALS,
            STARTING_PRICE,
            # Web3.toWei(STARTING_PRICE, "ether"),
            {"from": account, "required_confs": req_confirms},
        )
    print("Mocks Deployed!")
