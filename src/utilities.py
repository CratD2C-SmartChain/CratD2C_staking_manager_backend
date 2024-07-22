import redis
from web3 import Web3, HTTPProvider

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

    @property
    def rpc(self):
        if self._rpc is None:
            self._rpc = Web3(HTTPProvider(config.BLOCKCHAIN.PROVIDER))
        return self._rpc

    def check_balance(self, address) -> bool:
        return self.rpc.eth.get_balance(address) > config.BLOCKCHAIN.MIN_VALIDATOR_AMOUNT


network = Network()
