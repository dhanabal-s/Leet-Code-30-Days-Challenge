# Using slope of line formula

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0,y0),(x1,y1) = coordinates[:2]
        dx,dy = (x1-x0),(y1-y0)
        
        for x,y in coordinates:
            if(dy*(x-x1) != dx*(y-y1)): return False
        
        return True
        
Time Complexity : O(N)
Space Complexity : O(1)

# If you're good at mathematics, you will find it easily
# But, thinking as a programmer who bad at mathematics, i find the below soln.
# I solve the below, Program using Ratio 

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        xDiff = coordinates[0][0] - coordinates[1][0]
        yDiff = coordinates[0][1] - coordinates[1][1]
        
        gcd = math.gcd(xDiff,yDiff)
        xDiff = int(xDiff/gcd)
        yDiff = int(yDiff/gcd)
        
        for i in range(2,len(coordinates)):
            xNew = coordinates[0][0] - coordinates[i][0]
            yNew = coordinates[0][1] - coordinates[i][1]
            gcd = math.gcd(xNew,yNew)
            xNew = int(xNew/gcd)
            yNew = int(yNew/gcd)
            if(not(xDiff ==xNew and yDiff == yNew or xDiff == -xNew and yDiff == - yNew)):
                return False
        return True
        
Time Complexity : O(NlogN) N- coordinates lenght, logN- finding gcd()
Space Complexity : O(1)
