from convigure import Conf


class TestTOML:
    @classmethod
    def setup_class(self):
        self.toml = Conf.load_json("conf.json")

    def test_int(self):
        assert self.toml.id == 8

    def test_str(self):
        assert self.toml.title == "Microsoft Surface Laptop 4"

    def test_float(self):
        assert self.toml.discountPercentage == 10.23

    def test_list(self):
        assert self.toml.images[0] == "https://i.dummyjson.com/data/products/8/1.jpg"

    def test_list_size(self):
        assert len(self.toml.images) == 5
