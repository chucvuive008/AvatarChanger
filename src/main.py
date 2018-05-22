from player import *
from transformer import *
import sys
import csv
import random


def get_avatar_list():
    open_file = open("avatar_list.txt", "r")
    avatar_list_file = open_file.read().split("\n")
    avatar_list = []
    for avatar in avatar_list_file:
        avatar_list.append(avatar.rstrip())
    return avatar_list


def get_avatar(avatar_list):
    avatar_name = random.choice(avatar_list)
    avatar = getattr(sys.modules[__name__], avatar_name.capitalize())()
    return avatar


def main():
    try:
        avatar_list = get_avatar_list()
        transformer = Transformer(avatar_list)
        player = Player(get_avatar(avatar_list))

        for i in range(10):
            player.perform_action()
            player.up_from(transformer)
            print(player.current_avatar.name)

    except AttributeError:
        print("the avatar list contain non-existing avatar name")
    except FileNotFoundError:
        print("avatar_list.txt file is not in the directory.")


main()
