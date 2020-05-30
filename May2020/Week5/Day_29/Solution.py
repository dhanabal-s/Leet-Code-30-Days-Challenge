from collections import defaultdict as dd
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edge=defaultdict(list)
        for p in prerequisites:
	        edge[p[0]].append(p[1]) 

        for k in range(numCourses):
            stack=[k]
            visit=set()
            while stack:
                node=stack.pop(0)
                if visit and node==k:     
                    return False
                if node not in visit:
                    visit.add(node)
                    stack+=edge[node]
        return True
        
        
        
