# LISTS!

# in lesson 3, we briefly encountered lists
# in many programming languages, we have things called arrays - you may have encountered them before - they can hold a fixed number of a single type of object (we're a bit off object oriented programming yet, so just think a single type of value, eg. an integer or a float, etc.)
# lists are what you use in python in place of an array - they are possibly a bit less efficient, but are far more versatile as a result
# they are denoted by [square brackets], with each entry inside being comma separated

# note: there are many examples here - I recommend regularly running the program (even better, in interactive mode (`-i` flag, see lesson 2)) so you can see how they work, and maybe play around a bit

# to create an empty list:
emptyList = []
print(emptyList)

# to create a list that has stuff in it:
populatedList = [1,2,3,"hi"]
print(populatedList)
# note: `populatedList` can be pre-defined or not - Python doesn't care

# adding an element to a list is called "appending":
populatedList.append("good morrow!")
print(populatedList)

# to remove the last element of a list, we pop it:
populatedList.pop()
print(populatedList)

# to remove another index, we can tell it which to pop:
populatedList.pop(0)
print(populatedList)
# note: python uses zero-indexing, so 0 is the position of the first element, 1 is the second, and so on

# speaking of indexing, we can use it to get the value of a particular element of a list - surround an integer with square brackets directly after a list (or, indeed a string, etc.) to get the value at a particular index:
newList = ["zero","one","two","three","four","five"]
print(newList[0])
print(newList[1])
print(newList[2])
print(newList[3])
print(newList[4])
print(newList[5])

# if we want to do the above, we can actually do it better using loops:
for i in range(len(newList)):
    print(newList[i])
# the `len()` function returns the length of a list (again, or string, etc.) as an integer, and the rest is syntax you're already aware of (if not, revisit lesson 7)

# there is an even better way to do loops over lists that will suit your purposes in many cases:
for item in newList:
    print(item)
# `item` can be whatever you want, so choose a name that makes sense - for example if looping over a list of the names of people, `names`, then you might do:
# `for name in names:`

# you can also use the `in` operator to test if an element is in an array:
if "zero" in newList:
    print("found zero!")

# we can also slice lists:
print(newList[0:2])
# note the first entry is inclusive and the second is exclusive

# you can actually drop the first entry if you want to go from 0:
print(newList[:2])
# and you can drop the last entry if you want to go to the end:
print(newList[3:])

# you can also negatively index:
print(newList[-2])
# the above will print the second last element, for example

# apart from `append()` and `pop()`, all the stuff discussed above actually works on strings too!

# using a lot of your skills so far, here's a fun challenge - try to write a program that when run keeps asking the user if they want to enter another number. If they say "yes", then ask them for a number. When they say "no", print out all the numbers, then also tell the user what the sum of all their numbers is. (Make sure it works if they just enter "no" immediately!) If you encounter challenges, Google and StackOverflow are your friends, and maybe come back to it tomorrow if it's still not working. If you really can't get it done, let me know and I'll happily help :)

# send me the program when it's done

# and finally, you can use the `index()` method to get the index of an element in an array, if exists - if doesn't, you'll get an error (you can avoid this by, for example, checking using `in` first)
print(newList.index("two"))

# END OF LESSON