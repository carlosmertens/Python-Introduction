""" DEFAULT ARGUMENTS """

print("\n==================== Example 1 ====================\n")


def box(width, height, symbol="*"):
    """print a box made up of asterisks, or some other character.

    symbol="*" is a default in case there is not input
    width: width of box in characters, must be at least 2
    height: height of box in lines, must be at least 2
    symbol: a single character string used to draw the box edges
    """
    # print top edge of box
    print(symbol * width)

    # print sides of box
    for _ in range(height - 2):
        print(symbol + " " * (width - 2) + symbol)

    # print bottom edge of box
    print(symbol * width)


# Call function
box(10, 10)
box(10, 10, "$")

print("\n==================== Example 2 ====================\n")


def print_list(l, numbered=False, bullet_character="-"):
    """Prints a list on multiple lines, with numbers or bullets

    Arguments:
    l: The list to print
    numbered: set to True to print a numbered list
    bullet_character: The symbol placed before each list element. This is
                      ignored if numbered is True.
    """
    for index, element in enumerate(l):
        if numbered:
            print("{}: {}".format(index + 1, element))
        else:
            print("{} {}".format(bullet_character, element))


print_list(["cats", "in", "space"])
print_list(["cats", "in", "space"], True)

print("\n==================== Example 3 ====================\n")
""" Default arguments are a helpful feature, but there is one situation where they can be surprisingly unhelpful.
Using a mutable type (like a list or dictionary) as a default argument and then modifying that argument can lead
to strange results. It's usually best to avoid using mutable default arguments: to see why, try the following
code locally.

Consider this function which adds items to a todo list. Users can provide their own todo list, or add items
to a default list:
"""


def todo_list(new_task, base_list=['wake up']):
    """Docstring is expected."""
    base_list.append(new_task)
    return base_list


print(todo_list("check the mail"))
print(todo_list("begin orbital transfer"))

print("\n==================== Example 4 ====================\n")
