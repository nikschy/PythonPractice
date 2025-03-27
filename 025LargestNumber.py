'''
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
'''

def largestNumber(nums):
    num1 = nums.copy()
    print(num1)
    length = len(num1)
    for i in range(length-1):
        for j in range(i+1,length):
            Exchanged = False
            if str(num1[i])[0] < str(num1[j])[0]:
                k = num1[i]
                num1[i] = num1[j]
                num1[j] = k
            elif str(num1[i])[0] == str(num1[j])[0]:
                if len(str(num1[i])) > len(str(num1[j])):
                    m = 1
                    while m < len(str(num1[j])):
                        if str(num1[i])[m] < str(num1[j])[m]:
                            k = num1[i]
                            num1[i] = num1[j]
                            num1[j] = k
                            Exchanged = True
                            break
                        m+=1
                    if m == len(str(num1[j])) and str(num1[j])[m-1] > str(num1[i])[m] and not Exchanged and not (str(num1[i])[m-1] > str(num1[j])[m-1]):
                        k = num1[i]
                        num1[i] = num1[j]
                        num1[j] = k
                elif len(str(num1[i])) < len(str(num1[j])):
                    m = 1
                    while m < len(str(num1[i])):
                        if str(num1[i])[m] < str(num1[j])[m]:
                            k = num1[i]
                            num1[i] = num1[j]
                            num1[j] = k
                            Exchanged = True
                            break
                        m+=1
                    if m == len(str(num1[i])) and str(num1[i])[m-1] < str(num1[j])[m] and not Exchanged and not (str(num1[i])[m-1] > str(num1[j])[m-1]):
                        k = num1[i]
                        num1[i] = num1[j]
                        num1[j] = k
    inp = list(map(str,num1))
    result = "".join(inp)
    return result

nums = [2,10]
nums2 = [3,34,30,5,9]
nums3 = [3,34,30,325,9]
print(largestNumber(nums))
print(largestNumber(nums2))
print(largestNumber(nums3))