""" Work with files.

You're going to create a list of the actors who appeared in the television
programme Monty Python's Flying Circus.
"""
# Monty Python's Flying Circus cast list
#
# Write a function called create_cast_list that takes a filename as input and
# returns a list of actors' names. It will be run on the fil
# flying_circus_cast.txt (this information was collected from imdb.com).
# Each line of that file consists of an actor's name, a comma, and then some
# (messy) information about roles they played in the programme. You'll need to
# extract only the name and add it to a list. You might use the .split()
# method to process each line.


def create_cast_list(filename):
    cast_list = []
    # use with to open the file filename
    with open(filename) as f:
        # use the for loop syntax to process each line
        for line in f:
            # and add the actor name to cast_list
            cast_list.append(line.split(',')[0])
    return cast_list


print(create_cast_list("flying_circus_cast.txt"))
