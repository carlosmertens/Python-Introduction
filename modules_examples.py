"""STANDARD LIBRARY."""

# MODULES
#
# Our favourite modules  -- UDACITY
# Here are a selection of our favourite Python Standard Library!
#
# csv: very convenient for reading and writing csv files
# collections: useful extensions of the usual data types including OrderedDict,
# defaultdict and namedtuple random: generates pseudo-random numbers, shuffles
# sequences randomly and chooses random items
# string: more functions on strings.
# This module also contains useful collections of letters like string.digits
# (a string containing all characters with are valid digits).
# re: pattern-matching in strings via regular expressions
# math: some standard mathematical functions
# os: interacting with operating systems
# os.path: submodule of os for manipulating path names
# sys: work directly with the Python interpreter
# json: good for reading and writing json files (good for web work)
# We hope you find these useful!
import random as rd
from datetime import datetime

# Third-Party Libraries
import pytz
# import math  # import the module math
# from collections import defaultdict, namedtuple  # will import only the 2 functions form the module
# import multiprocessing as mp  # module can be imported with different name
# from csv import reader as csvreader  # a function from a module can be imported with diff name

print("\n")
print("==================== Example 1 ====================\n")

# print(math.factorial(3))

# print(math.exp(3))

# defaultdict

# namedtuple()

# mp.get_all_start_methods()

# csvreader()"""

print("\n")
print("==================== Quiz 1 ====================\n")

"""Password Generator."""
# Write a function called generate_password that selects three random words
# from the list of words word_list and concatenates them into a single string.
# Your function should not accept any arguments and should reference the global
# variable word_list to build the password.
# Note: words.txt

# will be call the module random at the beginning of the program

# Use an import statement at the top

word_file = "words.txt"
word_list = []

# fill up the word_list
with open(word_file, 'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # Exclude words that are too long or too short
        if 4 < len(word) < 10:
            word_list.append(word)


def generate_password():
    return rd.choice(word_list) + rd.choice(word_list) + rd.choice(word_list)


# test your function
print(generate_password())

#
#
print("\n")
print("==================== Example 2 ====================\n")

# from datetime import datetime
# import pytz
# called above

utc = pytz.utc  # utc is Coordinated Universal Time
ist = pytz.timezone('Asia/Kolkata')  # IST is Indian Standard Time

now = datetime.now(tz=utc)  # this is the current time in UTC
ist_now = now.astimezone(ist)  # this is the current time in IST.

print(now)
print(ist_now)

# Useful Third-Party Packages
# Being able to install and import third party libraries is useful, but to be
# an effective programmer you also need to know what libraries are available
# for you to use. People typically learn about useful new libraries by word of
# mouth; from an online recommendation or from a colleague. If you're a new
# Python programmer you may not have many colleagues, so to get you started
# here's a list of packages that are popular with engineers at Udacity:

# IPython - A better interactive Python interpreter
# requests - Provides easy to use methods to make web requests. Useful for accessing web APIs.
# Flask - a lightweight framework for making web applications and APIs.
# Django - A more featureful framework for making web applications. Django is particularly good for designing complex, content heavy, web applications.
# Beautiful Soup - Used to parse HTML and extract information from it. Great for web scraping.
# pytest - extends Python's builtin assertions and unittest module.
# PyYAML - For reading and writing YAML files.
# NumPy - The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
# Pandas - A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes!
# matplotlib - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments.
# ggplot - Another 2D plotting library, based on R's ggplot2 library.
# Pillow - The Python Imaging Library adds image processing capabilities to your Python interpreter.
# pyglet - A cross-platform application framework intended for game development.
# Pygame - A set of Python modules designed for writing games.
# pytz - World Timezone Definitions for Python"""
