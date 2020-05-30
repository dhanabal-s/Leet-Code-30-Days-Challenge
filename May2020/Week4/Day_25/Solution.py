class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:

        A = [ -1 ] + A
        B = [ -1 ] + B

        h, w = len(A), len(B)
        dp_table = [ [ 0 for _ in range(w) ] for _ in range(h) ]
        
                
        for y in range(1, h):
            for x in range(1, w):
                
                if A[y] == B[x]:
                    dp_table[y][x] = dp_table[y-1][x-1] + 1
                    
                else:
                    dp_table[y][x] = max( dp_table[y][x-1], dp_table[y-1][x] )

                    
        return dp_table[-1][-1]


Time Complexity : O(M*N)

Space Complexity : O(M*N)


