## Sum
Python has lots of built-in functions to help us work with numbers. One of them helps us calculate the sum (the total). e.g.

```
student_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = sum(student_scores) 
```

But how does ```sum()``` work behind the scenes? The code is written by the people who developed Python and it might look something like this:

```
student_scores = [180, 124, 165]

sum = 0
for score in student_scores:
    sum += score

print(sum)
```

## Max
There are also a built-in Python methods called ```max()``` and ```min()```, which allow you to pass in a List of numbers, and it will give you the highest number or the lowest number.

Your job is to figure out how the Python programmers might have built this functionality using loops and conditionals.
