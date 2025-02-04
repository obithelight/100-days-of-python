'''
Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x weeks left.

Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

Example Input
56

Example Output
You have 1768 weeks left.

life_in_weeks(12)
'''

def life_in_weeks():
    current_age = int(input("How old are you? "))
    time_left_in_years = 90 - current_age
    time_left_in_weeks = time_left_in_years * 52
    message = f"You have {time_left_in_weeks} weeks left."
    print(message)

life_in_weeks()
