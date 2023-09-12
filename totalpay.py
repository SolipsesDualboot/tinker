# A short program for calculating the sum of two numbers, in the context of a weekly payment plus a bonus

# A function for parsing input. It helps to break your main function into procedures
# with the purpose of avoiding exceeding three or four levels of indentation, keeping
# code readable and digestible
def input_test(currencies, switch):  # The two variable names between the () indicate their input's intention
    if not switch:  # Switch is intended to be a boolean. this checks if switch is set to false
        currencies[0] = float(input("what is your weekly salary? "))  # Lists start at index 0, like binary
    else:
        currencies[1] = float(input("what is your bonus? "))  # Must not be a plain integer, they are immutable


def pay_pan():
    currencies = list((None, None))  # We intend to store two numbers in this list and no more
    # though You could maybe alternatively use .append() in input_test on an empty list
    while True:  # Forms an infinite loop until this is done correctly
        try:    # First part of error handling
            input_test(currencies, False)
            if type(currencies[0]) is not None:  # The beauty of Python syntax
                break  # Indicates to the loop that it is time to end
        except ValueError:  # Instead of ValueError, enter whatever error you get, if you have a plan
            print("Only enter a number!")  # Handled error message. Or you could give no message
    while True:
        try:
            input_test(currencies, True)
            if type(currencies[1]) is not None:
                break
        except ValueError:
            print("Only enter a number!")
    total_pay = str(currencies[0] + currencies[1])  # It is fine to assume the values are integers
    # as we already checked when setting them
    print("the total pay for this week is $" + total_pay)


pay_pan()
