class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = " "+word1
        word2 = " "+word2        
        len1 = len(word1)
        len2 = len(word2)
        
        dis = [[None]*len1 for i in range(len2)]
        for i in range(len1):
            dis[0][i] = i
        for i in range(len2):
            dis[i][0] = i

        for i in range(1,len2):
            for j in range(1,len1):
                if(word1[j] == word2[i]): dis[i][j]=dis[i-1][j-1]
                else : dis[i][j] = min(dis[i-1][j-1],dis[i][j-1],dis[i-1][j])+1
        return dis[-1][-1]
        
        
Time Complexity : O(M*N) , M & N are length of word1 and word2.

Space Complexity : O(M*N)


