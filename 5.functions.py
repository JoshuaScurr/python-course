# FUNCTIONS!

# functions are a core bit of programming - they allow you to reuse bits of code that you (or someone else) have already written, and are the basis of how most modern programming is performed (including in python)

# you have actually already used two functions - `print()` and `input()` - anything that is a name and then a set of brackets is a function
# some terms:
    # "parameters" - the things you can input/parse into a function - in the example of `print()`, this is the string to output, eg. in `print("hello")`, `"hello"` is the value parsed to the first parameter of the function `print()`
    # "return value" - the value the functon gives back after it's finished - in the case of `input()`, this is a string of whatever the user entered, eg. in `name = input("enter your name: ")`, if the user enters "Bob", then the return value of the function call would be `"Bob"` - this should hopefully become clear with some more examples
    # "function body" - the code "inside the function" - I'll point this out in a minute
    # "call a function" - run a function


# example function - add two numbers together
def aPlusB(a, b):
    total = a + b
    return total

# the `def` keyword tells python that what is coming is a function declaration
# `aPlusB` is the name of the function
# `(a,b)` indicates that `a` and `b` are the two parameters for the function
# the `:` is just necessary - python wants it, so do it..!
# the body of the function is:
# ```
#     total = a + b
#     return total
# ```
# (stuff surrounded by ```triple backticks``` indicates multiple lines of code in a comment)
# the body is indented one level in from the definition line, and is it's own scope - the variable `total` doesn't exist outside of lines 15 and 16, and `a` and `b` don't exist outside of lines 14-16, so we can do this:
a = 5
b = 7
total = 100000000.124578
# and this will not affect the operation of the function `aPlusB()` at all, and calling `aPlusB()` will not affect the `a`,`b`,`total` we just defined

# using `aPlusB()`, write some code below that will receive input of two separate numbers from the user, then adds them together, printing the result:





# run the program

# ...

# not what you expected?
# Certainly not what I instructed you to do (unless you've very sneaky and already know this) - as I've already mentioned in `4.input.py`, `input()` returns a string. Adding two strings together is called concatenation, and just merges the second one onto the end of the first - eg. `"hel" + "lo"` => `"hello"`
# to actually add the number together, we need to turn the strings received as input into numbers (we'll assume integers, but if you want to use any number, then replace `int()` with `float()`)

# the function `int()` tries to create an integer value from whatever it is given (in this case a string) - `int("1")` => `1`, `int("-7")` => `-7`, etc.

threeAsInt = int("3")

# using this newfound knowledge, modify your code to actually add two numbers together, and check it works by running the program (I know you're good at maths, so you should be able to check it's correct...)

# END OF LESSON