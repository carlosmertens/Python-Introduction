""" DICTIONARIES

Rather than storing single objects like lists and sets do,
dictionaries store pairs of elements: keys and values.

Dictionary keys are similar to list indices: we can select elements
from the data structure by putting the index/key in square brackets.
Unlike lists, dictionaries can have keys of any immutable type, not
just integers. The element dictionary uses strings for its keys. However,
it's not even necessary for every key to have the same type!
"""

from test_countries_list import country_list
# Note: since the list of countries is so large,
# it's tidier to put it in a separate file. (test_countries_list.py)
# this is for Quiz 1


print("\n")
print("==================== Example 1 ====================\n")
# In this example we define a dictionary where the keys are element names and the values are
# their corresponding atomic numbers.

elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}  # create a dictionary{}
print(elements)
print(elements['carbon'])  # print the value of the specific key

elements['lithium'] = 3  # add new key ('lithium') and value (3) to the dictionary{}
print(elements)

#
#
print("\n")
print("==================== Example 2 ====================\n")
"""Quiz: Define a Dictionary
Define a Dictionary, population, that provides information on the
world's largest cities. The key is the name of a city (a string), 
and the associated value is its population in millions of people.

   Key     |   Value
 Shanghai  |   17.8
 Istanbul  |   13.3
 Karachi   |   13.0
 Mumbai    |   12.5

"""

population = {"Shanghai": 17.8, "Istambul": 13.3, "Karachi": 13.0, "Mumbai": 12.5}

print(population)

# trying to find elements in the dictionary

# print(population["New York"])    will create a key error

# better ways to look up for elements:

if "New York" in population:
    print(population["New York]"])
else:
    print("We do not have data for New York")

print(population.get("New York"))  # will return None but it will not create a key error
print(population.get("New York", "We do not have data for New York"))  # after the coma, text to be return

#
#
print("\n")
print("==================== Quiz 1 ====================\n")
"""Quiz: Users by Country
Create a dict, country_counts, whose keys are country names, and whose values are the 
number of times the country occurs in the countries list."""

# from test_countries_list import country_list (already call on top of the file)

country_counts = {}
for country in country_list:
        if country in country_counts:
            country_counts[country] += 1  # increase the count of the country found
        else:
            country_counts[country] = 1  # add the country to the dictionary and set the value to 1

print(country_counts)

#
#
print("\n")
print("==================== Example 3 ====================\n")
"""The syntax for iterating over dictionaries is very similar. 
The difference is that dicts store key value pairs, and when we loop over them we iterate through the keys:"""

Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963,
                       "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
                       "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
                       "Sgt. Pepper's Lonely Hearts Club Band": 1967,
                       "Magical Mystery Tour": 1967, "The Beatles": 1968,
                       "Yellow Submarine": 1969, 'Abbey Road': 1969,
                       "Let It Be": 1970}

for album_title in Beatles_Discography:
    print("title: {}, year: {}".format(album_title, Beatles_Discography[album_title]))  # iterating

#
#
print("\n")
print("==================== Quiz 2 ====================\n")
"""Quiz: Prolific Year

Write a function most_prolific that takes a dict formatted like Beatles_Discography 
example above and returns the year in which the most albums were released. If you call 
the function on the Beatles_Discography it should return 1964, which saw more releases 
than any other year in the discography.

If there are multiple years with the same maximum number of releases, 
the function should return a list of years."""


def most_prolific(discs):
    years = {}  # empty dictionary to create key: year, value: how many times they are in the discography
    max_years = []  # empty list to be use to calculate the most repeating years
    max_number = 0  # variable to be used as a counter

    for disc in discs:
        # loop to add values to years{}
        year = discs[disc]
        if year in years:
            years[year] += 1
        else:
            years[year] = 1

    for year in years:
        # loop to count the repeating years
        if years[year] > max_number:
            # max_years = []     observation!!!
            max_years.append(year)
            max_number = years[year]
        elif years[year] == max_number and not (year in max_years):
            max_years.append(year)
    if len(max_years) == 1:
        return max_years[0]
    else:
        return max_years


print(most_prolific(Beatles_Discography))

#
#
print("\n")
print("==================== Quiz 3 ====================\n")
""" A DICTIONARIES OF DICTIONARIES

Flying Circus Records:
A regular flying circus happens twice or three times a month. For each month, information about
the amount of money taken at each event is saved in a list, so that the amounts appear in the order 
in which they happened. The months' data is all collected in a dictionary called monthly_takings.

For this quiz, write a function total_takings that calculates the sum of takings from every circus
 in the year. Here's a sample input for this function:
"""


def total_takings(monthly_takings):
    total = 0  # variable to add the monthly takings
    for month in monthly_takings.keys():  # iterate through the keys(months)
        total += sum(monthly_takings[month])  # add the values of every month
    return total


monthly_takings_list = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                        'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                        'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                        'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}

print(total_takings(monthly_takings_list))
