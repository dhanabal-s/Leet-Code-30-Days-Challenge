# convert the number into binary
# val = 0
# if binary[i] == 0
   # add 2 pow i to val
# return val

class Solution:
    def findComplement(self, num: int) -> int:
        binary = [] 
        
        if(num == 0):
            return 1
         # also use bin() build in function for find binary value
        while(num > 0):
            binary.append(num%2)
            num = int(num/2)
     
      
        for i in range(len(binary)):
            if(binary[i] == 0):
                num += 2**i
        
        return num
        
Time Complexity : O(logN)
Space Complexity :O(logN)

