"""
sec: 02
topic: 01
name: String Formatting
author: Faisal Manzer
"""

"""Code Block"""

# Code block in python is indented by whitespace
# Generally we use TAB or 4 SPACES
for i in range(1, 11):
    print("{:2} squared = {:3}".format(i, i**2))

# Multiple Blocks
age = int(input("Enter Age: "))
if age >= 18:
    print("You can VOTE.")
else:
    print("You can't VOTE.")

# Blocks in side Block
for i in range(1, 11):
    if i % 2:
        print("{} is Even".format(i))
    else:
        print("{} is Odd".format(i))

"""IndentationError: expected an indented block"""
# if age >= 18:
#
# name = "James Bond"

# We Will write the logic of if afterwards
if age >= 18:
    pass
name = "James Bond"
