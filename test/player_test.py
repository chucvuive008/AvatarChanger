import unittest
from player import *
from bike import *
from car import*
from jet import *
from rocket import *
import types
from avatar import *


class PlayerTest(unittest.TestCase):
    def test_Canary(self):
        self.assertTrue(True)

    def test_perform_action_bike(self):
        original_action = Bike.action

        def fake_action(self):
            self.called = True
            original_action(self)

        bike = Bike()
        bike.action = types.MethodType(fake_action, bike)
        player = Player(bike)
        player.perform_action()

        self.assertTrue(bike.called)

    def test_perform_action_car(self):
        original_action = Car.action

        def fake_action(self):
            self.called = True
            original_action(self)

        car = Car()
        car.action = types.MethodType(fake_action, car)
        player = Player(car)
        player.perform_action()

        self.assertTrue(car.called)

    def test_perform_action_jet(self):
        original_action = Jet.action

        def fake_action(self):
            self.called = True
            original_action(self)

        jet = Jet()
        jet.action = types.MethodType(fake_action, jet)
        player = Player(jet)
        player.perform_action()

        self.assertTrue(jet.called)

    def test_perform_action_rocket(self):
        original_action = Rocket.action

        def fake_action(self):
            self.called = True
            original_action(self)

        rocket = Rocket()
        rocket.action = types.MethodType(fake_action, rocket)
        player = Player(rocket)
        player.perform_action()

        self.assertTrue(rocket.called)

    def test_up_from(self):
        transformer = Transformer(["bike", "car", "rocket", "jet"])
        player = Player(Car())
        player.up_from(transformer)

        self.assertEqual("bike", player.current_avatar.name)

    def test_down_from(self):
        transformer = Transformer(["bike", "car", "rocket", "jet"])
        player = Player(Car())
        player.down_from(transformer)

        self.assertEqual("rocket", player.current_avatar.name)

    def test_down_from_then_up_from(self):
        transformer = Transformer(["bike", "car", "rocket", "jet"])
        player = Player(Car())
        player.down_from(transformer)
        player.up_from(transformer)

        self.assertEqual("car", player.current_avatar.name)

    def test_up_from_then_down_from(self):
        transformer = Transformer(["bike", "car", "rocket", "jet"])
        player = Player(Car())
        player.up_from(transformer)
        player.down_from(transformer)

        self.assertEqual("car", player.current_avatar.name)

    def test_up_from_first_avatar(self):
        transformer = Transformer(["bike", "car", "rocket", "jet"])
        player = Player(Bike())
        player.up_from(transformer)

        self.assertEqual("jet", player.current_avatar.name)

    def test_up_from_then_down_from_first_avatar(self):
        transformer = Transformer(["bike", "car", "rocket", "jet"])
        player = Player(Bike())
        player.up_from(transformer)
        player.down_from(transformer)

        self.assertEqual("bike", player.current_avatar.name)

    def test_down_from_last_avatar(self):
        transformer = Transformer(["bike", "car", "rocket", "jet"])
        player = Player(Jet())
        player.down_from(transformer)

        self.assertEqual("bike", player.current_avatar.name)

    def test_down_from_then_up_from_last_avatar(self):
        transformer = Transformer(["bike", "car", "rocket", "jet"])
        player = Player(Jet())
        player.down_from(transformer)
        player.up_from(transformer)

        self.assertEqual("jet", player.current_avatar.name)

    def test_up_from_current_avatar_not_in_list(self):
        transformer = Transformer(["bike", "car", "jet"])
        player = Player(Rocket())
        player.up_from(transformer)

        self.assertEqual("rocket", player.current_avatar.name)

    def test_down_from_current_avatar_not_in_list(self):
        transformer = Transformer(["bike", "car", "jet"])
        player = Player(Rocket())
        player.down_from(transformer)

        self.assertEqual("rocket", player.current_avatar.name)