import helper

my_user_input = ""
while my_user_input != "exit":
    my_user_input = input("hey user, please enter any number of days and conversion unit!\n")
    days_and_unit = my_user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    helper.validate_and_execute(days_and_unit_dictionary)

















