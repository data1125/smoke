##############################211
from random import choice 

places = ["McDonalds", "KFC", "Burger king", "Taco Bell",
          "wendys", "Ardys", "pizza Hut"]
def pick():
    """Return random fast food place"""
    return choice(places)