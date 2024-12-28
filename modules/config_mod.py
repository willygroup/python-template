import json
import os
import sqlite3
import string
import sys
import traceback
from types import SimpleNamespace


class Config:

    def create_json_default_config(self):
        config_data = {
            "language": "en",
            "datas": {
                "data1": 100,
                "data2": 200
            }
        }
        try:
            write_file = open(self.config_file, mode="w", encoding="utf-8")
        except:
            return False
        else:
            json.dump(config_data, write_file)
            return True

    def load_config(self):

        try:
            f = open(self.config_file, 'r')
        except FileNotFoundError:
            # Create the default config
            self.create_json_default_config()
        except Exception as e:
            # print a not handled exception
            print(traceback.format_exception(*sys.exc_info()))
            raise  # reraises the exception
        else:
            data = f.read()
            self.data = json.loads(
                data, object_hook=lambda d: SimpleNamespace(**d))

    def __init__(self, filename: str = "") -> None:
        # Load the configuration from file or create a new standard one
        if filename.strip() == "":
            self.config_file = os.path.join("files", "config.json")
        else:
            self.config_file = os.path.join("files", filename)
        self.load_config()
        # self.data =
