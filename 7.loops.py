# LOOPS...LOOPS...LOOPS...LOOPS...

# sometimes we want to do things multiple times in a row - a loop
# there are two types of loop: for and while

# a for loop is deterministic - when you start the first iteration of the loop, you (almost always) know exactly how many iterations it will perform; you may wish to print out "hello" 5 times:

for _ in range(5):
    print("hello")

# the syntax of this may look a little weird, but it'll make more sense soon.
# the `for` and `in` are basically just to indicate we're doing a for loop
# the `_` indicates we don't actually care what number of iteration we're currently on
# `range()` is a function - it takes up to three parameters and returns an iterable sequence of numbers, but we will discuss this in a minute

for x in range(3,99,5):
    print(x)

# the above uses all parameters of `range()`, and also uses the value from `in`
# it will print:
#   3
#   8
#   13
#   18
#   ...
#   93
#   98

# as you can probably work out, when using all three parameters of `range()`, the first is the start value (inclusive), the second is the end value (exclusive), and the third is the step size
# if you only use one parameter, it's just the end value (exclusive)
# if you use two, the first is the start value (inclusive) and the second is the end value (exclusive)

# try below to write some code that will ask the user for a positive number, then print out all the numbers from 0 to that number, INCLUSIVELY







# run the program and check it works
# if you encounter an error, try to read through it and understand where you went wrong (this is an essential part of programming - it's totally normal to encounter errors (more to the point, almost impossible to not encounter them), so understanding them is key) - if reading through it doesn't help, try Googling it (with some context, if nothing useful shows up initially), maybe looking for results from StackOverflow; if nothing helps, then try contacting me

# END OF LESSON