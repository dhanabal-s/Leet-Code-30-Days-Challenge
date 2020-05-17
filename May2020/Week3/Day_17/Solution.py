class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if(len(s)<len(p)):
            return []
        def charToIndex(char):
            return ord(char)-ord('a')
        result = []
        pCount = [0]*26
        sCount = [0]*26
        for i in range(len(p)):
            index = charToIndex(p[i])
            pCount[index]+=1
            index = charToIndex(s[i])
            sCount[index]+=1
        if(sCount == pCount):
            result.append(i-len(p)+1)    
        for i in range(len(p),len(s)):
            index = charToIndex(s[i])
            sCount[index]+=1
            index = charToIndex(s[i-len(p)])
            sCount[index]-=1
            if(sCount == pCount):
                result.append(i-len(p)+1)
            
        return result
            
            
Time Complexity : O(N) N - length of string s

Space Complexity : O(k) k - number of anagram matchs

