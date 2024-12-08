# Create a program using maths and f-Strings that tells u how many days, weeks, and months we have left if we live until 90 years old.

# Don't change the code below
age = input("What is your current age? ")
# Don't change the code above

# Write your code below this line

age = int(age)
max_age = 90

years_remaining = max_age - age
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."

# print the message
print(message)

