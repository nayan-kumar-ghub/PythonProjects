#Feedback Project
def feedback(fed1, fed2, fed3, fed4):

    if fed1 == 0:
        print(f"Thank you for providing {fed1} rating, we will do our best to improve")
    elif (fed2 == 1) or (fed2 == 2):
        print(f"Thank you for providing {fed2} rating, let us know where we need to improve")
    elif (fed3 == 3) or (fed3 == 4):
        print(f"Thank you for providing {fed3} rating, we wont disappoint you next time")
    elif fed4 == 5:
        print(f"Thank you for providing {fed4} rating, it’s much appreciated!")
    else:
        print("Invalid rating, please provide a rating between 0 and 5.")

# Prompting the user for input and calling the function
print("how would you like to rate out of 5")
user_input = int(input("Enter a rating (0-5): "))

# Calling the function based on user input
if user_input == 0:
    feedback(user_input, None, None, None)
elif user_input == 1 or user_input == 2:
    feedback(None, user_input, None, None)
elif user_input == 3 or user_input == 4:
    feedback(None, None, user_input, None)
elif user_input == 5:
    feedback(None, None, None, user_input)
else:
    print("Invalid rating, please provide a rating between 0 and 5.")