class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix)+1
        col = len(matrix[0])+1
        subMatrix = [[0]*col for _ in range(row)]
        total = 0
        
        for i in range(1,row):
            for j in range(1,col):
                if(matrix[i-1][j-1] == 0):
                    subMatrix[i][j]=0
                else:
                    subMatrix[i][j] = min(subMatrix[i][j-1],subMatrix[i-1][j],subMatrix[i-1][j-1])+1
                total +=subMatrix[i][j]
        return total
        
Time Complexity : O(M*N)

Space Complexity : O((M+1)*(N+1))


