# Add the all the elements of jewels in set.
# Iter through stone 
     #if that stone present in set increase count

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set()
        count = 0
        
        for i in J:
            jewels.add(i)
        
        for i in S:
            if i in jewels:
                count +=1
        return count
        
Time Complexity : O(len(J)+len(S))
Space Complexity : O(len(J))
