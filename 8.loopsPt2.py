# LOOPS PT.2 - WHILE LOOPS

# reminder: a for loop is deterministic - when you start the first iteration of the loop, you (almost always) know exactly how many iterations it will perform.
# a while loop, on the other hand, is non-deterministic - when you start you don't know how many loops you'll do - you simply loop whilst a condition holds.
# this might seem like a weird example, but is pretty much the most common use for them: I want to loop until the user inputs the word "hello":

word = None
while word != "hello":
    word = input("please enter \"hello\" to terminate - entering anything else will make me ask again: ")

# note: we have to initialise the variable `word` to `None` (a special value basically meaning undefined) before using it in the loop condition.

# try below to create a while loop that will keep going until the user enters a value more than 1000:






# run the program

# try below to create an infinite loop - this is occasionally useful:






# run the program

# END OF LESSON