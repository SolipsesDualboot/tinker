def input_test(currencies, switch):
    if not switch:
        currencies[0] = float(input("what is your weekly salary? "))
    else:
        currencies[1] = float(input("what is your bonus? "))


def pay_pan():
    currencies = list((None, None))
    while True:
        try:
            input_test(currencies, False)
#            salary = float(input("what is your weekly salary? "))
            if type(currencies[0]) is not None:
                break
        except ValueError:
            print("Only enter a number!")
    while True:
        try:
            input_test(currencies, True)
#            bonus = float(input("what is your bonus? "))
            if type(currencies[1]) is not None:
                break
        except ValueError:
            print("Only enter a number!")
    total_pay = str(currencies[0] + currencies[1])
    print("the total pay for this week is $" + total_pay)


pay_pan()
