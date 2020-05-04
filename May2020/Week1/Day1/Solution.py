# Using, Binary search we will find the first bad version effectively.
# Given version is bad, check it is starting version if return it, else change it as a end bad verion and do the same steps again.
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
           
# Inbuilt function given by leetcode 
def isBadVersion(n):
  if(n>=firstBadVersion):
     return True
  else:
     return False
 
 # getting no.of version and first bad version
 noOfVersion, firstBadVerion = int(input().split())
 
 firstBadVersion(noOfVersion)
