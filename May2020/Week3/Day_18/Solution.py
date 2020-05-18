class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)):
            return False
        fir = [0]*26
        sec = [0]*26
        def charToIndex(char):
            return ord(char)-ord('a')
        for i in range(len(s1)):
            index = charToIndex(s1[i])
            fir[index] +=1
            index = charToIndex(s2[i])
            sec[index] +=1
        if(fir == sec):
            return True
        for i in range(len(s1),len(s2)):
            index = charToIndex(s2[i-len(s1)])
            sec[index] -=1
            index = charToIndex(s2[i])
            sec[index] +=1
            if(fir == sec):
                return True
        return False
        
Time Complexity : O(L1+26*(L2-L1)) 

Space Complexity : O(1)


