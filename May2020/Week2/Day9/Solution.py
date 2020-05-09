# We don't use sqrt.
# Soln in user Solution 

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if(num == 0):
            return False
        for root in range(1,num+1):
            if(root * root == num): return True
            elif(root * root > num): return False

Time Complexity : O(sqrt(N)+1)
Space Complxity : O(1)

# Using power
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        val = int(num ** 0.5)
        return num != 0 and  val**2 == num
        
Time Complexity : O(n)
Space Complexity : O(1)

   
