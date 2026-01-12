pragma solidity ^0.7.0;

contract Test {
    function withdraw(address payable user) public {
        user.call{value: 1 ether}("");
    }
}
