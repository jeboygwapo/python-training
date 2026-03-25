print("Welcome to tip calculator!")
total_bill = int(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
if tip in [10, 12, 15]:
    num_of_people_split = int(input("How many people to split the bill? "))
    if num_of_people_split > 0: 
        # Computation for each person final bill
        total_with_tip = total_bill * (1 + tip / 100)
        each_pay = total_with_tip / num_of_people_split

        print(f"For {num_of_people_split} people, each person should pay: ${each_pay:.2f}")
    else:
        print("Invalid number of people.")
else:
    print("Invalid input for tip.")
