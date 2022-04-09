pragma solidity ^0.5.0; // newest, end of Saturday class

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract FUNdrop is ERC721Full {
    constructor() public ERC721Full("FUNdropToken", "DROP") {}

    struct FUNdraiser{  // this is creating the NFT- which we are treating as the "cause" or fundraising event
        address payable owner; // this is stating who the funds from the event will go to
        string cause; // creating the name of the fundraising event
        address donor_wallet; // taking the ID/wallet of the donors
        uint256 donation_amount; // for declaring a donation amount
        
    }

    mapping(uint256 => FUNdraiser) public FUNdraiser_mapping; // ???? NOT REALLY SURE

    event Donation(uint256 tokenId, uint256 donation_amount, string reportURI); // when someone makes a donation, needs a ID , amount (although

    function CreateFundraiser(
        string memory cause,
        address payable owner,
        address donor_wallet,
        uint256 donation_amount,
        string memory tokenURI
        
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();

    

        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        FUNdraiser_mapping[tokenId] = FUNdraiser(owner, cause, donor_wallet, donation_amount);

        return tokenId;
    }
/*
    function newAppraisal(
        uint256 tokenId,
        uint256 newAppraisalValue,
        string memory reportURI
    ) public returns (uint256) {
        artCollection[tokenId].appraisalValue = newAppraisalValue;

        emit Appraisal(tokenId, newAppraisalValue, reportURI);

        return artCollection[tokenId].appraisalValue;
    }
    */
}
