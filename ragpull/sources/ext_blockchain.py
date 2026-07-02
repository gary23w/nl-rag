"""Blockchain, cryptocurrency, smart contracts, and Web3."""

from .common import APACHE, CC_BY_SA, MIT, WIKI, wiki

DOMAINS = {
    "bitcoin": {
        "tags": ["bitcoin", "btc", "bitcoin protocol", "utxo model", "satoshi nakamoto"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Bitcoin",
            "Bitcoin_protocol",
            "Lightning_Network",
            "SegWit",
            "Fork_(blockchain)",
            "Litecoin",
        ),
    },
    "ethereum": {
        "tags": ["ethereum", "ether cryptocurrency", "vitalik buterin", "ethereum account"],
        "license": CC_BY_SA + " / CC-BY-4.0 (ethereum.org)",
        "pages": wiki("Ethereum", "Ethereum_Classic", "Vitalik_Buterin")
        + [
            "https://ethereum.org/en/developers/docs/accounts/",
            "https://ethereum.org/en/developers/docs/transactions/",
            "https://ethereum.org/en/developers/docs/nodes-and-clients/",
            "https://ethereum.org/en/developers/docs/dapps/",
        ],
    },
    "solidity-lang": {
        "tags": ["solidity", "solidity contract", "solidity types", "contract inheritance"],
        "license": "GPL-3.0 (soliditylang.org)",
        "pages": wiki("Solidity", "Smart_contract", "Application_binary_interface")
        + [
            "https://docs.soliditylang.org/en/latest/introduction-to-smart-contracts.html",
            "https://docs.soliditylang.org/en/latest/structure-of-a-contract.html",
            "https://docs.soliditylang.org/en/latest/types.html",
            "https://docs.soliditylang.org/en/latest/contracts.html",
            "https://docs.soliditylang.org/en/latest/solidity-by-example.html",
        ],
    },
    "smart-contracts": {
        "tags": ["smart contract", "on-chain code", "contract execution", "dapp"],
        "license": CC_BY_SA + " / CC-BY-4.0 (ethereum.org)",
        "pages": wiki("Smart_contract", "Decentralized_autonomous_organization", "The_DAO", "Solidity")
        + [
            "https://ethereum.org/en/developers/docs/smart-contracts/",
            "https://ethereum.org/en/developers/docs/dapps/",
        ],
    },
    "web3js": {
        "tags": ["web3.js", "web3js", "ethereum javascript api", "web3 provider"],
        "license": "LGPL-3.0 (web3.js docs)",
        "pages": wiki("Web3", "JavaScript", "Application_binary_interface")
        + [
            "https://docs.web3js.org/guides/getting_started/quickstart",
            "https://docs.web3js.org/guides/web3_eth/methods",
            "https://docs.web3js.org/guides/smart_contracts/smart_contracts_guide",
            "https://docs.web3js.org/guides/wallet/",
        ],
    },
    "ethers-js": {
        "tags": ["ethers.js", "ethers", "ethereum provider", "contract abstraction"],
        "license": MIT + " (ethers.js docs)",
        "pages": wiki("Web3", "Node.js", "Application_binary_interface")
        + [
            "https://docs.ethers.org/v6/getting-started/",
            "https://docs.ethers.org/v6/api/contract/",
            "https://docs.ethers.org/v6/api/providers/",
        ],
    },
    "hardhat": {
        "tags": ["hardhat", "hardhat network", "solidity testing", "contract deployment"],
        "license": MIT + " (hardhat docs)",
        "pages": wiki("Solidity", "Ethereum", "Node.js")
        + [
            "https://hardhat.org/hardhat-runner/docs/getting-started",
            "https://hardhat.org/hardhat-runner/docs/guides/project-setup",
            "https://hardhat.org/hardhat-runner/docs/guides/test-contracts",
            "https://hardhat.org/hardhat-runner/docs/guides/deploying",
        ],
    },
    "foundry-ethereum": {
        "tags": ["foundry", "forge testing", "solidity fuzzing", "anvil node"],
        "license": APACHE + " / MIT (foundry book)",
        "pages": wiki("Solidity", "Ethereum", "Smart_contract")
        + [
            "https://book.getfoundry.sh/getting-started/installation",
            "https://book.getfoundry.sh/forge/writing-tests",
            "https://book.getfoundry.sh/forge/cheatcodes",
            "https://book.getfoundry.sh/anvil/overview",
        ],
    },
    "truffle-suite": {
        "tags": ["truffle framework", "contract migration", "ganache", "solidity toolchain"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Solidity",
            "Ethereum",
            "Smart_contract",
            "Application_binary_interface",
            "Web3",
            "Node.js",
        ),
    },
    "proof-of-work": {
        "tags": ["proof-of-work", "hashcash", "crypto mining", "nakamoto consensus"],
        "license": CC_BY_SA + " / CC-BY-4.0 (ethereum.org)",
        "pages": wiki(
            "Proof_of_work",
            "Hashcash",
            "Mining_pool",
            "Application-specific_integrated_circuit",
            "Bitcoin",
        )
        + [
            "https://ethereum.org/en/developers/docs/consensus-mechanisms/pow/",
        ],
    },
    "proof-of-stake": {
        "tags": ["proof-of-stake", "proof-of-stake staking", "validator", "peercoin"],
        "license": CC_BY_SA + " / CC-BY-4.0 (ethereum.org)",
        "pages": wiki(
            "Proof_of_stake",
            "Peercoin",
            "Ouroboros_(protocol)",
            "Cardano_(blockchain_platform)",
            "Ethereum",
        )
        + [
            "https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/",
        ],
    },
    "merkle-tree": {
        "tags": ["merkle tree", "hash tree", "merkle root", "merkle proof"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Merkle_tree",
            "Hash_tree_(persistent_data_structure)",
            "Cryptographic_hash_function",
            "Bitcoin_protocol",
            "Blockchain",
        )
        + [
            "https://docs.ipfs.tech/concepts/how-ipfs-works/",
        ],
    },
    "decentralized-finance": {
        "tags": ["defi", "decentralized finance", "automated market maker", "yield farming"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Decentralized_finance",
            "Uniswap",
            "Constant_function_market_maker",
            "Blockchain",
            "Ethereum",
            "Stablecoin",
        ),
    },
    "nft-tokens": {
        "tags": ["nft", "non-fungible token", "erc-721 token", "erc-1155"],
        "license": CC_BY_SA + " / CC-BY-4.0 (ethereum.org)",
        "pages": wiki("Non-fungible_token", "ERC-721", "Ethereum", "Smart_contract")
        + [
            "https://ethereum.org/en/developers/docs/standards/tokens/erc-721/",
            "https://ethereum.org/en/developers/docs/standards/tokens/erc-1155/",
        ],
    },
    "ipfs": {
        "tags": ["ipfs", "content addressing", "distributed hash table", "ipns"],
        "license": CC_BY_SA + " / CC-BY-4.0 (ipfs docs)",
        "pages": wiki(
            "InterPlanetary_File_System",
            "Content-addressable_storage",
            "Distributed_hash_table",
        )
        + [
            "https://docs.ipfs.tech/concepts/content-addressing/",
            "https://docs.ipfs.tech/concepts/dht/",
            "https://docs.ipfs.tech/concepts/ipns/",
        ],
    },
    "solana-blockchain": {
        "tags": ["solana", "sol cryptocurrency", "proof of history", "solana validator"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Solana_(blockchain_platform)",
            "Proof_of_stake",
            "Blockchain",
            "Cryptocurrency",
            "Smart_contract",
            "Digital_currency",
        ),
    },
    "polkadot": {
        "tags": ["polkadot", "dot cryptocurrency", "parachain", "relay chain"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Polkadot_(blockchain_platform)",
            "Blockchain",
            "Proof_of_stake",
            "Cryptocurrency",
            "Smart_contract",
            "Digital_currency",
        ),
    },
    "cosmos-network": {
        "tags": ["cosmos network", "atom cryptocurrency", "tendermint", "inter-blockchain communication"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Cosmos_(network)",
            "Blockchain",
            "Proof_of_stake",
            "Byzantine_fault",
            "Cryptocurrency",
            "Smart_contract",
        ),
    },
    "zk-snarks": {
        "tags": ["zk-snark", "zksnark", "succinct proof", "zcash privacy"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Non-interactive_zero-knowledge_proof",
            "Zcash",
            "Cryptographic_hash_function",
            "Public-key_cryptography",
            "Blockchain",
            "Monero",
        ),
    },
    "zero-knowledge-proofs": {
        "tags": ["zero-knowledge proof", "zkp", "zk rollup", "prover verifier"],
        "license": CC_BY_SA + " / CC-BY-4.0 (ethereum.org)",
        "pages": wiki(
            "Zero-knowledge_proof",
            "Zcash",
            "Public-key_cryptography",
            "Cryptographic_hash_function",
            "Monero",
        )
        + [
            "https://ethereum.org/en/developers/docs/scaling/zk-rollups/",
        ],
    },
    "layer2-rollups": {
        "tags": ["layer 2 rollup", "optimistic rollup", "zk rollup", "data availability"],
        "license": CC_BY_SA + " / CC-BY-4.0 (ethereum.org)",
        "pages": wiki("Ethereum", "Blockchain", "Bitcoin_scalability")
        + [
            "https://ethereum.org/en/developers/docs/scaling/",
            "https://ethereum.org/en/developers/docs/scaling/optimistic-rollups/",
            "https://ethereum.org/en/developers/docs/scaling/zk-rollups/",
        ],
    },
    "ethereum-virtual-machine": {
        "tags": ["evm", "ethereum virtual machine", "evm opcode", "evm bytecode"],
        "license": CC_BY_SA + " / CC-BY-4.0 (ethereum.org)",
        "pages": wiki("Ethereum", "Smart_contract", "Solidity", "Application_binary_interface")
        + [
            "https://ethereum.org/en/developers/docs/evm/",
            "https://ethereum.org/en/developers/docs/evm/opcodes/",
        ],
    },
    "gas-fees": {
        "tags": ["gas", "gas fee", "gas limit", "transaction fee"],
        "license": CC_BY_SA + " / CC-BY-4.0 (ethereum.org)",
        "pages": wiki("Ethereum", "Smart_contract", "Blockchain", "Front_running")
        + [
            "https://ethereum.org/en/developers/docs/gas/",
            "https://ethereum.org/en/developers/docs/transactions/",
        ],
    },
    "crypto-wallets": {
        "tags": ["crypto wallet", "cryptocurrency wallet", "private key", "seed phrase", "mnemonic"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Cryptocurrency_wallet",
            "Public-key_cryptography",
            "Mnemonic",
            "Coinbase",
            "Blockchain.com",
            "Bitcoin",
        ),
    },
    "dao-governance": {
        "tags": ["dao", "dao governance", "on-chain voting", "the dao"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Decentralized_autonomous_organization",
            "The_DAO",
            "Smart_contract",
            "Ethereum",
            "Blockchain",
            "Tokenomics",
        ),
    },
    "blockchain-consensus": {
        "tags": ["blockchain consensus", "byzantine fault", "consensus mechanism", "distributed ledger"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Consensus_(computer_science)",
            "Byzantine_fault",
            "Proof_of_work",
            "Proof_of_stake",
            "Blockchain",
            "Peercoin",
        ),
    },
    "tokenomics": {
        "tags": ["tokenomics", "token supply", "initial coin offering", "token distribution"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Tokenomics",
            "Initial_coin_offering",
            "Security_token_offering",
            "Cryptocurrency",
            "Digital_currency",
            "Stablecoin",
        ),
    },
    "stablecoins": {
        "tags": ["stablecoin", "tether usdt", "dai stablecoin", "central bank digital currency"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Stablecoin",
            "Tether_(cryptocurrency)",
            "Dai_(cryptocurrency)",
            "Central_bank_digital_currency",
            "Cryptocurrency",
            "Digital_currency",
        ),
    },
    "cryptocurrency": {
        "tags": ["cryptocurrency", "digital currency", "altcoin", "crypto asset"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Cryptocurrency",
            "Digital_currency",
            "Bitcoin",
            "Litecoin",
            "Dash_(cryptocurrency)",
            "Cryptocurrency_and_crime",
        ),
    },
    "blockchain-mining": {
        "tags": ["crypto mining", "mining pool", "asic mining", "mining hardware"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Mining_pool",
            "Application-specific_integrated_circuit",
            "Proof_of_work",
            "Environmental_impact_of_bitcoin",
            "Renewable_energy",
            "Bitcoin",
        ),
    },
    "blockchain-scalability": {
        "tags": ["blockchain scalability", "throughput scaling", "layer 2 scaling", "scalability trilemma"],
        "license": CC_BY_SA + " / CC-BY-4.0 (ethereum.org)",
        "pages": wiki("Bitcoin_scalability", "Lightning_Network", "SegWit", "Blockchain")
        + [
            "https://ethereum.org/en/developers/docs/scaling/",
            "https://ethereum.org/en/developers/docs/data-availability/",
        ],
    },
    "sidechains": {
        "tags": ["sidechain", "pegged chain", "two-way peg", "child chain"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Blockchain",
            "Bitcoin_scalability",
            "Polkadot_(blockchain_platform)",
            "Cosmos_(network)",
            "Smart_contract",
            "Fork_(blockchain)",
        ),
    },
    "atomic-swaps": {
        "tags": ["atomic swap", "cross-chain swap", "hash time-locked contract", "trustless exchange"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Cryptocurrency",
            "Smart_contract",
            "Lightning_Network",
            "Blockchain",
            "Litecoin",
            "Public-key_cryptography",
        ),
    },
    "blockchain-oracles": {
        "tags": ["blockchain oracle", "chainlink oracle", "price feed", "off-chain data"],
        "license": CC_BY_SA + " / CC-BY-4.0 (ethereum.org)",
        "pages": wiki(
            "Blockchain_oracle",
            "Chainlink_(blockchain_oracle)",
            "Smart_contract",
            "Ethereum",
            "Decentralized_finance",
        )
        + [
            "https://ethereum.org/en/developers/docs/oracles/",
        ],
    },
    "erc-token-standards": {
        "tags": ["erc-20", "erc token standard", "erc-721", "erc-1155", "fungible token"],
        "license": CC_BY_SA + " / CC-BY-4.0 (ethereum.org)",
        "pages": wiki("Non-fungible_token", "Smart_contract", "Ethereum")
        + [
            "https://ethereum.org/en/developers/docs/standards/tokens/",
            "https://ethereum.org/en/developers/docs/standards/tokens/erc-20/",
            "https://ethereum.org/en/developers/docs/standards/tokens/erc-1155/",
        ],
    },
    "maximal-extractable-value": {
        "tags": ["mev", "maximal extractable value", "transaction ordering", "sandwich attack"],
        "license": CC_BY_SA + " / CC-BY-4.0 (ethereum.org)",
        "pages": wiki(
            "Front_running",
            "Proof_of_stake",
            "Ethereum",
            "Decentralized_finance",
            "Uniswap",
        )
        + [
            "https://ethereum.org/en/developers/docs/mev/",
        ],
    },
    "liquidity-pools": {
        "tags": ["liquidity pool", "automated market maker", "uniswap pool", "impermanent loss"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Decentralized_finance",
            "Constant_function_market_maker",
            "Uniswap",
            "Stablecoin",
            "Ethereum",
            "Smart_contract",
        ),
    },
    "cross-chain-bridge": {
        "tags": ["cross-chain bridge", "blockchain bridge", "wrapped asset", "chain interoperability"],
        "license": CC_BY_SA + " / CC-BY-4.0 (ethereum.org)",
        "pages": wiki(
            "Chainlink_(blockchain_oracle)",
            "Cosmos_(network)",
            "Polkadot_(blockchain_platform)",
            "Blockchain",
            "Avalanche_(blockchain_platform)",
        )
        + [
            "https://ethereum.org/en/developers/docs/bridges/",
        ],
    },
    "hyperledger-fabric": {
        "tags": ["hyperledger fabric", "permissioned blockchain", "enterprise ledger", "chaincode"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Hyperledger",
            "Blockchain",
            "Smart_contract",
            "Consensus_(computer_science)",
            "Byzantine_fault",
            "Distributed_hash_table",
        ),
    },
    "avalanche-blockchain": {
        "tags": ["avalanche blockchain", "avax cryptocurrency", "subnet", "snowman consensus"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Avalanche_(blockchain_platform)",
            "Proof_of_stake",
            "Smart_contract",
            "Blockchain",
            "Cryptocurrency",
            "Consensus_(computer_science)",
        ),
    },
    "cardano": {
        "tags": ["cardano", "ada cryptocurrency", "ouroboros protocol", "proof-of-stake staking"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Cardano_(blockchain_platform)",
            "Ouroboros_(protocol)",
            "Proof_of_stake",
            "Blockchain",
            "Cryptocurrency",
            "Smart_contract",
        ),
    },
    "monero-privacy": {
        "tags": ["monero", "xmr cryptocurrency", "ring signature", "privacy coin"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Monero",
            "Ring_signature",
            "Zcash",
            "Public-key_cryptography",
            "Cryptocurrency",
            "Digital_currency",
        ),
    },
    "decentralized-identity": {
        "tags": ["decentralized identity", "decentralized identifier", "verifiable credentials", "self-sovereign identity"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Self-sovereign_identity",
            "Decentralized_identifier",
            "Verifiable_credentials",
            "Public-key_cryptography",
            "Blockchain",
            "Smart_contract",
        ),
    },
    "blockchain-sharding": {
        "tags": ["blockchain sharding", "shard chain", "state sharding", "horizontal partitioning"],
        "license": CC_BY_SA + " / CC-BY-4.0 (ethereum.org)",
        "pages": wiki("Shard_(database_architecture)", "Ethereum", "Blockchain", "Bitcoin_scalability")
        + [
            "https://ethereum.org/en/developers/docs/nodes-and-clients/",
            "https://ethereum.org/en/developers/docs/data-availability/",
        ],
    },
    "account-abstraction": {
        "tags": ["account abstraction", "smart contract wallet", "erc-4337", "user operation"],
        "license": CC_BY_SA + " / CC-BY-4.0 (ethereum.org)",
        "pages": wiki("Cryptocurrency_wallet", "Smart_contract", "Ethereum", "Public-key_cryptography")
        + [
            "https://ethereum.org/en/developers/docs/accounts/",
            "https://ethereum.org/en/developers/docs/smart-contracts/",
        ],
    },
}
