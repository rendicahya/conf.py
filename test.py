from config_py import Config

toml = Config.load_toml("config.toml")

print(toml.title)
print(toml.images[0])
