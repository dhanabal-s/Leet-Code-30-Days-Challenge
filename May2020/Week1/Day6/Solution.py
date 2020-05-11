# Method-1
# Sort the give list, return the middle element of the list. Because majority element always greater [n/2].

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int(len(nums)/2)]
        
Time Complexity : O(NlogN)
Space Complexity : O(1)

# Method-2
# Count no.of occurence of each element in list using dict
# return the element if its count is greater than [n/2]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        eleCount = {}
        for ele in nums:
            eleCount[ele] = eleCount.get(ele,0)+1
            if(eleCount[ele] > int(len(nums)/2)):
                return ele

Time Complexity : O(N)
Space Complexity : O(N)

Note: if you apply both methods in a leetcode, method-1 beats more than 98% soln, but method-2 beats only a 30% soln. 
      Even method-2 big notaion smaller than method-1 (reason is input size). So, everyone is better than another in different situations.
      Real life also like that so, belive on youself, love youself. 

    
# Method-3
# using Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ele = None
        for num in nums:
            if(count == 0):
                ele = num
            count += (1 if(num == ele) else -1)
        return ele
