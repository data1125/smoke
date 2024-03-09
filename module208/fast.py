###############208  模組  模組 模組 模組 模組  模組 模組 模組S
from random import choice

places = ["McDonalds", "KFC", "Burger king", "Taco Bell",
          "Wendys", "Arbys", "pizza Hut"]
def pick(): #看到下面的docstring了嗎?
    """Return random fast food place"""
    return choice(places)
