class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        first = [i for i,j in costs]
        diff = [j-i for i,j in costs]
        
        return sum(first)+sum(sorted(diff)[:len(diff)//2])
    
    
Time Complexity : O(NlogN) 

Space Complexity : O(2*N) 


