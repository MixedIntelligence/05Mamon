const hre = require("hardhat");

async function main() {
  const [deployer] = await hre.ethers.getSigners();

  const MXI = await hre.ethers.getContractFactory("MXIToken");
  const mxi = await MXI.deploy();
  await mxi.deployed();
  console.log("MXI deployed to:", mxi.address);

  const Glyph = await hre.ethers.getContractFactory("GlyphToken");
  const glyph = await Glyph.deploy();
  await glyph.deployed();
  console.log("Glyph deployed to:", glyph.address);

  const Proposals = await hre.ethers.getContractFactory("ProposalSystem");
  const proposals = await Proposals.deploy();
  await proposals.deployed();
  console.log("Proposals deployed to:", proposals.address);

  const Codex = await hre.ethers.getContractFactory("RitualCodex");
  const codex = await Codex.deploy();
  await codex.deployed();
  console.log("RitualCodex deployed to:", codex.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
