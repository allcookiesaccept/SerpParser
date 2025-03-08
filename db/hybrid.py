from db.interface import DatabaseInterface
from typing import List, Optional
from db.factory import DatabaseFactory
from utils.logger import Logger, logger
class HybridDB:
    def __init__(self, config: dict, logger: Logger = logger):
        self.logger: Logger = logger
        self.relational_dbs: List[DatabaseInterface] = []
        self.document_dbs: List[DatabaseInterface] = []
        self.version = 1

        self._initialize_dbs(config["databases"])

    def _initialize_dbs(self, db_configs: dict):
        for db_type, configs in db_configs.items():
            for db_name, db_config in configs.items():
                db_instance = DatabaseFactory.create_db(db_type, db_config)
                if db_type in {"sqlite", "bigquery"}:  # Реляционные
                    self.relational_dbs.append(db_instance)
                elif db_type == "mongo":  # Документные
                    self.document_dbs.append(db_instance)
                self.logger.info(f"Initialized {db_type} database: {db_name}")

        if not self.relational_dbs:
            self.logger.error("No relational databases configured")
        if not self.document_dbs:
            self.logger.error("No document databases configured")

    def insert(self, table: str, data: dict):
        for db in self.relational_dbs:
            db.insert(table, data["relational"], self.version)
        for db in self.document_dbs:
            db.insert(table, data["document"], self.version)

    def update_version(self, new_version: int):
        self.version = new_version