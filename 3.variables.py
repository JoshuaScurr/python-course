# VARIABLES!

# a variable is how you store data in progamming
# it can use upper and lowercase letters, as well as numbers, but can only start with a lowercase letter - the standard format is the following thisIsMyVariableName123, and should be kept to as rigidly as possible
# there are some reserved keywords in python, such as `if` or `list` - a safe assumption is if the variable name goes a different colour to all your other variable names, thats reserved and you need to use a different name
# variables are case sensitive


# for example, if I were a sheep farmer, and wanted to track how many sheep I had, I could do the following:

sheep = 5

# this is setting the variable `sheep` to the integer value `5`
# you can change the value of variables - what if two of the sheep had a baby?

sheep = 6

# the above works, but obviously requires knowing how many there were before - we might not always know that - they have another baby...

sheep = sheep + 1

# this is better, as it works for any number of sheep before
# we can make this a little prettier using syntactic sugar (stuff that makes code prettier) - one more baby!

sheep += 1

# and two deaths...

sheep -= 2

# and now every sheep clones itself

sheep *= 2

# the evil farmer sends half to the abattoir...

sheep /= 2

# you can print out anything, not just strings (kind of, but we'll ignore that for now, unless you want to know silly details - in which case let me know)
# eg. `print(5)` will print the number `5` to the terminal
# `print(sheep)` will print the value of `sheep` to the terminal - make the farmer buy some more sheep, then print out the current number to the terminal below:





# run the program and let me know what happened

# we've discussed integers above, and strings last time (they, too, can be assigned to variables, eg. `farmerName = "Bob Ross"`), but there are many other types, including:

# float/real, eg.
f1 = 4.567
f2 = 0.0
f3 = 1.23456789
f4 = -1.02

# boolean, eg.
b1 = True
b2 = False

# list - these will get their own lesson, but eg.
l1 = [1,2,3]
l2 = ["a","b","c"]
l3 = [1,"b",False,9.7]

# object instance - kind of a special thing, not important for now, but eg.
x = int()

# END OF LESSON