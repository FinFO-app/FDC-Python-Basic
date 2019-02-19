"""
sec: 02
topic: 02
name: IF Statement
author: Faisal Manzer
"""

"""If works with boolean."""
if True:
    print("Condition is always True")

if False:
    print("Will never run")

name = input("Enter you name: ")
age = int(input("{} enter your age: ").format(name))

if age >= 18:
    print("You are old enough to vote")
    print("We request you to cast your vote")
else:
    print("Sorry {}, you can't vote".format(name))
    print("Wait for {} years to cast vote".format(18 - age))
