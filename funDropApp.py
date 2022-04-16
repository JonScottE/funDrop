import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st




load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

#start presentation part here

st.title("Starting a Token!")
st.title("funDrop")
st.image("really_fun_drop.png")

if st.button("The Vision"):
    st.write ("The vision of the project was to lay the groundwork, for humanity to be able to save humanity, and ergo the world, through a fundraising token.")
    st.write ("The ultimate goal included a lottery system, where people would WANT to donate more money to the cause.")
    st.write ("And everyone would get some participation NFT art, so they could humblebrag on social media with it about how amazing they are.")
    st.write ("And anyone would be able to create their own fundraiser.")
   
        
if st.button("What we got"):
    st.write ("We're pretty sure we just made a very basic and simple tool for people to steal someones money anonymously... ")
    st.image("hamburgler.jpg")
    st.write ("So who wants to see it?")
  
    st.markdown("---")
    
st.title("This is the Code")
st.image("mandolorian.png")

if st.button("ERC-20 versus ERC-721"):
    st.write ("Because of the NFT art aspect of the vision, the group decided on the ERC-721 path.")
    st.write ("Pragma 5 cause we started with a class example to get us going.")
    st.write ("And setting the contract to import ERC-721 full.")
    st.image("erc721fundrop.png")
    
if st.button("The Struct!!!"):
    st.write ("This is the struct saying what will be included in the contracts, the structure of the contract.")
    st.write ("Technically it allows users to create their own data type in the form of structure'")
    st.image("struct_fundrop_code.png")

if st.button("The funDrop"):
    st.write ("The meat and potatoes of the code.  This is public so anyone can do it.")
    st.write ("It allows someone to input the cause name, state the owner as the creator, and allows the creator to state the donation amount they're looking for.")
    st.write ("And it mints the NFT.")
    st.image("start_fundraiser_function.png")
    
if st.button("Dough-nations!!!"):
    st.write ("I'm not going to lie, I though the code was done...")    
    st.write ("Until Andrei was all:")  
    st.write ("How do we steal the money, if theres no way for them to give it to us?")
    st.write ("(Lester found this -extra- hilarious)")
    st.image("donation_function.png")
    st.write ("Very bare bones, just gimme the money.") 
    
    st.markdown("---")
    
st.title("Now it seems like you're just making up names...") 
if st.button("ABI?"):
    st.write ("Errors are worked out, and I'm ready to punch my computer.") 
    st.write ("Check the compiler, make sure it matches/accepts the pragma") 
    st.write ("Make sure it's the right contract.")  
    st.write ("DONT FORGET TO COPY THE ABI")  
    st.image("save_the_abi.png")

if st.button("JSON???"):  
    st.write ("Take that ABI, and paste it into a notepad that's saved locally (mines in jupyterlab).")
    st.write ("that will eventually be called by streamlit, so it can 'read' the contract")  
    st.image("JSON_image_code.png")
    
if st.button("How JSON looks"):     
    st.write ("Here's a sample of the actual json code:") 
    st.image("json_code_looks.png")

st.markdown("---")
        
st.title("Deployment")

if st.button("The five steps to deploy:"):     
    st.write ("Step 1: Check your environment, injected web.") 
    st.write ("Step 2: Check your account, this will be the receiving account.  Make sure it matches an account hash in Ganache") 
    st.write ("Step 3: Check your contract, make sure it's right.") 
    st.write ("Step 4: Click deploy.")
    st.write ("Step 5: Copy the contract address. Paste it into your .env file (like with API's), so the contract can be accessed. ") 
    st.image("5_steps_to_deploy.png")


if st.button("On to the magic!!!!"):         
    st.image("magic.gif")    
      
    
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
# Start a funDrop
################################################################################
st.title("Start a funDrop!")

st.write("Choose your wallet")
accounts = w3.eth.accounts
owner = st.selectbox("Select your account for funds to go to.", options=accounts) # this should be reflecting the address of the payable owner
st.markdown("---")

cause = st.text_input("Enter the name of the Cause") 

donation_amount = int(st.number_input("How Much would you like to raise", step=1)) 

tokenURI = st.text_input("Enter Cause's secret PIN number") #shit hack here, should be getting it from the contract...

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
    
    Donate = contract.functions.donate().transact({'from':sender,'value':donation_amount, 'gas':1000000})
    receipt = w3.eth.waitForTransactionReceipt(Donate)
    st.write("BWAHAHA!!  We got your Money BEYATCH!!!!")
    st.markdown("---")
    
    st.write("Now you gonna be all:")
    
    st.image("dear-diary.gif")

 
