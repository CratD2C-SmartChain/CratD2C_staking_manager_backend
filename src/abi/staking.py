staking_abi = [
    {
        "inputs": [],
        "name": "AccessControlBadConfirmation",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            },
            {
                "internalType": "bytes32",
                "name": "neededRole",
                "type": "bytes32"
            }
        ],
        "name": "AccessControlUnauthorizedAccount",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InvalidInitialization",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "NotInitializing",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ReentrancyGuardReentrantCall",
        "type": "error"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "delegator",
                "type": "address"
            }
        ],
        "name": "DelegatorCalledForWithdraw",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "delegator",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "DelegatorClaimed",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "delegator",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "validator",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "DelegatorDeposited",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "delegator",
                "type": "address"
            }
        ],
        "name": "DelegatorRevived",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "delegator",
                "type": "address"
            }
        ],
        "name": "DelegatorWithdrawed",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint64",
                "name": "version",
                "type": "uint64"
            }
        ],
        "name": "Initialized",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            },
            {
                "indexed": True,
                "internalType": "bytes32",
                "name": "previousAdminRole",
                "type": "bytes32"
            },
            {
                "indexed": True,
                "internalType": "bytes32",
                "name": "newAdminRole",
                "type": "bytes32"
            }
        ],
        "name": "RoleAdminChanged",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "account",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "sender",
                "type": "address"
            }
        ],
        "name": "RoleGranted",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "account",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "sender",
                "type": "address"
            }
        ],
        "name": "RoleRevoked",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "validator",
                "type": "address"
            }
        ],
        "name": "ValidatorCalledForWithdraw",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "validator",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "ValidatorClaimed",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "validator",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "commission",
                "type": "uint256"
            }
        ],
        "name": "ValidatorDeposited",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "validator",
                "type": "address"
            }
        ],
        "name": "ValidatorRevived",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "validator",
                "type": "address"
            }
        ],
        "name": "ValidatorWithdrawed",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "DEFAULT_ADMIN_ROLE",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "DISTRIBUTOR_ROLE",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "PRECISION",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "SWAP_ROLE",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "YEAR_DURATION",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "validator",
                "type": "address"
            }
        ],
        "name": "claimAsDelegatorPerValidator",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "claimAsValidator",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "validator",
                "type": "address"
            }
        ],
        "name": "delegatorCallForWithdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "delegator",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "validator",
                "type": "address"
            }
        ],
        "name": "delegatorEarnedPerValidator",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "fixedReward",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "variableReward",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "delegator",
                "type": "address"
            },
            {
                "internalType": "address[]",
                "name": "validatorsArr",
                "type": "address[]"
            }
        ],
        "name": "delegatorEarnedPerValidators",
        "outputs": [
            {
                "internalType": "uint256[]",
                "name": "fixedRewards",
                "type": "uint256[]"
            },
            {
                "internalType": "uint256[]",
                "name": "variableRewards",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "validator",
                "type": "address"
            }
        ],
        "name": "depositAsDelegator",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "commission",
                "type": "uint256"
            }
        ],
        "name": "depositAsValidator",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "sender",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "commission",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "vestingEnd",
                "type": "uint256"
            }
        ],
        "name": "depositForValidator",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address[]",
                "name": "validators",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "amounts",
                "type": "uint256[]"
            }
        ],
        "name": "distributeRewards",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "forFixedReward",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getActiveValidators",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "validators",
                "type": "address[]"
            },
            {
                "internalType": "uint256[3][]",
                "name": "amounts",
                "type": "uint256[3][]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "delegator",
                "type": "address"
            }
        ],
        "name": "getDelegatorInfo",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "validatorsArr",
                "type": "address[]"
            },
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "amount",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "storedValidatorAcc",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "calledForWithdraw",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "lastClaim",
                        "type": "uint256"
                    },
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "apr",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "lastUpdate",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "fixedReward",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "totalClaimed",
                                "type": "uint256"
                            }
                        ],
                        "internalType": "struct CRATStakeManager.FixedReward",
                        "name": "fixedReward",
                        "type": "tuple"
                    },
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "variableReward",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "totalClaimed",
                                "type": "uint256"
                            }
                        ],
                        "internalType": "struct CRATStakeManager.VariableReward",
                        "name": "variableReward",
                        "type": "tuple"
                    }
                ],
                "internalType": "struct CRATStakeManager.DelegatorPerValidatorInfo[]",
                "name": "delegatorPerValidatorArr",
                "type": "tuple[]"
            },
            {
                "internalType": "uint256[]",
                "name": "withdrawAvailable",
                "type": "uint256[]"
            },
            {
                "internalType": "uint256[]",
                "name": "claimAvailable",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "validator",
                "type": "address"
            }
        ],
        "name": "getDelegatorsInfoPerValidator",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "delegators",
                "type": "address[]"
            },
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "amount",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "storedValidatorAcc",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "calledForWithdraw",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "lastClaim",
                        "type": "uint256"
                    },
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "apr",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "lastUpdate",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "fixedReward",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "totalClaimed",
                                "type": "uint256"
                            }
                        ],
                        "internalType": "struct CRATStakeManager.FixedReward",
                        "name": "fixedReward",
                        "type": "tuple"
                    },
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "variableReward",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "totalClaimed",
                                "type": "uint256"
                            }
                        ],
                        "internalType": "struct CRATStakeManager.VariableReward",
                        "name": "variableReward",
                        "type": "tuple"
                    }
                ],
                "internalType": "struct CRATStakeManager.DelegatorPerValidatorInfo[]",
                "name": "delegatorPerValidatorArr",
                "type": "tuple[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            }
        ],
        "name": "getRoleAdmin",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getStoppedValidators",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "validators",
                "type": "address[]"
            },
            {
                "internalType": "uint256[3][]",
                "name": "amounts",
                "type": "uint256[3][]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "validator",
                "type": "address"
            }
        ],
        "name": "getValidatorInfo",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "amount",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "commission",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "lastClaim",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "calledForWithdraw",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "vestingEnd",
                        "type": "uint256"
                    },
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "apr",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "lastUpdate",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "fixedReward",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "totalClaimed",
                                "type": "uint256"
                            }
                        ],
                        "internalType": "struct CRATStakeManager.FixedReward",
                        "name": "fixedReward",
                        "type": "tuple"
                    },
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "variableReward",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "totalClaimed",
                                "type": "uint256"
                            }
                        ],
                        "internalType": "struct CRATStakeManager.VariableReward",
                        "name": "variableReward",
                        "type": "tuple"
                    },
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "lastSlash",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "potentialPenalty",
                                "type": "uint256"
                            }
                        ],
                        "internalType": "struct CRATStakeManager.SlashPenaltyCalculation",
                        "name": "penalty",
                        "type": "tuple"
                    },
                    {
                        "internalType": "uint256",
                        "name": "delegatedAmount",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "stoppedDelegatedAmount",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "delegatorsAcc",
                        "type": "uint256"
                    },
                    {
                        "internalType": "address[]",
                        "name": "delegators",
                        "type": "address[]"
                    },
                    {
                        "internalType": "uint256",
                        "name": "withdrawAvailable",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "claimAvailable",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct CRATStakeManager.ValidatorInfoView",
                "name": "info",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "grantRole",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "hasRole",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_distributor",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_receiver",
                "type": "address"
            }
        ],
        "name": "initialize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "isDelegator",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "isValidator",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "callerConfirmation",
                "type": "address"
            }
        ],
        "name": "renounceRole",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "validator",
                "type": "address"
            }
        ],
        "name": "restakeAsDelegator",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "restakeAsValidator",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "validator",
                "type": "address"
            }
        ],
        "name": "reviveAsDelegator",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "reviveAsValidator",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "revokeRole",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "setDelegatorsAPR",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "setDelegatorsClaimCooldown",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "setDelegatorsMinimum",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "setDelegatorsPercToSlash",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "setDelegatorsWithdrawCooldown",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "receiver",
                "type": "address"
            }
        ],
        "name": "setSlashReceiver",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "setValidatorsAPR",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "setValidatorsAmountToSlash",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "setValidatorsClaimCooldown",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "setValidatorsLimit",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "setValidatorsMinimum",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "setValidatorsWithdrawCooldown",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "settings",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "validatorsLimit",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "slashReceiver",
                "type": "address"
            },
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "apr",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "toSlash",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "minimumThreshold",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "claimCooldown",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "withdrawCooldown",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct CRATStakeManager.RoleSettings",
                "name": "validatorsSettings",
                "type": "tuple"
            },
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "apr",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "toSlash",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "minimumThreshold",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "claimCooldown",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "withdrawCooldown",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct CRATStakeManager.RoleSettings",
                "name": "delegatorsSettings",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address[]",
                "name": "validators",
                "type": "address[]"
            }
        ],
        "name": "slash",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "stoppedDelegatorsPool",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "stoppedValidatorsPool",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes4",
                "name": "interfaceId",
                "type": "bytes4"
            }
        ],
        "name": "supportsInterface",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "delegator",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "validator",
                "type": "address"
            }
        ],
        "name": "totalDelegatorRewardPerValidator",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "fixedReward",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "variableReward",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "totalDelegatorsPool",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "totalDelegatorsRewards",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "fixedReward",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "variableReward",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "validator",
                "type": "address"
            }
        ],
        "name": "totalValidatorReward",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "fixedReward",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "variableReward",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "totalValidatorsPool",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "totalValidatorsRewards",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "fixedReward",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "variableReward",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "validatorCallForWithdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "validator",
                "type": "address"
            }
        ],
        "name": "validatorEarned",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "fixedReward",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "variableReward",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "validator",
                "type": "address"
            }
        ],
        "name": "withdrawAsDelegator",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "withdrawAsValidator",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "withdrawExcessFixedReward",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "validator",
                "type": "address"
            },
            {
                "internalType": "address[]",
                "name": "delegators",
                "type": "address[]"
            }
        ],
        "name": "withdrawForDelegators",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "validator",
                "type": "address"
            }
        ],
        "name": "withdrawForValidator",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "stateMutability": "payable",
        "type": "receive"
    }
]
