import os
import logging
from logging.config import dictConfig
import yaml

_CONFIG = r"/home/andrew/projects/tick/config.yaml"
env = {}
_MAPPINGS = {
    ("TICKSPOT_USERNAME", "tickspot.username"),
    ("TICKSPOT_PASSWORD", "tickspot.password"),
}

def yaml_parse(config, key_path):
    """
    Parses a yaml config (dictionary) to get the value targeted
    by key_path, using 'dot notation'.

    :param dict config: the dict representing the yaml config
    :param key_path str: the path of the value to retrieve

    :return value|None: whatever value is to be returned, or None if not found
    """
    _value = config.get(key_path[0])
    if _value is None:
        return None
    elif isinstance(_value, dict):
        return yaml_parse(_value, key_path[1:])
    else:
        return _value


if _CONFIG:
    with open(_CONFIG, "r") as conf:
        config = yaml.safe_load(conf.read())
        for env_key, yaml_key in _MAPPINGS:
            if "." in yaml_key:
                key_path = yaml_key.split(".")
                value = yaml_parse(config, key_path)
                if value is not None:
                    env.update({env_key: yaml_parse(config, key_path)})
            else:
                if config.get(yaml_key) is not None:
                    env.update({env_key: config.get(yaml_key)})

        # Logging Config
        logging_config = {
            "version": 1,
            "formatters": {
                "standard": {"format": "%(asctime)s %(pathname)s %(levelname)s %(message)s"}
            },
            "handlers": {
                "error": {
                    "class": "logging.StreamHandler",
                    "formatter": "standard",
                    "level": logging.ERROR,
                },
                "info": {
                    "class": "logging.StreamHandler",
                    "formatter": "standard",
                    "level": logging.INFO,
                },
            },
            "loggers": {
                "tasks": {"handlers": ["error", "info"], "level": logging.INFO, "propagate": True}
            },
        }
        dictConfig(logging_config)