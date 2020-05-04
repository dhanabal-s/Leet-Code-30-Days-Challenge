# Method 1

# Check if i element of ransomNote in magazine
    # if change the ransomNote[i] in magazine into undefined magazine char
    # else return false
#if all are there return true

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(ransomNote)):
            if(magazine.find(ransomNote[i])>=0):
                magazine = magazine.replace(ransomNote[i],'~',1)
            else:
                return False
        return True
        
Time Complexity : O(len(ransomNote)*len(magazine))
Space Complexity : O(1)


# Method 2
# Using count the number of each char in a magazine
# check no.of char in ransomNote is present in a magazine
# if return True
# else False


import string
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        strs = string.ascii_lowercase
        alpha = list(map(magazine.count,strs))
        for i in ransomNote:
            if (alpha[ord(i)-97] >0):
                alpha[ord(i)-97] -= 1
            else:
                return False
        return True
        
