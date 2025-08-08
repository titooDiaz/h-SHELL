from core.config_parser import load_main_config
from commands import generate_project
from commands.ghost_display import main

DEFAULT_COMMANDS = {
    "generate-project": generate_project,
    "version": main,
}

def get_command_aliases():
    config = load_main_config()
    aliases = dict(config.items("commands"))
    resolved = {}

    for real_name, module in DEFAULT_COMMANDS.items():
        alias = aliases.get(real_name, real_name)
        resolved[alias] = module

    return resolved
