# Using, Binary search we will find the first bad version effectively.
# Find the mid, then check it is good or bad
# if it is Bad, 
    # then check if it equal to mid true 
        #  return mid 
    # else 
        # change end
# else
     # change the start
class Solution:
    def firstBadVersion(self, n):
        start,end = 1,n
        while(True):
            mid = math.floor((start+end)/2)
            if(isBadVersion(mid)):
                if(mid == start):
                    return mid
                else:
                    end = mid
            else :
                start = mid +1
        
Time Complexity : O(logN)
Space Complexity : O(1)
    
# Inbuilt function given by leetcode 
def isBadVersion(n):
  if(n>=firstBadVersion):
     return True
  else:
     return False
 
 # getting no.of version and first bad version
 noOfVersion, firstBadVerion = int(input().split())
 
 firstBadVersion(noOfVersion)
