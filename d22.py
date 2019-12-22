import utils
import re


class Shuffle(object):

    def __init__(self, num_cards, factor, offset):
        super(Shuffle, self).__init__()
        self.num_cards = num_cards
        self.factor = ((factor % num_cards) + num_cards) % num_cards
        self.offset = ((offset % num_cards) + num_cards) % num_cards

    def apply(self, shuffle):
        self.factor = (self.factor * shuffle.factor) % self.num_cards
        self.offset = ((shuffle.factor * self.offset) % self.num_cards) + shuffle.offset

    def get_card_pos(self, card):
        return (((card * self.factor) % self.num_cards) + self.offset) % num_cards


def cut(num_cards, offset):
    return Shuffle(num_cards, 1, -offset)


def deal_increment(num_cards, factor):
    return Shuffle(num_cards, factor, 0)


def new_stack(num_cards):
    return Shuffle(num_cards, -1, -1)


def apply_input(num_cards):
    result = Shuffle(num_cards, 1, 0)

    re_deal_inc = re.compile(r"deal with increment ([0-9]+)")
    re_deal_new = re.compile(r"deal into new stack")
    re_cut = re.compile(r"cut (-?[0-9]+)")

    data = utils.get_input(2019, 22)[:-1]
    lines = data.split('\n')
    for line in lines:
        m = re.match(re_deal_new, line)
        if m:
            result.apply(new_stack(num_cards))
            continue

        m = re.match(re_deal_inc, line)
        if m:
            inc = int(m.group(1))
            result.apply(deal_increment(num_cards, inc))
            continue

        m = re.match(re_cut, line)
        if m:
            c = int(m.group(1))
            result.apply(cut(num_cards, c))
            continue

        print(f"Error at line: {line}")
    return result


num_cards = 10007
shuffle = apply_input(num_cards)
print(f"Part 1: {shuffle.get_card_pos(2019)}")


num_cards = 119315717514047
shuffle = apply_input(num_cards)
repeats = 101741582076661
n = 1
while n <= repeats:
    n *= 2
    shuffle.apply(shuffle)
print(f"Part 2: {shuffle.get_card_pos(2020)}")
