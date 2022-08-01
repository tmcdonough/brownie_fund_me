from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from web3 import Web3


def deploy_fund_me():

    account, req_confirms = get_account()

    # if we are on a persistent network like rinkeby or goerli, use the associated address
    # otherwise, deploy mocks.

    # price_feed_address = "0x8A753747A1Fa494EC906cE90E9f37563A8AF630e"

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        print(f"{network.show_active}")
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {
            "from": account,
            "required_confs": req_confirms,
        },
        publish_source=config["networks"][network.show_active()].get(
            "verify"
        ),  # publishes the sourcecode / abi to etherscan
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
