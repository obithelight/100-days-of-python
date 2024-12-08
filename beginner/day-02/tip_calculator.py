# Create a program that calculates a bill split between friends and adds a percentage tip to the it

# Print a welcome message
print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, 0r 15? "))

people = int(input("How many people to split the bill? "))

# Get tip amount using the percentage tip * bill
tip_amount = bill * (tip / 100)

# Add tip_amount to bill
total_bill = tip_amount + bill

# Divide total bill by number of people to get what each person will pay
each_to_pay = total_bill / people

# Round up each_to_pay to 2 decimal numbers
each_to_pay = round(each_to_pay, 2)

# Print the output message with final_bill for each person
print(f"Each person should pay: ${each_to_pay}")
