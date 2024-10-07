'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

def lengthOfLongestSubstring(s):
    length = len(s)
    string = s[0]
    cnt = 1
    resultlist = [string,cnt]
    i = 1
    while i<length:
        if s[i] not in string:
            string = string + s[i]
            cnt+=1
        else:
            if cnt>resultlist[1]:
                resultlist[1] = cnt
                resultlist[0] = string
            string = s[i]
            cnt = 1
        i+=1
    return resultlist[1]

#s = "abcabcbb"
#s = "bbbbb"
s = "pwwkew"
print(lengthOfLongestSubstring(s))