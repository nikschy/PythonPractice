'''
Find Indexes of a subarray with given sum

Given an unsorted array A of size N that contains only non negative integers, find a continuous sub-array that adds to a given number S and return the left and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.

Note:- You have to return an ArrayList consisting of two elements left and right. In case no such subarray exists return an array consisting of element -1.

Example 1:

Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.
Example 2:

Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements 
from 1st position to 5th position
is 15.
Your Task:
You don't need to read input or print anything. The task is to complete the function subarraySum() which takes arr, N, and S as input parameters and returns an ArrayList containing the starting and ending positions of the first such occurring subarray from the left where sum equals to S. The two indexes in the array should be according to 1-based indexing. If no such subarray is found, return an array consisting of only one element that is -1.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 105
0 <= Ai <= 109
0<= S <= 109
'''


def FindSub(a,S):
    result = [-1]
    i = j = 0
    length = len(a)
    sumSub = 0
    while j<=length or i!=j:
        if sumSub<S:
            sumSub+=a[j]
            print(f"2. i: {i}, j: {j}, a[j]: {a[j]}, sumSub: {sumSub}")
            j+=1
        elif sumSub>S:
            sumSub-=a[i]
            i+=1
        else:
            result[0] = i+1
            result.append(j)
            break
        print("-------------")
    return result

a = [1,2,56,48,74,59,23,15,10,48,3,4,5]
S = 3

print(FindSub(a,S))