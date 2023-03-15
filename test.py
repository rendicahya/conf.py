from convigure import Conf

toml = Conf.load_toml("conf.toml")

print(toml.title)
print(toml.images[0])
