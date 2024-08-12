from web3 import Web3

from src.abi import staking_abi
from src.utilities import config, network


class ContractProcessor:

    def __init__(self, address, abi, rpc: Web3):
        self.abi = abi
        self.rpc = rpc
        self.address = self.rpc.to_checksum_address(address)
        self._contract = None

    @property
    def contract(self):
        if self._contract is None:
            self._contract = self.rpc.eth.contract(abi=self.abi, address=self.address)
        return self._contract

    def create_call_data(self, function_name, params):
        function = getattr(self.contract.functions, function_name)
        return function(*params)

    def deposit_as_validator(self, commission, amount, address):
        cd = self.create_call_data("depositAsValidator", [commission])
        tx = cd.build_transaction(self.get_tx_params(amount, address))
        return tx

    def get_tx_params(self, amount, address) -> dict:
        data = {
            "from": address,
            "gasPrice": self.rpc.eth.gas_price,
            "chainId": self.rpc.eth.chain_id,
            "nonce": self.rpc.eth.get_transaction_count(address),
            "gas": 1000000,
            "value": amount,
        }
        return data

    def get_block_from_tx(self, tx_hash, address_from):
        tx = self.rpc.eth.get_transaction(tx_hash)
        if tx["from"] == address_from:
            return tx["blockNumber"]
        return None

    def get_active_validators_info(self) -> tuple:
        validators, amounts = self.contract.functions.getActiveValidators().call()
        amounts = [a[0] + a[1] for a in amounts]
        return validators, amounts

    def get_stopped_validators_info(self) -> set | list | None:
        validators, _ = self.contract.functions.getStoppedValidators().call()
        return set(validators) if validators else None

    def is_validator_active(self, address):
        address = self.rpc.to_checksum_address(address)
        is_validator = self.contract.functions.isValidator(address).call()
        return is_validator


contract_processor = ContractProcessor(
    abi=staking_abi,
    rpc=network.rpc,
    address=config.BLOCKCHAIN.STAKING_CONTRACT_ADDRESS,
)
