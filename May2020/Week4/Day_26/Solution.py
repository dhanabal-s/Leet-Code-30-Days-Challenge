class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        maxLen = 0
        count =  0
        container = {0:-1}
        for i in range(len(nums)):
            if(nums[i]): count+=1
            else : count-=1
            if(count in container): maxLen = max(i-container[count],maxLen)
            else: container[count] = i
        
        return maxLen
        

Time Complexity : O(N) 

Space Complexity : O(N)


