# Convigure

Easy configuration for Python with dot notation. Currently supports JSON and TOML.

## Installation
```
pip install conviguration
```

## Usage
```python
from conviguration import Conf

toml = Conf.load_toml("conf.toml")

print(toml.title)
print(toml.images[0])
```