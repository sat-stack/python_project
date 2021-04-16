# print("my name is satabdi")
# print(200)

minutes = 24 * 60 * 60
unit = 'sec'


def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * minutes} {unit}"


def validate_and_execute():
    try:
        user_input_number = int(many_days)

        # we want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("please enter valid value")
        else:
            print("your number is negative, enter a positive number")

    except ValueError:
        print("enter numbers only, no text")


my_user_input = ""
while my_user_input != "exit":
    my_user_input = input("enter any number of days here and i will covert it into seconds!\n")
    list_of_days = my_user_input.split(", ")

    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))

    for many_days in set(list_of_days):
        validate_and_execute()


