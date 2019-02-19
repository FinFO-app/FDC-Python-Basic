"""
@sec: 01
topic: 05
name: Strings
author: Faisal Manzer
"""

"""Strings are sequence of characters"""
name = "James Bond"

print(name[2])  # m 
print(name[-3])  # o

# We count from 0 (zero)
# index:    0 1 2 3 4 5 6 7 8 9
# values:   J a m e s   B o n d
# negative: -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# variable[index]

"""Slicing A String"""
print(name[6:10])  # Bond
print(name[::-1])  # dnoB semaJ
print(name[2:7:2])  # msB
print(name[-7:-2:1])  # es Bo
print(name[::-3])  # dBeJ

# variable[from:to:step]
# `from` is inclusive, ie: Count that two
# `to` is exclusive, ie: Count till one place before
# `step` is to skip `n-1` char
# if you skip `from` then it is `0` (zero)
# if you skip `to` then it is the `total length`
# All `from`, `to`, `step` con be negative also


numbers = "1, 2, 3, 4, 5, 7, 8, 9"
print(numbers[::3])  # 123456789

"""Concatenation"""

# "xyz" "abc"
# "xyz" + "abc"
# string1 + string2     [string1 & string2 are variables]
# string1 "abc"         [NOT ALLOWED]
# "abc" * 4             [abcabcabcabc]


"""The `in` operator"""

print("James" in name)  # True
print("james" in name)  # False
print("z" in name)  # False
print("James Bond is great in movie" in name)  # False
print(name in "James Bond is great in movie")  # True
print(name in "James Bond")  # True
