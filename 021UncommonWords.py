'''
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"

Output: ["sweet","sour"]

Explanation:

The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:

Input: s1 = "apple apple", s2 = "banana"

Output: ["banana"]

 

Constraints:

1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.
'''

def uncommonFromSentences(s1,s2):
    list1 = s1.split()
    list2 = s2.split()
    length1 = len(list1)
    length2 = len(list2)
    result = []
    if length1==length2:
        for i in range(length1):
            if list1[i]!=list2[i]:
                result.append(list1[i])
                result.append(list2[i])
    elif length1>length2:
        i = 0
        while i<length2:
            if list1[i]!=list2[i]:
                result.append(list1[i])
                result.append(list2[i])
            i+=1
        for j in range(i,length1):
            result.append(list1[j])
    else:
        i = 0
        while i<length1:
            if list1[i]!=list2[i]:
                result.append(list1[i])
                result.append(list2[i])
            i+=1
        for j in range(i,length2):
            result.append(list2[j])
    return result

#s1 = "apple apple"
#s2 = "banana"
s3 = "this apple is sweet"
s4 = "this apple is sour"
print(uncommonFromSentences(s3,s4))