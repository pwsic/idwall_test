import os

import yaml

_cache = {}


def _deep_get(_dict, keys):
    for key in keys:
        if key not in _dict:
            return None
        if isinstance(_dict, dict):
            _dict = _dict[key]
    return _dict


def get(path, env=None):
    global _cache
    if not _cache:
        with open("settings.yaml") as yaml_file:
            _cache = yaml.load(yaml_file, Loader=yaml.FullLoader)
    keys = path.split(".")
    if keys[0] != "default":
        env = env or os.environ.get("APPLICATION_ENV", "development")
        keys.insert(0, env)
    return _deep_get(_cache, keys)
