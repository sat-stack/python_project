# print("my name is satabdi")
# print(200)

minutes = 24*60*60
unit = 'sec'


def days_to_units(number_of_days):
    if int(number_of_days) > 0:
        return f"{number_of_days} days are {20 * minutes} {unit}"
    elif int(number_of_days) == 0:
        return "please enter valid value"
    else:
        return "invalid value, no conversion"


my_user_input = input("enter any number of days here and i will covert it into seconds!\n")

if my_user_input.isdigit():
    user_input_number = int(my_user_input)
    calculated_value = days_to_units(my_user_input)
    print(calculated_value)
else:
    print("enter only number")



# here I learnt if and else condition for validation of input