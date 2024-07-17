import redis

from src.settings import config


class RedisClient:
    def __init__(self) -> None:
        self.pool = redis.ConnectionPool(
            host=config.REDIS_HOST,
            port=config.REDIS_PORT,
            db=0,
        )

    def set_connection(self) -> None:
        self._conn = redis.Redis(connection_pool=self.pool)

    @property
    def connection(self) -> "redis.Redis":
        if not hasattr(self, "_conn"):
            self.set_connection()
        return self._conn
