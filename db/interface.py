from abc import ABC, abstractmethod
from typing import List, Optional

class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self): pass
    @abstractmethod
    def disconnect(self): pass
    @abstractmethod
    def insert(self, table: str, data: dict, version: Optional[int] = 1): pass
    @abstractmethod
    def select(self, table: str, conditions: dict, version: Optional[int] = None) -> list: pass