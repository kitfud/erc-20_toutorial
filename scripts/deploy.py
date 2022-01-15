from brownie import OurToken, accounts, network


def deploy_our_token():
    account = accounts.load("freecodecamp-account")
    deployedOurToken = OurToken.deploy(1000, {"from": account})
    print(deployedOurToken)
    print(deployedOurToken.name())
    print("success")


def main():
    deploy_our_token()