st.markdown("---")

st.title("SpaceBalls: The Whitepaper!")
if st.button("The Whitepaper"):
    st.text_area("We wanted to create a fundraiser and put it on the blockchain.  As a group we decided to go with a non fungible token. We created the blockchain to protect us from theft and use it to pay others out of our income. \n\n\nThe blockchain allowed us to take control of the funds and the blockchain keeps track of all the transactions that were put in by other people who have this control over our funds. Since there was no limit on the number of bitcoins or litecoin transactions made, it meant we needed to be able to set up an account to transfer our bitcoins to people else while we paid out from our wallet. We spent two weeks getting all the users together to get their signatures to an agreement on how we could pay them back in bitcoins. We also created a payment tool to help with that as well. Now we've got a tool that works without that limitation. The blockchain is a completely fungible value, so there really isn't anything that could possibly go wrong with it. It's all done at the right speed.")

    
    st.text_area("By setting up a cryptocurrency infrastructure, we could empower people to fund whatever they wanted. The erc-721 standard was  icky for a number of reasons. One is, the coins are completely fungible (it makes no sense to store them with other cryptocurrencies), thus anyone who wants to sell them can make money by selling them on exchanges and buying them in exchange for a share in an investment. For example, in early 2015, bitcoin lost over 7 million BTC in value, it's no coincidence that at that time bitcoin was going through a massive correction because only 7% of the users had the ability to buy and sell on exchanges and only about 90% of users kept the full value of their coins to themselves. In short, we could be creating the most convenient form or currency for people to keep their money, but at the same time, we needed to develop a secure way to use them and the core protocol was broken. A crypto-currency needs software to run on the coins when someone tries to buy/sell them and when someone tries not to buy them (that's when you buy them). We then had to do a rewrite of the entire decentralized cryptocurrency roadmap in order to improve the protocol so you had to get it working.")
    
    st.text_area("Uncertain Regulations and Enforcement Actions : The regulatory status of the funDrop Token and distributed ledger technology has been carefully considered in every regulatory area, including in-country issuance of licenses. The regulatory status of the funDrop Token and distributed ledger technology has been carefully considered in every regulatory area, including in-country issuance of licenses. Prevalence of crypto-currencies on exchanges : The crypto-currencies on exchanges include: BitStamp,CoinDash, Gemcoin, Hexchange, XR,P BitNexa, Viridianx.  In exchange for the tokens generated in the cryptocurrency, users will receive a small amount of tokens. The fees will depend on the total supply of tokens and their availability.  The crypto-currencies on exchanges include: XRP, XCP, XRP, XCP Hashing, Blockchain Blockchain Security Crypto-currency security consists of a mechanism to keep a single key of the source code secure, as well as secure from outside attack. Protocols like S.I.S and OSE do not support the standard Bitcoin protocol. There are no 'official' mechanisms that enable 'this.")
    
    st.text_area("In conclusion, the NFT fundraising token funDrop will change the world, by letting humanity save humanity.\n\nWe'll look out for NFT in future announcements, and look forward to your feedback. Don't forget to join our social media accounts for the day, and tell your friends to help support the cause.")
    
st.markdown("---") 

st.title("What just happened, I don't smell burnt toast, but I feel like I should be?") 
if st.button("What gives?"):
    st.write ("Ok, you got us... We didn't write that.") 
    st.write ("We originally wanted to have a full legit whitepaper.")
    st.write ("But then were all... 'that seems like a lot of work.'")
    st.write ("We're officially programmers, there has to be a lazier way.")
    st.write ("Why not machine learn, and feed some whitepapers into an LSTM model???")
    st.write ("But that was way too much work.  We needed something EVEN lazier...")
    st.write ("Then we found the GPT-2")
    st.image("GPT-2_image.png", caption="This is the ultimate in lazy...")
    st.write ("The GPT-2 is a text predictor, but it's pretrained with some 15 million documents/texts.")
    st.write ("We just wrote the first couple sentences, and tried to keep them 'keyword rich'")
    
    
st.title("What would we do differently?") 
if st.button("What was just wrong"):
    st.write ("1- not NFT, probably erc-20") 
    st.write ("Possibly erc-1155. Like an erc777, it takes parts from both 20 and 721, to accomodate tokens and NFT's") 
    st.write ("Very specifically it passes both token and NFT through as an array.")
    st.write ("So for example, in gaming, a character can have both a rare item like a excalibur type sword (nft), as well as in game tokens/coins ")
   

