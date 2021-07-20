# CONDITIONALS!

# currently, our programs don't branch, so no logic can occur
# let's change this...

# we need conditionals, starting with `if`s
# `if` statements take the form:
# `if {CONDITION}:`

# for example:
if 1 == 1:
    print("hi")
    print("moo")
    print("heya!")
# note: checking if `a` equals `b` is done using `a == b`, NOT `a = b`

# Quiz Time!
# for each of these, try to work out what will be printed out
# I've not taught you `else` and `elif`, but don't worry - you'll get it

if True:
    print("a")

if False:
    print("b")

if True == False:
    print("c")

if True == True:
    print("d")

if (1 == 2) == False:
    print("e")

# `!=` means not equals
if 1 != 2:
    print("f")

if True:
    print("g")
else:
    print("h")

if True:
    print("i")
elif False:
    print("j")
else:
    print("k")

if 1 == 2:
    print("l")
elif 3 == 4:
    print("m")
elif 5 == 6:
    print("n")
else:
    print("o")

# run the program and see if you were right!
# if you got any wrong, let me know and I'll try to explain

# syntactic sugar time:
# if you only need a single line inside an `if` statement, you can do the following:
print("moo") if True else print("baa")

# a useful example (`%` is the modulo operator)
num = 4
numOddEven = "even" if num % 2 == 0 else "odd"
# note modulo can be useful for modular aritmetic too:
# eg:
for x in range(100):
    y = x % 3
    print(x+y)
    # etc.


# test yourself - write a program (call it `nameCheck.py`) that asks the user for their name, then their age, then their favourite number. If their name is "Anna", tell them they're a silly billy, if their name is "Josh", tell them they're a god. Otherwise, tell them what their age times their favourite number is.
# test it thoroughly, and when you're happy with it, send it to me

# END OF LESSON