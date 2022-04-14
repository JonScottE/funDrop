import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI-------------- got ABI from contract deployment in remix, saved to existing artregistry_abi.json
    with open(Path('artregistry_abi.json')) as f: #points to the .json file saved locally, sets our .json as -f-
        contract_abi = json.load(f)  # loads our .json and saves as contract_abi

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS") # once deployed from remix, save the contract address to 

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address, # variable set above with .env file
        abi=contract_abi    # variable set above with .json
    )

    return contract


# Load the contract
contract = load_contract()


################################################################################
# Register New Artwork
################################################################################
st.title("Start a funDrop!")

st.write("Choose your wallet")
accounts = w3.eth.accounts
owner = st.selectbox("Select your account for funds to go to.", options=accounts) # this should be reflecting the address of the payable owner
st.markdown("---")

cause = st.text_input("Enter the name of the Cause") 

donation_amount = int(st.number_input("How Much would you like to raise", step=1)) 

tokenURI = st.text_input("Enter Cause ID") #shit hack here, should be getting it from the contract, should this just read tokenURI = tokenURI???

if st.button("Let the funDrop begin!"):
    tx_hash = contract.functions.CreateFundraiser(cause, owner, donation_amount, tokenURI).transact({'from': owner, 'gas': 1000000}) #donor_wallet,removed but hashed out in case
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
st.markdown("---")

################################################################################
# Make a donation
################################################################################
st.markdown("## Make a donation")
st.selectbox("Find your cause", options={cause})

st.write(f"The donation amount is {donation_amount}.")

# sender = msg.sender
sender = st.selectbox("Select your account to donate funds from.", options=accounts)
if st.button("Donate"): # just want this to take from sender and give to original owner
    # Make the Donation
    
    Donate = contract.functions.donate(owner).transact({'from':sender, 'gas':1000000})
    receipt = w3.eth.waitForTransactionReceipt(Donate)
    st.write("Thank you for your donation.")
    #st.image
    

   
