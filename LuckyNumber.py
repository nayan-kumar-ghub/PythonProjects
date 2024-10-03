#Project Lucky Number
import random
import time

# Get user input for the lucky number
user_input = int(input("Enter your lucky number:"))

# Tuple of random numbers
random_num=(45, 10, 8, 100, 1, 9, 99, 143, 121, 69)

# Convert tuple to list and add the user's number
lucky_random = list(random_num)
lucky_random.append(user_input)

# Choose a random number from the updated list
lucky_num = random.choice(lucky_random)

# Countdown timer before displaying the lucky number
print("***Today's lucky choice number will be revealed in...***")
for i in range(5, 0, -1):  # Countdown from 5 to 1
    print(i, end="...", flush=True)  # Print the countdown number
    time.sleep(1)  # Wait for 1 second between numbers
print("")
print("")
# Display the lucky number
print("***Today's lucky choice number is***")
print(lucky_num)

# Check if the lucky number matches the user's input
if lucky_num==user_input:
    print("Congratulations, you won today's lucky number game.")
    print("Keep Winning")
else:
    print("Better luck next time")