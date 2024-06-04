#!/usr/bin/env python
# __coconut_hash__ = 0xd796c34e

# Compiled with Coconut version 1.3.0 [Dead Parrot]

# Coconut Header: -------------------------------------------------------------


# Compiled Coconut: -----------------------------------------------------------

game1 = {
    "player": {"name": "Kvido", "nick": "kvido"},
    "results": {"score": {"last": 1000, "top": 2000}, "lives": 0},
}


def print_last_score_variant_A(game):
    score = game.get("results").get("score").get("last")
    print("Score: {s}".format(s=score))


print("\nVariant A")
print_last_score_variant_A(game1)

game2 = {"player": {"name": "Kvido", "nick": "kvido"}}


def print_last_score_variant_B(game):
    score = game.get("results", {}).get("score", {}).get("last")
    print("Score: {s}".format(s=score))


print("\nVariant B")
print_last_score_variant_B(game1)
print_last_score_variant_B(game2)


def print_last_score_variant_C(game):
    score = (
        lambda x: None
        if x is None
        else (lambda x: None if x is None else x.get("last"))(x.get("score"))
    )(game.get("results"))
    print("Score: {s}".format(s=score))


print("\nVariant C")
print_last_score_variant_C(game1)
print_last_score_variant_C(game2)


class Player(_coconut.object):
    def __init__(self, name, nick):
        self.name = name
        self.nick = nick


class Score(_coconut.object):
    def __init__(self, last, top):
        self.last = last
        self.top = top


class Game(_coconut.object):
    def __init__(self, player, score, lives):
        self.player = player
        self.score = score
        self.lives = lives


def print_last_score_variant_D(game):
    score = (
        lambda x: None
        if x is None
        else (lambda x: None if x is None else x.last)(x.score)
    )(game)
    print("Score: {s}".format(s=score))


game1_obj = Game(Player("Kvido", "kvido"), Score(1000, 2000), 0)

game2_obj = Game(Player("Kvido", "kvido"), None, 0)

print("\nVariant D")
print_last_score_variant_D(game1_obj)
print_last_score_variant_D(game2_obj)
