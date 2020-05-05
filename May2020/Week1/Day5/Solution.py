# Count the no.of time each char occured in a string using Counter()
# Iter from string check the char occured time is equal to 1 return 1
# else return -1

from collections import OrderedDict,Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        order = Counter(s)
        # Manual implement of count
        '''order = OrderedDict()
        for i in s:
            order[i] = order.get(i,0)+1'''
            
        for i in range(len(s)):
            if(order[s[i]] == 1):
                return i
        return -1
        
Time Complexity : O(N)
Space Complexity : O(N)<br/>

