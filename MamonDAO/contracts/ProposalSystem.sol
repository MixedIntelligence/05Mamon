// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract ProposalSystem {
    struct Proposal {
        string title;
        string sigil;
        string intent;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
    }

    mapping(uint => Proposal) public proposals;
    uint public proposalCount;

    function createProposal(string memory title, string memory sigil, string memory intent) public {
        proposals[proposalCount++] = Proposal(title, sigil, intent, 0, 0, false);
    }

    function vote(uint proposalId, bool support) public {
        Proposal storage p = proposals[proposalId];
        require(!p.executed, "Already executed");
        if (support) {
            p.votesFor++;
        } else {
            p.votesAgainst++;
        }
    }

    function executeProposal(uint proposalId) public {
        Proposal storage p = proposals[proposalId];
        require(!p.executed, "Already executed");
        require(p.votesFor > p.votesAgainst, "Not enough support");
        p.executed = true;
        // Rituals and fund movement can be triggered here
    }
}
