from web3 import Web3
import json
from flask import current_app

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(current_app.config['WEB3_PROVIDER_URI']))

# Load the smart contract
def get_contract():
    contract_address = current_app.config['CONTRACT_ADDRESS']
    abi = json.loads(current_app.config['CONTRACT_ABI'])
    return web3.eth.contract(address=contract_address, abi=abi)

# Function to mint fungible tokens
def mint_fungible_tokens(to_address, amount):
    contract = get_contract()
    tx = contract.functions.mintFungible(to_address, amount).buildTransaction({
        'from': web3.eth.default_account,
        'gas': 2000000
    })
    # Sign and send transaction
    signed_tx = web3.eth.account.sign_transaction(tx, private_key="YOUR_PRIVATE_KEY")
    web3.eth.send_raw_transaction(signed_tx.rawTransaction)

# Function to mint a unique NFT
def mint_nft(to_address):
    contract = get_contract()
    tx = contract.functions.mintNFT(to_address).buildTransaction({
        'from': web3.eth.default_account,
        'gas': 2000000
    })
    # Sign and send transaction
    signed_tx = web3.eth.account.sign_transaction(tx, private_key="YOUR_PRIVATE_KEY")
    web3.eth.send_raw_transaction(signed_tx.rawTransaction)
