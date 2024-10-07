'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

def longestCommonPrefix(strs):
    lenlist = []
    for item in strs:
        lenlist.append(len(item))
    minlen = min(lenlist)
    result = ""
    items = len(strs)
    i = 0
    ok = 0
    while i<minlen:
        a = strs[0][i]
        ok = 0
        for item in strs:
            if item[i] == a:
                ok+=1
        if ok==items:
            result = result + a
        else:
            break
        i+=1
    return result

strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))