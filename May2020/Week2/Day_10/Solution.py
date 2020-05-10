
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        judges = set([i+1 for i in range(N) ])  # assume all peoples are judges
        trusted_person = [0]*N  # Count how many person trust particular person 
		
        for (truster,trusted) in trust:
            if(truster in judges): judges.remove(truster)  # if one person trust anoter one remove that person a judge
            trusted_person[trusted-1] += 1  # Counting each person trusted
        
        if(len(judges) == 1):  # return -1 if more judges are there
            judge = judges.pop() # if only one judge is remain check all the person trusted him
            if(trusted_person[judge-1]==N-1): return judge # return judge 
            else : return -1  # else return -1
        else : return -1
        
 Time Complexity : O(n)
 Space Complexity : O(2n)
 
