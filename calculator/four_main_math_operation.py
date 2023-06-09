from make_list_main_character import list_main_character
from make_list_main_character import make_list_character


# I in this function we calculate the multiplication and division then separate the answer of them instead of
# Last number.
# Tip: In math before and after any math operation we have a number like this (2 * 6 - 1)
def multiplication_and_dvision():
    while '*' in list_main_character or '/' in list_main_character:

        for item in list_main_character:
            # This is the first part of this function.
            # In here we define the numbers that are before and after dvision and this is for tip that i sayed
            # Then we divided the number before dvision and number after dvision then
            # Remove this 3 character and separate answer in list_character.
            if item == '/':
                number_before_math_operation = list_main_character[list_main_character.index(item) - 1]
                number_after_math_operation = list_main_character[list_main_character.index(item) + 1]

                result_dvision = float(number_before_math_operation) / float(number_after_math_operation)

                list_main_character.insert(list_main_character.index(item) - 1, result_dvision)
                list_main_character.remove(number_before_math_operation)
                list_main_character.pop(list_main_character.index(item))
                list_main_character.remove(number_after_math_operation)

            # This is the second part of this function.
            # In here work like part 1 but the difference between this two it's the math operation
            # First one is division the second part is multiplication.
            elif item == '*':
                number_before_math_operation = list_main_character[list_main_character.index(item) - 1]
                number_after_math_operation = list_main_character[list_main_character.index(item) + 1]

                result_multiplication = float(number_after_math_operation) * float(number_before_math_operation)

                list_main_character.insert(list_main_character.index(item) - 1, result_multiplication)
                list_main_character.remove(number_before_math_operation)
                list_main_character.pop(list_main_character.index(item))
                list_main_character.remove(number_after_math_operation)

            else:
                continue

    return list_main_character


# This function exactly work like last function but in here we calculate total and subtraction
# Tip: in math before and after any math operation we have a number like this (2 * 6 - 1)
def total_subtraction():
    while '+' in list_main_character or '-' in list_main_character:

        for item in list_main_character:
            # This function hase two part and this is first.
            # First like function one we define after and before number of math operation
            # Then calculate our phrase and separate answer by last character
            if item == '+':
                number_before_math_operation = list_main_character[list_main_character.index(item) - 1]
                number_after_math_operation = list_main_character[list_main_character.index(item) + 1]

                result_total = float(number_before_math_operation) + float(number_after_math_operation)

                list_main_character.insert(list_main_character.index(item) - 1, result_total)
                list_main_character.remove(number_before_math_operation)
                list_main_character.pop(list_main_character.index(item))
                list_main_character.remove(number_after_math_operation)

            # This is the second part of function
            # This part work like last part but the difference is our math operation
            elif item == '-':
                number_before_math_operation = list_main_character[list_main_character.index(item) - 1]
                number_after_math_operation = list_main_character[list_main_character.index(item) + 1]

                result_multiplication = float(number_before_math_operation) - float(number_after_math_operation)

                list_main_character.insert(list_main_character.index(item) - 1, result_multiplication)
                list_main_character.remove(number_before_math_operation)
                list_main_character.pop(list_main_character.index(item))
                list_main_character.remove(number_after_math_operation)

            else:
                continue

    return list_main_character


# This function is relation of our function's that we made.
# After multiplication_and_dvision() and total_subtraction() len list_main_character is 1 and this object is our answer.
def calculate_math_operation():
    multiplication_and_dvision()
    total_subtraction()
    answer_math = list_main_character
    return answer_math


# This function is for get new math operation from user and if we don't do this, calculate_math_operation
# Calculate the last math operation.
def new_list_main_character():
    global  list_main_character
    list_main_character = make_list_character()
