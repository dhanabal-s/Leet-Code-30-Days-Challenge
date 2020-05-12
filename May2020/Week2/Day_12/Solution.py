# you can solve this using binary search algorithm
Note : you can directly use the binary search algo. if they ask to find the number in a sorted list

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        while(start<end):
            mid = int ((start+end+1)/2)
            if(nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]): return nums[mid]
            if(nums[mid-1] == nums[mid]): mid-=1
            if((mid-start)%2 == 0): start=mid+2
            else: end=mid-1
        return nums[start]
        
Time Complexity : O(logN)
Spce Complexity : O(1)

# Using Xor

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        nonDuplicate = 0
        for num in nums:
            nonDuplicate ^= num
        return num
        
Time Complexity : O(N)
Space Complexity : O(1)


