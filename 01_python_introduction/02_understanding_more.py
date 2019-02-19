"""
sec: 01
topic: 02
name: Understanding More
author: Faisal Manzer
"""

"""Define a variable with '='."""
greeting = "Hello"

"""Variable should be used used without quotes"""
print(greeting)

"""Input from keyboard is from 'input'."""
name = input("Enter your name: ")

"""Concatenate with '+'."""
print(greeting + ' ' + name)
# Space added

"""Did You Noticed '#'. That is used to make single line comment."""
"""To comment a line use `CMD + Tab` (MacOS) or `Ctrl + Tab` (Linux and Windows)"""

"""There are also escaped character in string. ex: \n."""
print("First Line\nSecond Line\nDid you noticed text spanned in many lines?")

"""Can Also Use tab. say \t"""
print("1.\tHello\tWorld")

"""Double Quote can be escaped within Double Quotes. Same for single quotes."""
print("We Will print \"quotes\" like this. See that backslash")
print('XYZ\'s car is expensive')


"""The TRIPLE QUOTES is used to split string in several line"""
long_para = """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""

print(long_para)
'''This also works'''
