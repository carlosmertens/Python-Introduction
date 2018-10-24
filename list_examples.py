""" LIST

A List is defined using square brackets[] and the elements of the list are
separated by commas.
We can look up individual elements in the List by their index.
Python follows a convention, called "zero based indexing". The firs element is
at index [0].
"""

print("\n")
print("==================== Example 1 ====================\n")

# Creating a List with all the versions of Python's releases:

python_versions = [1.0, 1.5, 1.6, 2.0, 2.1, 2.2, 2.3,
                   2.4, 2.5, 2.6, 2.7, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6]

print(python_versions)
print(python_versions[0])
print(python_versions[1])
print("Last version of Python is " + str(python_versions[-1]))

print("\n")
print("==================== Example 2 ====================\n")

# Return how many days there is in a month
month_input = 3


def how_many_days(month_number):
    """Returns the number of days in a month.
    WARNING: This function doesn't account for leap years!
    """
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = days_in_month[month_number - 1]
    return result


print("There is {} in month number {}".format(how_many_days(month_input), month_input))

print("\n")
print("==================== Example 3 =====================\n")

""" Slicing Lists """

months_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December']


print(months_name)
q3 = months_name[6:9]  # Start index[6] : end index[9]
print(q3)

first_half = months_name[:6]  # Start index[0] : end index[6]
print(first_half)

second_half = months_name[6:]  # Start index[6] : end index[finish List]
print(second_half)

print("\n")
print("==================== Example 4 ====================\n")

"""List vs String

'len' function and 'in' operator
"""
# The obvious difference is that strings are sequences of letters,
# while list elements can be any type of object.
# A more subtle difference is that lists can be modified, but strings can't be.
# Lists are mutable, while strings are immutable.

sample_string = "And Now For Something Completely Different"
sample_list = ['Graham', 'John', 'Terry', 'Eric', 'Merry', 'Michael']

print(sample_string[4])
print(sample_list[4])

print(sample_string[12:21])

print(sample_list[2:4])

print(len(sample_string))  # len will return the number of character in the String

print(len(sample_list))  # len will return the number

if 'thing' in sample_string:
    print("True")
else:
    print("False")

if 'Rowan' in sample_list:
    print("True")
else:
    print("False")

print(sample_list)
sample_list[3] = "Carlitos"
print(sample_list)

# sample_string [3] = y
# (will produce an error because String are immutable

print("\n")
print(sorted(sample_list))  # Sorted the List alphabetically
print(max(sample_list))  # max() function returns the greatest element in the List
print(min(sample_list))  # min() function returns the minimum element in the List

batch_sizes = [15, 6, 89, 34, 65, 200]
print(sorted(batch_sizes))
print(max(batch_sizes))
print(min(batch_sizes))

# .join method examples:
print("\n")
join_sample_list = "\n".join(sample_list)
print(join_sample_list)
join_sample_list = ", ".join(sample_list)
print(join_sample_list)
join_sample_list = "-".join(sample_list)
print(join_sample_list)
join_sample_list = "////".join(sample_list)
print(join_sample_list)

# .append method examples:
sample_list.append("Maria")  # .append will add to the List
print(sample_list)

sample_list.append("Nicole")
print(sample_list)

print("\n")
print("==================== Example 4 ====================\n")
"""Quiz: Top Three

Write a function, top_three, that takes a list as its argument, and returns a
list of the three largest elements.
For example, top_three([2,3,5,6,8,4,2,1]) == [8, 6, 5]
"""


def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

        If input_list has fewer than three elements, return input_list element sorted largest to smallest/
        """
    input_list = sorted(input_list, reverse=True)
    return input_list[:3]


quiz_list = [13, 2, 3, 4, 5, 6, 12, 15]
quiz_list0 = ["adam", "micky", "carlos", "xavier", "Elvis", "walter"]
quiz_list1 = [20, 100]
print(top_three(quiz_list))
print(top_three(quiz_list0))
print(top_three(quiz_list1))

print("\n")
print("==================== Example 4 ====================\n")
""" Median Quiz

When median is given a list with an even number of elements, it returns the
mean of the two central elements.
"""


def median(numbers):
    numbers.sort()
    if len(numbers) % 2:
        """ Uncomment to understand the condition

        print(numbers)
        print(len(numbers))
        print(len(numbers) % 2)"""
        middle_index = int(len(numbers) / 2)
        return numbers[middle_index]
    else:
        """ Uncomment to understand the condition

        print(numbers)
        print(len(numbers))
        print(len(numbers) % 2)
        """
        right_of_middle = len(numbers) // 2
        left_of_middle = right_of_middle - 1
        return (numbers[right_of_middle] + numbers[left_of_middle]) / 2


test1 = median([1, 2, 3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1, 2, 3, 4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))
