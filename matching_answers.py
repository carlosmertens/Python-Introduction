"""Quiz: Refactor the Code

This was a pretty long list of ways to improve this code! Don't be daunted,
we don't have to take them all on at once - in fact, it's better to make one
change at a time, and test the results.
"""

# In this quiz, make two changes to the program:

# TODO: Move (refactor) the code that checks the answers into a separate function.
# Give it a good name. Use a loop to call that function on each answer, so that
# there aren't five calls to the function.
# Improve the docstring and add comments to make the code easier to understand.
# This doesn't cover the whole list of improvements, but it's a good start!
# If you want to do more, feel free. Your code will be tested on some test cases,
# so just make sure it still works correctly!


# def check_answers(my_answers,answers):
#     """
#     Checks the five answers provided to a multiple choice quiz and returns the results.
#     """
#     results = [None, None, None, None, None]
#     if my_answers[0] == answers[0]:
#         results[0] = True
#     elif my_answers[0] != answers[0]:
#         results[0] = False
#     if my_answers[1] == answers[1]:
#         results[1] = True
#     elif my_answers[1] != answers[1]:
#         results[1] = False
#     if my_answers[2] == answers[2]:
#         results[2] = True
#     elif my_answers[2] != answers[2]:
#         results[2] = False
#     if my_answers[3] == answers[3]:
#         results[3] = True
#     elif my_answers[3] != answers[3]:
#         results[3] = False
#     if my_answers[4] == answers[4]:
#         results[4] = True
#     elif my_answers[4] != answers[4]:
#         results[4] = False
#     count_correct = 0
#     count_incorrect = 0
#     for result in results:
#         if result == True:
#             count_correct += 1
#         if result != True:
#             count_incorrect += 1
#     if count_correct/5 > 0.7:
#         return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
#     elif count_incorrect/5 >= 0.3:
#         return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."


# ====================================================================================================================

# function that will check and compare the answers


def compare_answers(answer_input, correct_answer):
    count_correct = 0  # to count the correct answer
    i = 0  # to loop through the answer_input list
    while i < (len(answer_input)):
        if answer_input[i] == correct_answer[i]:
            count_correct += 1
        i += 1
    if count_correct / len(correct_answer) > 0.7:
        print("Congratulations, you passed the test! "
              "You scored {} out of {}".format(count_correct, len(correct_answer)))
    else:
        print("Unfortunately, you did not pass the test. "
              "You scored {} out of {}".format(count_correct, len(correct_answer)))


test_correct_answers = ["tree", "train", "bout", "road", "house", "love"]
test_input_answers = ["tree", "train", "bout", "road", "mouse", "love"]

compare_answers(test_input_answers, test_correct_answers)
