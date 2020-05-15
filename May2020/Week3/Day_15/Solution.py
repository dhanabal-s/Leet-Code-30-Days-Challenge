class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def kande(A):
            maxVal,curMax = -float('inf'),-float('inf')
            for i in range(len(A)):
                curMax = max(curMax+A[i],A[i])
                maxVal = max(curMax,maxVal)
            return maxVal
        kandeSum = kande(A)
        total = sum(A)+kande([-A[i] for i in range(len(A))])
        return total if total>kandeSum and total!=0 else kandeSum
        
Time Complexity : O(N)
Space Complexity : O(1)


