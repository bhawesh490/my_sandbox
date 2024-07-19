from datetime import datetime


# Example 1
class TimeUTC:
    def __get__(self, instance, owner_class):
        return datetime.utcnow().isoformat()


class Logger:
    current_time = TimeUTC()  # instance of TimeUTC class


print("Example 1")
print(Logger.__dict__)
print(Logger.current_time)
l = Logger()
print(l.current_time)

# Example 2
from random import choice, seed


class Deck:
    @property
    def suit(self):
        return choice(("Spade", "Heart", "Diamond", "Club"))

    @property
    def card(self):
        return choice(tuple("23456789") + ("10", "J", "Q", "K", "A"))


d = Deck()
seed(0)
print("Example 2")
for _ in range(10):
    print(d.suit, d.card)

# Now we have two properties that do the same thing.they choose fro ma given iterable
# to handle this lets define descriptor class


class Choice:
    def __init__(self, *choices):
        self.choices = choices

    def __get__(self, instance, owner_class):
        # print("Calling getters from descriptor class")
        return choice(self.choices)


class Deck:
    suit = Choice("Spade", "Heart", "Diamond", "Club")
    card = Choice(*"23456789", "10", "J", "Q", "K", "A")


seed(0)
d = Deck()
for _ in range(10):
    print(d.suit, d.card)
    break


class Dice:
    dice_1 = Choice(1, 2, 3, 4, 5, 6)
    dice_2 = Choice(1, 2, 3, 4, 5, 6)
    dice_3 = Choice(1, 2, 3, 4, 5, 6)


seed(0)
d = Dice()
for _ in range(10):
    print(d.dice_1, d.dice_2, d.dice_3)
