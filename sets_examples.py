"""SETS

Sets() are simple data structures, and they have one main use: c
ollecting unique elements.
"""
print("\n==================== Quiz 1 ====================\n")
"""Quiz: De-duplication

Write a function, remove_duplicates that takes a list as its argument
and returns a new list containing the unique elements of the original
list. The elements in the new list without duplicates can be in any
order.
"""
print("\n==================== Example 1 ====================\n")


def remove_duplicates(source):
    """ Function to remove any duplicates elements in a list[]."""
    target = []

    for element in source:
        if element not in target:
            target.append(element)

    return target


test_list = ["apple", "chille", "orange", "hot souce", "apple", "chille"]
new_list = remove_duplicates(test_list)
print(new_list)

print("\n==================== Example 2 ====================\n")

# converts the list[] in a set()
test_set = set(test_list)
print(test_set)

test_set.add("black pepper")
print(test_set)

print("\n==================== Quiz 2 ====================\n")
"""Quiz: Build a Set

In a similar way to building an empty list with my_list = [], you can create
an empty set with my_set = set(). Using this technique, and the add method,
build a set of all of the square numbers greater than 0 and less than 2,000.
For reference, I included my implementation of nearest_square function from
an earlier quiz. You may call the function in your code, integrate it into
your code, or ignore it altogether.
"""

# Note: If you want to call the nearest_square function, you must define
# the function on a line before you call it. Feel free to move this code up!
squares = set()


def nearest_square(limit):
    """Squares are created

    Starting from square of 1, then tested if it is less than the number
    provided (limit) at the same time, also add the element to the set
    """
    # Variable to count
    i = 0
    while (i + 1)**2 <= limit:
        """ Squares are created, starting from square of 1, then tested
            if it is less than the number provided (limit)

            at the same time, also add the element to the set"""
        squares.add((i + 1)**2)
        # Counter increases to create the next square number
        i += 1
    # Return the nearest square to the number given
    return squares


test1 = nearest_square(2000)
print(sorted(squares))
