"""
sec: 01
topic: 03
name: Variables
author: Faisal Manzer
"""

"""Rules for defining variable names"""
# Should only contain A-Z, a-z, 0-9, and _ (underscore)
# Should not start with number

"""Valid Names"""
greeting = "Hi, "
_greet = "Hi, "
greetUser = "Hi, "
greet_user = "Hi, "
Greeting = "Hi, "


greetuser = "Hi, " 
# Python is case sensitive, means: `greetUser` and `greetuser` are two different names
"""Invalid Names"""
# 1user = "User Name"

# -----------------------------------

"""Python is Dynamic typed language"""

"""String: str"""
user = "James Bond"

"""Integer: int"""
age = 24

"""Float: float"""
interest = 6.5

"""Boolean: bool"""
is_logged = True


"""Can add same type of variable"""
print(greet_user + user)
print(age + 6)
print(interest - 5)  # int(5) converted to float
print(is_logged + False)  # Boolean converted to int

"""Notes on type conversion"""
# int -> float
# bool -> int

"""Not of same type will give error."""
# print(greeting + 1) # str + int -> TypeError
