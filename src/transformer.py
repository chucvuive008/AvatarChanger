from bike import *
from car import *
from rocket import *
from jet import *
import sys


class Transformer:
    def __init__(self, avatar_names):
        self.avatar_names = avatar_names

    def find_index(self, avatar):
        index = len(self.avatar_names) + 1
        for i in range(len(self.avatar_names)):
            if avatar.name == self.avatar_names[i]:
                index = i
        return index

    def create_avatar_object(self, index):
        return getattr(sys.modules[__name__], self.avatar_names[index].capitalize())()

    def transform_up(self, avatar):
        above_avatar = avatar
        index = self.find_index(avatar) - 1
        if index < len(self.avatar_names):
            above_avatar = self.create_avatar_object(index)
        return above_avatar

    def transform_down(self, avatar):
        below_avatar = avatar
        index = self.find_index(avatar) + 1
        if index == len(self.avatar_names):
            below_avatar = self.create_avatar_object(0)
        elif index < len(self.avatar_names):
            below_avatar = self.create_avatar_object(index)
        return below_avatar
