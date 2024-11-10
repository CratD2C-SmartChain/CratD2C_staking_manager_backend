from src.utilities import network, config


class IntervalProcessor:
    def __init__(self):
        self.network = network

    def get_interval(self):
        last_block = self.network.rpc.eth.block_number
        if last_block < 0:
            raise ValueError("Invalid block number received from the network RPC")
        current_checkpoint_block = last_block - last_block % config.BLOCKCHAIN.EPOCH_LEN
        if current_checkpoint_block < config.BLOCKCHAIN.EPOCH_LEN:
            return 0
        previous_checkpoint_block = current_checkpoint_block - config.BLOCKCHAIN.EPOCH_LEN
        current_block_data = self.network.rpc.eth.get_block(current_checkpoint_block)
        previous_block_data = self.network.rpc.eth.get_block(previous_checkpoint_block)
        current_checkpoint_ts = current_block_data.timestamp
        previous_checkpoint_ts = previous_block_data.timestamp
        if current_checkpoint_ts <= 0 or previous_checkpoint_ts <= 0:
            raise ValueError("Invalid timestamps received from the network RPC")
        if current_checkpoint_ts <= previous_checkpoint_ts:
            raise ValueError("Current checkpoint timestamp is earlier than previous checkpoint timestamp")
        return current_checkpoint_ts - previous_checkpoint_ts


i_processor = IntervalProcessor()
