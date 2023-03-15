# conf.py

Easy configuration for Python with dot notation. Currently supports JSON and TOML.

## Installation
```
pip install conf.py
```

## Usage
```python
from conf_py import Conf

toml = Conf.load_toml("conf.toml")

print(toml.title)
print(toml.images[0])
```