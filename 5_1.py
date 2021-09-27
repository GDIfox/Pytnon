import random


def m_random():
    x = 0
    while x % 2 != 1:
        x = random.randint(0, 100)
    yield x


print(m_random().__next__())
