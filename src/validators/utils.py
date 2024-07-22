from web3 import Web3

from src.abi import staking_abi
from src.utilities import config, network


class ContractProcessor:

    def __init__(self, address, abi, rpc: Web3):
        self.abi = abi
        self.rpc = rpc
        self.address = self.rpc.to_checksum_address(address)

    def create_call_data(self, function_name, params):
        contract = self.rpc.eth.contract(abi=self.abi, address=self.address)
        function = getattr(contract.functions, function_name)
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


staking_processor = ContractProcessor(
    abi=staking_abi,
    rpc=network.rpc,
    address=config.BLOCKCHAIN.STAKING_CONTRACT_ADDRESS,
)
