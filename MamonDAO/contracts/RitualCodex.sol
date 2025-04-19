// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract RitualCodex {
    struct Record {
        string glyph;
        string purpose;
        string emotionalHash;
    }

    mapping(uint => Record) public records;
    uint public count;

    function inscribe(string memory glyph, string memory purpose, string memory emotionalHash) public {
        records[count++] = Record(glyph, purpose, emotionalHash);
    }
}
