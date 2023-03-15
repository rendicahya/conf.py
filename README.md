# config.py

Easy configuration for Python with dot notation. Currently supports JSON and TOML.

## Installation
```
pip install config.py
```

## Usage
```python
from config_py import Config

toml = Config.load_toml("config.toml")

print(toml.title)
print(toml.images[0])
```