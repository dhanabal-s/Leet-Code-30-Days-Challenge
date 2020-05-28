class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        result = []
        i = j = 0

        while i < len(A) and j < len(B):
            
            low = max(A[i][0], B[j][0])
            high = min(A[i][1], B[j][1])
            if low <= hi: result.append([low, high])
            if A[i][1] < B[j][1]: i += 1
            else: j += 1

        return result
        
Time Complexity : O(M+N)

Space Complexity : O(M+N)

