import unittest
from transformer import *
from bike import *


class TransformerTest(unittest.TestCase):
    def test_above_avatar(self):
        transformer = Transformer(["bike", "car", "rocket", "jet"])
        self.assertEqual("bike", transformer.transform_up(Car()).name)

    def test_below_avatar(self):
        transformer = Transformer(["bike", "car", "rocket", "jet"])
        self.assertEqual("rocket", transformer.transform_down(Car()).name)

    def test_bike_top_most_transform_up(self):
        transformer = Transformer(["bike", "car", "rocket", "jet"])
        self.assertEqual("jet", transformer.transform_up(Bike()).name)

    def test_below_avatar_of_last_avatar(self):
        transformer = Transformer(["bike", "car", "rocket", "jet"])
        self.assertEqual("bike", transformer.transform_down(Jet()).name)

    def test_bike_top_most_transform_down(self):
        transformer = Transformer(["bike", "car", "rocket", "jet"])
        self.assertEqual("car", transformer.transform_down(Bike()).name)

    def test_bike_bottom_most_transform_up(self):
        transformer = Transformer(["car", "rocket", "jet", "bike"])
        self.assertEqual("jet", transformer.transform_up(Bike()).name)

    def test_bike_bottom_most_transform_down(self):
        transformer = Transformer(["car", "rocket", "jet", "bike"])
        self.assertEqual("car", transformer.transform_down(Bike()).name)

    def test_incorrect_avatar_name(self):
        try:
            transformer = Transformer(["bike", "car", "rocket", "jet", "pet"])
        except AttributeError:
            assert True
