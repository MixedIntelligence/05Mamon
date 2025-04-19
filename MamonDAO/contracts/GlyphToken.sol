// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract GlyphToken is ERC721URIStorage {
    uint256 public nextId;

    constructor() ERC721("Glyph of Conscience", "GLYPH") {}

    function mintGlyph(address to, string memory uri) public {
        _mint(to, nextId);
        _setTokenURI(nextId, uri);
        nextId++;
    }

    function _transfer(address from, address to, uint256 tokenId) internal pure override {
        revert("Glyphs are soulbound and cannot be transferred");
    }
}
