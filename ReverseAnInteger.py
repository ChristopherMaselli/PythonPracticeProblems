'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21
'''

input = 120

def reverse(num):
    # Check if it is negative
    neg = False
    # Set to absolute value
    # turn into a string
    # Reverse the values
    # apply negatives if negative

    if num < 0:
        neg = True
        num = -1*num
    revnum = str(num)[::-1]
    num = int(revnum)
    if neg == True:
        num = num*-1
    print(num)
reverse(input)