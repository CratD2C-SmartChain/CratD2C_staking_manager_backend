import time

import redis
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

from src.settings import config


class RedisClient:
    def __init__(self) -> None:
        self.pool = redis.ConnectionPool(
            host=config.REDIS_HOST,
            port=config.REDIS_PORT,
            db=0,
        )
        self._conn = None

    def set_connection(self) -> None:
        self._conn = redis.Redis(connection_pool=self.pool)

    @property
    def connection(self) -> "redis.Redis":
        if self._conn is None:
            self.set_connection()
        return self._conn


class Network:
    def __init__(self) -> None:
        self._rpc = None
        self._block_number = None
        self._block_time = None

    @property
    def rpc(self):
        if self._rpc is None:
            self._rpc = Web3(HTTPProvider(config.BLOCKCHAIN.PROVIDER))
            self._rpc.middleware_onion.inject(geth_poa_middleware, layer=0)
        return self._rpc

    def check_balance(self, address) -> bool:
        return self.rpc.eth.get_balance(address) > config.BLOCKCHAIN.MIN_VALIDATOR_AMOUNT

    @property
    def block_number(self) -> int:
        if self._block_number is None or (time.time() - self._block_time) > config.BLOCKCHAIN.BLOCK_REFRESH_TIME:
            self._block_number = self.rpc.eth.block_number
            self._block_time = int(time.time())
        return self._block_number


network = Network()
