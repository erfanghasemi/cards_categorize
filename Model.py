class Search:
    def __init__(self):
        pass


class State:
    def __init__(self):
        pass


class Batch:
    def __init__(self):
        pass


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


class Input:
    def __init__(self):
        pass

