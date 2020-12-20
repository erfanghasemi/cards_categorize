from collections import deque


class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def get_color(self):
        return self.color

    def get_number(self):
        return self.number

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.number == other.number and self.color == other.color

    def __str__(self):
        return str(self.number) + str(self.color)


class Batch:
    def __init__(self):
        self.cards_count = 0;
        self.cards = deque()
        self.sorted_until = 0

    def is_empty(self):
        return self.cards.__len__() == 0

    def update_sorted_index(self):
        if self.cards_count == 0:
            self.sorted_until += 1
            self.cards_count += 1
        else:
            self.cards_count += 1
            color_match = self.cards.__getitem__(self.cards_count-1).color == self.cards.__getitem__(self.cards_count-2).color
            number_match = self.cards.__getitem__(self.cards_count-1).number < self.cards.__getitem__(self.cards_count-2).number
            if number_match and color_match:
                self.sorted_until += 1

    def insert_card(self, card: Card):
        self.cards.append(card)
        self.update_sorted_index()

    def pop_card(self):
        card = self.cards.pop()
        self.update_sorted_index()
        self.cards_count -= 1
        return card

    def is_sorted(self):
        return self.cards_count == self.sorted_until

    def last_card_number(self):
        return self.cards.__getitem__(self.cards_count-1).number

    def __eq__(self, other):
        try:
            for i in range(self.cards.__len__()):
                if self.cards.__getitem__(i) == other.cards.__getitem__(i):
                    continue
                else:
                    return False
            return True
        except IndexError:
            return False

    def __str__(self):
        if self.cards.__len__() == 0:
            return "#\n"

        representation = ""
        for card in self.cards:
            representation += card.__str__() + " "
        return representation


class State:
    def __init__(self):
        pass


class Search:
    def __init__(self):
        pass


class IO:
    def __init__(self):
        pass

