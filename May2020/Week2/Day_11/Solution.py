class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row,col = len(image),len(image[0])
        startColor = image[sr][sc]
        if startColor == newColor: return image
        def changeColor(sr,sc):
            if(image[sr][sc] == startColor):  
                image[sr][sc] = newColor
                if(sr>=1): changeColor(sr-1,sc)
                if(sr+1<row): changeColor(sr+1,sc)
                if(sc>=1): changeColor(sr,sc-1)
                if(sc+1<col): changeColor(sr,sc+1)
        
        changeColor(sr,sc)
        return image
        
Time Complexity : O(N)
Space Complexity : O(N)

