'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

def threeSum(nums):
    list1 = []
    resultlist = []
    length = len(nums)
    i = 0
    j = 1
    k = 2
    while i<length-2:
        if nums[i] + nums[j] + nums[k] == 0:
            list1.append(nums[i])
            list1.append(nums[j])
            list1.append(nums[k])
            list1.sort()
            if list1 not in resultlist:
                resultlist.append(list1.copy())
                list1.clear()
        k+=1
        if k == length:
            j+=1
            k = j + 1
            if k == length:
                i+=1
                j = i + 1
                k = j + 1
    return resultlist

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))