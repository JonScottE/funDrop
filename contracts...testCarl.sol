pragma solidity ^0.5.0; // newest, end of Tuesday class

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract FUNdrop is ERC721Full {  //makes the contract take the import above
    constructor() public ERC721Full("FUNdropToken", "DROP") {} //

    struct FUNdraiser{  // this is creating the NFT- which we are treating as the "cause" or fundraising event
        address payable owner; // this is stating who the funds from the event will go to
        string cause; // creating the name of the fundraising event
     //   address donor_wallet; // taking the ID/wallet of the donors
        uint256 donation_amount; // for declaring a donation amount
        
    }
    struct Donor {
    uint totalDonation;
    bool isEntity;
  }

   mapping(uint256 => FUNdraiser) public FUNdraiser_mapping; // Saves info defined below to the struct above
   mapping (address => Donor) public Donors; //saves the 

    event Donation(uint256 tokenId, uint256 donation_amount, string reportURI); // when someone makes a donation, needs a ID , amount (although

    function CreateFundraiser( // allows someone to initiate the struct?
        string memory cause,
        address payable owner,
      //  address donor_wallet,
        uint256 donation_amount,
        string memory tokenURI
        
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();

    

        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        FUNdraiser_mapping[tokenId] = FUNdraiser(owner, cause, donation_amount); //donor_wallet, was removed, this defines what is being mapped

        return tokenId;
    }