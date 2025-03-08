from db.interface import DatabaseInterface
from typing import List, Optional


class MongoDBAtlas(DatabaseInterface):
    def __init__(self, config: dict):
        self.host = config.get("host")
        self.port = config.get("port")
        self.login = config.get("login")
        self.password = config.get("password")
    def connect(self): pass
    def disconnect(self): pass
    def insert(self, table: str, data: dict, version: Optional[int] = 1): pass
    def select(self, table: str, conditions: dict, version: Optional[int] = None) -> list: pass