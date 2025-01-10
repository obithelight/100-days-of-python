# Tip Calculator Project
'''
Create a program that calculates a bill split between friends and adds a percentage tip to the bill.

Example:
If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay:

(150.00 / 5) * 1.12 = 33.6

After formatting the result to 2 decimal places = 33.60
'''
# Print a welcome message
print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

no_of_persons = int(input("How many people to split the bill? "))

# Get tip amount using the percentage tip * bill
tip_amount = (tip / 100) * bill

# Add tip_amount to bill
final_bill = tip_amount + bill

# Divide final_bill by no_of_persons to get what each person should pay
each_to_pay = final_bill / no_of_persons

# Round up each_to_pay to 2 decimal places as per requirement
each_to_pay = round(each_to_pay, 2)

# Print the output message with final_bill for each person
print(f"Each person should pay: ${each_to_pay}")
