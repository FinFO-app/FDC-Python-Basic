"""
sec: 01
topic: 06
name: String Formatting
author: Faisal Manzer
"""

"""Type Conversion"""
matches_won = 3
team_name = "liverpool"

# print(team_name + " won " + matches_won + " matches")  # Error: TypeError
print(team_name + " won " + str(matches_won) + " matches")  # liverpool won 3 matches

# `str` FUNCTION changes type of int to str
# can change any into string

"""Formatting String with `format()`"""
print("{0} won {1} matches".format(team_name, matches_won))
print("{} won {} matches".format(team_name, matches_won))

# `format` is an METHOD which maps
# The string format() method formats the given string into a nicer output.

# team_name     matches_won
# {0}           {1}
# respective index will take its value

# format automatically convert values to string.

print("Hello {0}, your balance is {1:9.3f}".format("Adam", 230.2346))
# Hello Adam, your balance is   230.235

# Here, Argument 0 is a string "Adam" and Argument 1 is a floating number 230.2346.
# The string "Hello {0}, your balance is {1:9.3f}" is the template string.
# This contains the format codes for formatting.
#
# The curly braces are just placeholders for the arguments to be placed.
# In the above example, {0} is placeholder for "Adam" and {1:9.3f} is placeholder for 230.2346.
#
# Since the template staring references format() arguments as {0} and {1},
# the arguments are positional arguments.
# They both can also be referenced without the numbers as {} and Python internally converts them to numbers.

# HOW THAT WORKED
# Since "Adam" is the 0th argument, it is placed in place of {0}.
# Since, {0} doesn't contain any other format codes, it doesn't perform any other operations.
# However, it is not the case for 1st argument 230.2346.
# Here, {1:9.3f} places 230.2346 in its place and performs the operation 9.3f.
# f specifies the format is dealing with a float number.
# If not correctly specified, it will give out an error.
# The part before the "." (9) specifies the minimum width/padding the number (230.2346) can take.
# In this case, 230.2346 is allotted a minimum of 9 places including the ".".
# If no alignment option is specified, it is aligned to the right of the remaining spaces.
# (For strings, it is aligned to the left.)
# The part after the "." (3) truncates the decimal part (2346) upto the given number.
# In this case, 2346 is truncated after 3 places.
# Remaining numbers (46) is rounded off outputting 235.

# ---------------------------------------------------------------------
# https://www.programiz.com/python-programming/methods/string/format  |
# ---------------------------------------------------------------------

"""Numbers formatting with format()"""
# d	Decimal integer
# c	Corresponding Unicode character
# b	Binary format
# o	Octal format
# x	Hexadecimal format (lower case)
# X	Hexadecimal format (upper case)
# n	Same as 'd'. Except it uses current locale setting for number separator
# e	Exponential notation. (lowercase e)
# E	Exponential notation (uppercase E)
# f	Displays fixed point number (Default: 6)
# F	Same as 'f'. Except displays 'inf' as 'INF' and 'nan' as 'NAN'
# g	General format. Rounds number to p significant digits. (Default precision: 6)
# G	Same as 'g'. Except switches to 'E' if the number is large.
# %	Percentage. Multiples by 100 and puts % at the end.

# <	Left aligned to the remaining space
# ^	Center aligned to the remaining space
# >	Right aligned to the remaining space
# =	Forces the signed (+) (-) to the leftmost position

"""Formatting string with %"""

print("%s won %d matches" % (team_name, matches_won))

# %c	character
# %s	string conversion via str() prior to formatting
# %i	signed decimal integer
# %d	signed decimal integer
# %u	unsigned decimal integer
# %o	octal integer
# %x	hexadecimal integer (lowercase letters)
# %X	hexadecimal integer (UPPERcase letters)
# %e	exponential notation (with lowercase 'e')
# %E	exponential notation (with UPPERcase 'E')
# %f	floating point real number
# %g	the shorter of %f and %e
# %G	the shorter of %f and %E

# *	argument specifies width or precision
# -	left justification
# +	display the sign
# <sp>	leave a blank space before a positive number
# #	add the octal leading zero ( '0' ) or hexadecimal leading '0x' or '0X', depending on whether 'x' or 'X' were used.
# 0	pad from left with zeros (instead of spaces)
# %	'%%' leaves you with a single literal '%'
# (var)	mapping variable (dictionary arguments)
# m.n.	m is the minimum total width and n is the number of digits to display after the decimal point (if appl.)
