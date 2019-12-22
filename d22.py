import utils
import re
from itertools import cycle


def deal_into_new_stack(deck):
    deck.reverse()
    return deck


def deal_with_increment(deck, increment):
    deck_size = len(deck)
    steps = range(0, deck_size * increment, increment)
    positions = [i % deck_size for i in steps]
    new_deck = [0] * deck_size
    for i in range(deck_size):
        new_deck[positions[i]] = deck[i]
    return new_deck


def cut(deck, cut):
    return deck[cut:] + deck[:cut]


data = utils.get_input(2019, 22)[:-1]
lines = data.split('\n')
factory_order = range(0, 119315717514047)
deck = list(factory_order)

re_deal_inc = re.compile(r"deal with increment ([0-9]+)")
re_deal_new = re.compile(r"deal into new stack")
re_cut = re.compile(r"cut (-?[0-9]+)")

for line in lines:
    m = re.match(re_deal_new, line)
    if m:
        deck = deal_into_new_stack(deck)
        continue

    m = re.match(re_deal_inc, line)
    if m:
        inc = int(m.group(1))
        deck = deal_with_increment(deck, inc)
        continue

    m = re.match(re_cut, line)
    if m:
        c = int(m.group(1))
        deck = cut(deck, c)
        continue

    print(f"Error at line: {line}")

print(f"Part 1: The position of card 2019 is {deck.index(2020)}")
