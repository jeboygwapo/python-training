import random

# Using random module getting random floating number from 0 to 1
# If I add * 10 at the end, it will be from 0 to 10

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# Random floating number between numbers a and b
# random_float = random.uniform(1,10)
# print(random_float)

# Heads or tails
coin = random.randint(0,1)
if coin == 0:
    print("Heads")
else:
    print("Tails")
