import os
import yaml
from typing import Dict, Any


class ConfigLoader:
    def __init__(self, config_path: str = "config.yaml"):
        self.config_path = config_path

    def load_config(self) -> Dict[str, Any]:
        with open(self.config_path, "r") as f:
            config = yaml.safe_load(f)

        # Подстановка переменных окружения
        for db_type, db_configs in config["databases"].items():
            for db_name, db_data in db_configs.items():
                for key, value in db_data.items():
                    if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
                        env_var = value[2:-1]
                        db_data[key] = os.getenv(env_var, value)  # Значение из .env или исходное
        return config