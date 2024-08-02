'''
Minimum number of jumps

Given an array of N integers arr[] where each element represents the maximum length of the jump that can be made forward from that element. This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.

Note: Return -1 if you can't reach the end of the array.


Example 1:

Input:
N = 11 
arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9} 
Output: 3 
Explanation: 
First jump from 1st element to 2nd 
element with value 3. Now, from here 
we jump to 5th element with value 9, 
and from here we will jump to the last. 
Example 2:

Input :
N = 6
arr = {1, 4, 3, 2, 6, 7}
Output: 2 
Explanation: 
First we jump from the 1st to 2nd element 
and then jump to the last element.

Your task:
You don't need to read input or print anything. Your task is to complete function minJumps() which takes the array arr and it's size N as input parameters and returns the minimum number of jumps. If not possible return -1.


Expected Time Complexity: O(N)
Expected Space Complexity: O(1)


Constraints:
1 ≤ N ≤ 107
0 ≤ arri ≤ 107
'''


def MinJumps(a):
    length = len(a)
    jump = 0
    i = 0
    while i<length:
        m = a[i]
        print(f"i: {i}, a[i]: {a[i]}, m:{m}")
        if m==0:
            jump = -1
            print(f"1. i: {i}, a[i]: {a[i]}")
            break
        elif i+m < length-1:
            jump+=1
            maxi = 0
            cnt = 1
            total = 0
            j = 0
            while i+cnt<=i+m:
                n = a[i+cnt]
                total = i+cnt+n
                if total>maxi:
                    maxi = total
                    j = i+cnt
                cnt+=1
            i = j
            print(f"2. i: {i}, a[i]: {a[i]}")
        elif i+m >= length-1:
            print(f"3. i: {i}, a[i]: {a[i]}")
            jump+=1
            break
        print("----------------")
    return jump

a = [1,3,0,0,1,7,5]
print("Minimum Jumps: ",MinJumps(a))