""" TUPLES

Tuples are similar to lists in that they store an ordered collection of
objects which can be accessed by their indexes (for example AngkorWat[0]
and AngkorWat[1]).
Unlike lists, tuples are IMMUTABLE. You can't add and remove items from tuples,
or sort them in place.
"""
print("\n==================== Example 1 ====================\n")

AngkorWat = (13.4125, 103.866667)
print(type(AngkorWat))
# Tuples are indexed
print("Angkor Wat is at latitude: {}".format(AngkorWat[0]))
print("Angkor Wat is at longitude: {}".format(AngkorWat[1]))

# Omit the parenthesis
dimensions = 52, 40, 100
# This is called tuple unpacking
length, width, height = dimensions
print("The dimensions are {}x{}x{}".format(length, width, height))

print("\n==================== Example 2 ====================\n")
"""In the example below we create a dictionary, world_heritage_locations
that has tuples of the form (latitude, longitude) as the keys and strings
denoting the corresponding place names as values.
"""

world_heritage_locations = {(13.4125, 103.866667): "Angkor Wat",
                            (25.73333, 32.6): "Ancient Thebes",
                            (30.330556, 35.4433330): "Petra",
                            (-13.116667, -72.583333): "Machu Picchu"}

print(world_heritage_locations)

print("\n==================== Example 3 ====================\n")
# A common use for tuples is to return multiple values from a function:


def first_and_last(sequence):
    """Returns the first and last elements of a sequence"""
    return sequence[0], sequence[-1]


print(first_and_last(["Spam", "egg", "sausage", "Spam", "lettuce"]))

start, end = first_and_last(["Spam", "egg", "sausage", "Spam"])
print(start)
print(end)

print("\n==================== Quiz 1 ====================\n")
""" Days and Hours:

Try your hand at writing a function that uses a tuple to return multiple
values. Write an hours2days function that takes one argument, an integer,
that is a time period in hours. The function should return a tuple of how
long that period is in days and hours, with hours being the remainder that
can't be expressed in days. For example, 39 hours is 1 day and 15 hours, so
the function should return (1,15).
"""


def hours2days(input_hours):
    """ Receive the hours and will return ow many days and hours there is in the input """
    # Floor division to get the days but not the extra hours
    days = input_hours // 24
    # Modulus to get the left hours after calculating the days
    hours = input_hours % 24
    # Returns tuples
    return days, hours


print(type(hours2days(24)))
print(hours2days(25))
print(hours2days(10000))
