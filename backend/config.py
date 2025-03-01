from converters import convert_string_to_bool
from filesystem import get_current_dir, get_parent_dir
from dataclasses import dataclass
from dotenv import load_dotenv
import os
from pathlib import Path

ENV_FILE = os.path.join(get_current_dir(__file__), ".env")

load_dotenv(ENV_FILE)

@dataclass
class AppSettings:

    data_dir_root: str = None
    db_filename: str = None
    db_filepath: str = None
    db_connection_string: str = None
    refresh_data: bool = False

    def __init__(self):
        self.data_dir_root = os.path.join(get_parent_dir(__file__), "data")
        self.db_filename = os.getenv("DB.FILENAME")
        self.db_filepath = os.path.join(get_current_dir(__file__), self.db_filename)
        self.db_connection_string = f"sqlite:///{self.db_filepath}"
        self.refresh_data = convert_string_to_bool(os.getenv("REFRESH.DATA"))