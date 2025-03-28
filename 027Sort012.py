'''
Sort an array of 0s, 1s and 2s
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.


Example 1:

Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated 
into ascending order.
Example 2:

Input: 
N = 3
arr[] = {0 1 0}
Output:
0 0 1
Explanation:
0s 1s and 2s are segregated 
into ascending order.

Your Task:
You don't need to read input or print anything. Your task is to complete the function sort012() that takes an array arr and N as input parameters and sorts the array in-place.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 <= N <= 10^6
0 <= A[i] <= 2
'''

def sort012(inp):
    length = len(inp)
    m = 0
    i = 0
    k = length - 1
    while m<=k:
        if inp[m] == 0:
            inp[m],inp[i] = inp[i],inp[m]
            i+=1
        elif inp[m] == 2:
            inp[m],inp[k] = inp[k],inp[m]
            k-=1
            m-=1
        m+=1
        
#inp = [0,0,1,2,1,0]
#inp = [0,1,0]
inp = [2,2,1,0,1,0]

print(inp)
sort012(inp)
print(inp)