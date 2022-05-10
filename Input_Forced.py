
# this function will check user input, and restrict it to a list that you have defined
# define that list on line 2
# any case sensitivy is managed in the function


def fRestrict_User_Input(user_can_only_type, input_message):
    list_upper_case = [each_string.upper() for each_string in user_can_only_type]
    while True:
        try:
            user_input = input(input_message + ": ")
            if str(user_input).upper() in list_upper_case:
                return user_input
            raise ValueError()
        except ValueError:
            print("    Error: You are required to enter one of the following: {}".format(user_can_only_type))
            print("    Please try again\n")


# modify list here
fruit_list = ["Apple", "banana", "Pineapple", "Potato", "Watermelon"]

# change the input message for user to read
input_message = "Select your favourite fruit"


# end result
selected_fruit = fRestrict_User_Input(fruit_list, input_message)
print("user selected " + selected_fruit)
