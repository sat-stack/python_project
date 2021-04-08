minutes = 24*60*60
unit = 'sec'


def days_to_units(number_of_days):
    return f"{number_of_days} days are {20 * minutes} {unit}"


user_input = input("enter any number of days here and i will covert it into seconds!\n")
user_input_number = int(user_input)

calculated_value = days_to_units(user_input)
print(calculated_value)





