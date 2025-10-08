"""
<7 kyu> "Center yourself", says the monk.
https://www.codewars.com/kata/596b8a3fc4cb1de46b000001

Your company MRE Tech has hired a spiritual consultant who advised on a new Balance policy: Don't take sides, don't favour, stay in the middle. This policy even applies to the software where all strings should now be centered. You are the poor soul to implement it.

Task
Implement a function center that takes a string strng, an integer width, and an optional character fill (default: ' ') and returns a new string of length width where strng is centered and on the right and left padded with fill.

center(strng, width, fill=' ')
If the left and right padding cannot be of equal length make the padding on the left side one character longer.

If strng is longer than width return strng unchanged.

Examples:
center('a', 3)  # returns " a "
center('abc', 10, '_')  # returns "____abc___"
center('abcdefg', 2)  # returns "abcdefg"
"""
#Solution
def center(strng, width, fill=' '):
    if len(strng) >= width:
        return strng

    total_padding = width - len(strng)
    left_padding = (total_padding + 1) // 2 
    right_padding = total_padding // 2

    return fill * left_padding + strng + fill * right_padding


#Function call
str = center('a', 3)  
print(str)
str = center('abc', 10, '_')  
print(str)
str = center('abcdefg', 2)  
print(str)


#Output
"""
 a 
____abc___
abcdefg

"""