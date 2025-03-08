from db.interface import DatabaseInterface
from typing import List, Optional


class SQLiteDB(DatabaseInterface):
    def __init__(self, config: dict):
        self.path = config.get("path")
    def connect(self): pass
    def disconnect(self): pass
    def insert(self, table: str, data: dict, version: Optional[int] = 1): pass
    def select(self, table: str, conditions: dict, version: Optional[int] = None) -> list: pass