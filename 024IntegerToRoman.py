'''
Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
Example 2:

Input: num = 58

Output: "LVIII"

Explanation:

50 = L
 8 = VIII
Example 3:

Input: num = 1994

Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV
 

Constraints:

1 <= num <= 3999
'''

def intToRoman(num):
    result = ""
    times = 0
    print(num)
    if num>=1000:
        times = num//1000
        for i in range(times):
            result = result + "M"
        num = num%1000
    if num>=900:
        result = result + "CM"
        num = num%100
    if num>=500:
        result = result + "D"
        times = num//100-5
        for i in range(times):
            result = result + "C"
        num = num%100
    if num>=400:
        result = result + "CD"
        num = num%100
    if num>=100:
        times = num//100
        for i in range(times):
            result = result + "C"
        num = num%100
    if num>=90:
        result = result + "XC"
        num = num%10
    if num>=50:
        result = result + "L"
        times = num//10-5
        for i in range(times):
            result = result + "X"
        num = num%10
    if num>=40:
        result = result + "XL"
        num = num%10
    if num>=10:
        times = num//10
        for i in range(times):
            result = result + "X"
        num = num%10
    if num>=9:
        result = result + "IX"
    elif num>=5:
        result = result + "V"
        times = num-5
        for i in range(times):
            result = result + "I"
        num = num%10
    elif num==4:
        result = result + "IV"
        num = num%10
    elif num>=1:
        times = num
        for i in range(times):
            result = result + "I"
        num = num%10
    return result

num = 1994
print(intToRoman(num))