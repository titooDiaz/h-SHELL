import configparser
from pathlib import Path

CONFIG_PATH = Path(__file__).parents[1] / "config" / "config.wcode"

def load_main_config():
    parser = configparser.RawConfigParser()
    parser.optionxform = str
    parser.read(CONFIG_PATH)
    return parser