from brownie import FundMe, MockV3Aggregator
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    mock = MockV3Aggregator[-1]
    account, confirms = get_account()
    print(f"Eth price: {fund_me.getPrice()}")
    print(f"Latest Round Data: {mock.latestRoundData()}")
    print(fund_me.getConversionRate(1))
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee, "required_confs": confirms})


def withdraw():
    fund_me = FundMe[-1]
    account, confirms = get_account()
    fund_me.withdraw({"from": account, "required_confs": confirms})


def main():
    fund()
    print("Finished funding, now withdrawing...")
    withdraw()
