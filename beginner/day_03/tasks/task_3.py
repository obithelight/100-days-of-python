# Nesting and Elif
'''
You can put if/else statements inside other if/else statements. This is known as nesting. e.g.
'''
maths_score = int(input("What did you score in math? "))
english_score = int(input("What did you score in english? "))

if maths_score >= 90:
    if english_score >= 90:
        print("You're good at both english and maths.")
    else:
        print("You're good at maths.")
elif english_score >= 90:
    print("You're good at english.")
else:
    print("Work hard to improve your english and math scores.")
'''
In this case only when a student has over 90 on maths and english, do they get "You are good at everything".
'''
# Note: You can also have if statements that don't have a paired else statement.
