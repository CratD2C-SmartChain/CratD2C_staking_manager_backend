from src.utilities import network, config


class IntervalProcessor:

    def __init__(self):
        self.network = network

    def get_interval(self):
        last_block = self.network.rpc.eth.block_number
        current_checkpoint_block = last_block - last_block % config.BLOCKCHAIN.EPOCH_LEN
        if current_checkpoint_block < config.BLOCKCHAIN.EPOCH_LEN:
            return 0
        previous_checkpoint_block = last_block - config.BLOCKCHAIN.EPOCH_LEN
        current_checkpoint_ts = self.network.rpc.eth.get_block(current_checkpoint_block).timestamp
        previous_checkpoint_ts = self.network.rpc.eth.get_block(previous_checkpoint_block).timestamp
        return current_checkpoint_ts - previous_checkpoint_ts


i_processor = IntervalProcessor()
