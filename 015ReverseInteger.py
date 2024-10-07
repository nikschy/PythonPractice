'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-2^31 <= x <= 2^31 - 1
'''

def reverse(x):
    m = x
    if m<0:
        m*=-1
    num = str(m)
    num = num[::-1]
    if x<0:
        num = -1*int(num)
    else:
        num = int(num)
    return num

#x = 123
#x = -321
x = -120
print(reverse(x))