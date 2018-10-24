""" FOR LOOPS

We use lists to store sequences of data, and we use for loops to iterate over lists.
"""
print("\n==================== Example 1 ====================\n")

names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc',
         'nigel incubator-jones', 'philip diplodocus mallory']
print(names)


for name in names:
    """This for loop will iterate through the List[names]
    # and return each element capitalized """
    print(name.title())

print("-" * 50)

# Create a new list of capitalized names without modifying the original list
names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc',
         'nigel incubator-jones', 'philip diplodocus mallory']
print(names)

# Create a new, empty list
capitalized_names = []
for name in names:
    # Add elements to the new list with .append method
    capitalized_names.append(name.title())

print(capitalized_names)

print("-" * 50)

# Modify the names list in place without creating a new list
# Iterate over the index numbers of the names list
for index in range(len(names)):
    # Modify each element of names
    names[index] = names[index].title()
print(names)

print("\n==================== Quiz 1 ====================\n")
""" Sum of a list quiz:

    Define a function, list_sum, that takes a list as its argument and returns
    the sum of the elements in the list. Use a for loop to iterate over
    the list.
    """


def list_sum(input_list):
    list_addition = 0
    for number in input_list:
        list_addition += number
    return list_addition


# These test cases check that list_sum works correctly
test1 = list_sum([1, 2, 3])
print("expected result: 6, actual result: {}".format(test1))

test2 = list_sum([-1, 0, 1])
print("expected result: 0, actual result: {}".format(test2))

test3 = list_sum([2, 2, 2, 2, 2, 5, 5])
print("expected result: 20, actual result: {}".format(test3))

print("\n==================== Quiz 2 ====================\n")

"""Write a function, `tag_count`, that takes as its argument a list
of strings. It should return a count of how many of those strings
are XML tags. You can tell if a string is an XML tag if it begins
with a left angle bracket "<" and ends with a right angle bracket ">".
"""


def tag_count(input_list):
    # Variable to count the XML tags
    xml_counter = 0
    # For Loop to iterate the list[]
    for item in input_list:
        # Check the item if it is a XML tag
        if item[0] == "<" and item[-1] == ">":
            xml_counter += 1
    return xml_counter


# Test for the tag_count function:
list1 = ['<greeting>', 'Hello World!', '</greeting>', 'loco>', '<epa', '<nino>']
count = tag_count(list1)
print("Expected result: 3, Actual result: {}".format(count))

print("\n==================== Quiz 3 ====================\n")
"""Write the html_list function. The function takes one argument, a list of strings,
and returns a single string which is an HTML list. For example, if the function should
produce the following string when provided the list ['first string', 'second string'].

<ul>
<li>first string</li>
<li>second string</li>
</ul>

That is, the string's first line should be the opening tag <ul>. Following that is one line
per element in the source list, surrounded by <li> and </li> tags. The final line
of the string should be the closing tag </ul>."""


def html_list(input_list):
    html_created = "<ul>\n"
    # Print(html_created)
    for line in input_list:
        html_created += ("<li>" + line + "<li>\n")
        # Print(html_created)

    html_created += "</ul>"
    # Print(html_created)
    return html_created


sample1 = ["1", 'second string', "third string"]
call_def = html_list(sample1)
print(call_def)

print("\n==================== Quiz 4 ====================\n")
"""Quiz starbox
    The starbox function in the quiz below prints a box made out of asterisks.
    The function takes two arguments, width and height, that specify how many
    characters wide the box is and how many lines tall it is. The function isn't
    quite complete: it prints boxes of the correct width, but the height argument
    is ignored. Complete the function so that both of the provided test cases
    print boxes that are the correct size. Hint: The range function could be helpful!"""


def starbox(width, height):
    """print a box made up of asterisks.

    width: width of box in characters, must be at least 2
    height: height of box in lines, must be at least 2
    """
    # Print top edge of box
    print("*" * width)
    # Print sides of box
    for i in range(height - 2):
        print("*" + " " * (width - 2) + "*")
    # Print bottom edge of box
    print("*" * width)


# Test Cases
print("Test 1:")
starbox(5, 10)

print("Test 2:")
starbox(20, 5)


""" WHILE LOOPS

They are loops with "indefinite iteration" which is when a loop repeats an
unknown number of times and ends when some condition is met.
"""

print("\n")
print("==================== Example 1 ====================\n")

card_deck = [4, 11, 8, 5, 13, 2, 8, 10]  # dealers card (manually picked)
hand = []  # empty list to add cards

while sum(hand) <= 21:
    # while the sum of the element in hand are True to the condition, the loop will iterate
    hand.append(card_deck.pop())  # add an element from card_deck list

print(hand)

#
#
print("\n")
print("==================== Quiz 1 ====================\n")
""" Quiz: Nearest Square
Implement the nearest_square function. The function takes an integer argument limit, and
returns the largest square number that is less than limit. A square number is the product of an
integer multiplied by itself, for example 36 is a square number because it equals 6*6. """


def nearest_square(limit):
    i = 0  # variable to count
    while (i + 1)**2 < limit:
        """ Squares are created, starting from square of 1, then tested
            if it is less than the number provided (limit)"""
        i += 1  # counter increases to create the next square number
    return i**2  # when condition has been met, will return the nearest square to the number given


test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))

#
#
print("\n")
print("==================== Example 2 ====================\n")
"""In the example below we will see how break can be used. Suppose you wanted
to load a cargo ship with a list of items. Each item weighs a certain amount
and the ship has a maximum weight capacity.
Ideally you would like to load all the items on the ship, but you do not want
to overload the ship.
Therefore when the ship's capacity is reached you should stop loading.
To accomplish that we will use a for loop, loading each item and keeping
track of the weight of all the items we have loaded so far.
We will use a break statement to stop loading once the ship reaches capacity.

Note: The manifest in this example is a list of list. We have seen lists
before, and you can also have list elements that are themselves lists- this
is the case with the manifest variable. Each element in the manifest list is
a list itself, one that contains two things: an item and its weight."""
# each item in the manifest is an item and its weight
manifest = [["bananas", 15], ["mattresses", 34], ["dog kennels", 42], ["machine that goes ping!", 120],
            ["tea chests", 10], ["cheeses", 0]]

cargo_weight = 0
cargo_hold = []

for cargo in manifest:
    if cargo_weight + cargo[1] >= 100:
        break
    else:
        cargo_hold.append(cargo[0])
        cargo_weight += cargo[1]

print(cargo_weight)
print(cargo_hold)

print("\n==================== Quiz 2 ====================\n")
""" Quiz: Break the String
Your task is to create a string, news_ticker that is exactly 140 characters
long. You should create the news ticker by adding headlines from the headlines
list, inserting a space in between each headline. If necessary, truncate the
last headline in the middle so that news_ticker is exactly 140 characters long.

Remember that break works in both for and while loops. Use whichever loop
seems most appropriate. Consider adding print statements to your code to help
you resolve bugs.
"""

headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for string in headlines:
    if len(news_ticker) >= 140:
        break
    else:
        news_ticker += string + " "
news_ticker = news_ticker[:140]

print(news_ticker)
print(len(news_ticker))
