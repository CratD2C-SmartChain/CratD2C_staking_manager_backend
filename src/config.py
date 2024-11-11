import os
from dataclasses import dataclass

import yaml
from marshmallow_dataclass import class_schema


@dataclass
class Blockchain:
    MIN_VALIDATOR_AMOUNT: int
    MIN_VALIDATOR_COMMISSION: int
    MAX_VALIDATOR_COMMISSION: int
    PROVIDER: str
    STAKING_CONTRACT_ADDRESS: str
    BLOCK_REFRESH_TIME: int
    EPOCH_LEN: int


@dataclass
class Config:
    ALLOWED_HOSTS: list
    SECRET_KEY: str
    DEBUG: bool
    SWAGGER_TITLE: str
    SWAGGER_DESCRIPTION: str
    API_KEY: str
    WALLET_CONNECT_MESSAGE_EXPIRATION_SECONDS: int
    BLOCKCHAIN: Blockchain
    

config_path = "/../config.yaml"
if os.getenv("IS_TEST", False):
    config_path = "../config.example.yaml"

with open(os.path.dirname(__file__) + config_path) as f:
    config_data = yaml.safe_load(f)

config: Config = class_schema(Config)().load(config_data)
