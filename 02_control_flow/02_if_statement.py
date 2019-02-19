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

"""The classical example"""

name = input("Enter you name: ")
age = int(input("{} enter your age: ").format(name))

if age >= 18:
    print("You are old enough to vote")
    print("We request you to cast your vote")
else:
    print("Sorry {}, you can't vote".format(name))
    print("Wait for {} years to cast vote".format(18 - age))

"""Caution"""

condition = "False"
if condition:
    print("condition is true")
else:
    print("condition is false")

# output: condition is true
# in python every `non zero` and `non int` values are true
#
