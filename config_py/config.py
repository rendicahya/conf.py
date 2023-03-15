import json
import toml


class DotDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class Config(object):
    @staticmethod
    def parse(data):
        if type(data) is dict:
            return Config.parse_dict(data)
        elif type(data) is list:
            return Config.parse_list(data)
        else:
            return data

    @staticmethod
    def parse_dict(data: dict) -> DotDict:
        config = DotDict()

        for key, value in data.items():
            config[key] = Config.parse(value)

        return config

    @staticmethod
    def parse_list(data: list):
        return [Config.parse(item) for item in data]

    @staticmethod
    def load_json(path: str) -> DotDict:
        with open(path, "r") as f:
            result = Config.parse(json.loads(f.read()))

        return result

    @staticmethod
    def load_toml(path: str):
        with open(path, "r") as f:
            result = Config.parse(toml.load(f))

        return result
