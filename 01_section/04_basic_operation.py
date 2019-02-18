"""
sec: 01
topic: 04
name: Basic Operations
author: Faisal Manzer
"""

"""Operator for int, float"""
# +     Addition
# -     Subtraction
# *     Multiplication
# /     Division
# %     Modulus
# **    Exponentiation
# //    Floor division

number1 = 20
number2 = 3

print(number1 + number2)  # 23
print(number1 - number2)  # 17
print(number1 * number2)  # 60
print(number1 / number2)  # 6.66...7 (will convert to float)
print(number1 % number2)  # 2
print(number1 ** number2)  # 8000
print(number1 // number2)  # 2 (only int)

"""Operators for str"""
string = "Hello"
print(string + "World")  # Hello World
print(string * 3)  # Hello Hello Hello
# print(string - "World")  # NOT APPLICABLE -> TypeError
# print(string / "Hello ")  # NOT APPLICABLE -> TypeError


"""Types of Operators"""
# Arithmetic operators  (+, -, *, /, %, **, //)
# Assignment operators  (=, +=, *=, /=, %=, //=, **=) [&=, |=, ^=, ~=, >>=, <<=]
# Comparison operators  (==, !=, >, <, >=, <=)
# Logical operators     (and, or, not)
# Identity operators    (is, is not)
# Membership operators  (in, not in)
# Bitwise operators     (&, |, ^, ~, >>, <<)
# https://www.w3schools.com/python/python_operators.asp

"""Operator Precedence: High -> Low"""
# **        [Exponentiation (raise to the power)]
# ~ +@ -@   [Complement, unary plus and minus (method names for the last two are +@ and -@)]
# * / % //  [Multiply, divide, modulo and floor division]
# + -       [Addition and subtraction]
# >> <<     [Right and left bitwise shift]
# &         [Bitwise `AND`]
# ^ |       [Bitwise exclusive `OR` and regular `OR`]
# <= < > >= [Comparison operators]
# <> == !=  [Equality operators]
# = %= /= //= -= += *= **=  [Assignment operators]
# is, is not                [Identity operators]
# in, not in                [Membership operators]
# not, or, and              [Logical operators]
# https://www.tutorialspoint.com/python/operators_precedence_example.htm


a = 20
b = 10
c = 15
d = 5

e = (a + b) * c / d  # ( 30 * 15 ) / 5
print("Value of (a + b) * c / d is ", e)  # 90

e = ((a + b) * c) / d  # (30 * 15 ) / 5
print("Value of ((a + b) * c) / d is ", e)  # 90

e = (a + b) * (c / d)  # (30) * (15/5)
print("Value of (a + b) * (c / d) is ", e)  # 90

e = a + (b * c) / d  # 20 + (150/5)
print("Value of a + (b * c) / d is ", e)  # 50
