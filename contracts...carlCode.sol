pragma solidity ^0.5.17;

contract funDrop {
  address owner;
  address payable recipient;
  address payable sender;
  uint winner_index;
  uint i;
  address payable winner;
  struct Donor {
    uint totalDonation;
    bool isEntity;
  }
  address payable[]  entries;
  mapping (address => Donor) public Donors;
  constructor(address payable _recipient) public {
    recipient = _recipient;
    owner = msg.sender;
   }
  function donate() public payable returns(bool success) {
    sender = msg.sender;
    Donors[sender].totalDonation += msg.value;
    i = 0;
    for (i=0; i<msg.value; i+=10000000000000000) {
      entries.push(sender);
    }
    return true;
  }
  function contractBalance() public view returns(uint){
      return address(this).balance;
  }
  function checkDonors(address donorAddress) public view returns(uint){
      require(msg.sender==owner);
      return Donors[donorAddress].totalDonation;
  }
  function checkEntries() public view returns(address payable [] memory){
      require(msg.sender==owner);
      return entries;
  }
    function random() private view returns (uint) {
        //https://stackoverflow.com/questions/48848948/how-to-generate-a-random-number-in-solidity
        return uint(keccak256(abi.encodePacked(block.difficulty, block.timestamp)));
    }
    function endAuction() public{
      require(msg.sender==owner);
        winner_index = random() % entries.length;
        winner = entries[winner_index];
        winner.transfer(address(this).balance/5);
        recipient.transfer(address(this).balance);
    }
    function viewWinner() public view returns (address){
      return winner;
    }
}