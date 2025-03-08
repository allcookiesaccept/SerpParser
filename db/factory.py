from db.interface import DatabaseInterface
from db.biqquery import BigQueryDB
from db.mongodb import MongoDBAtlas
from db.sqlite import SQLiteDB



class DatabaseFactory:
    @staticmethod
    def create_db(db_type: str, config: dict) -> DatabaseInterface:
        if db_type == "sqlite":
            return SQLiteDB(config)
        elif db_type == "mongo":
            return MongoDBAtlas(config)
        elif db_type == "bigquery":
            return BigQueryDB(config)
        raise ValueError(f"Unsupported database type: {db_type}")