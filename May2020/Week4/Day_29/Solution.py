class Solution:
    def countBits(self, num: int) -> List[int]:
        bitArr = [0]
        
        for val in range(1,num+1):
            bitCount = bitArr[val//2] + val%2
            bitArr.append(bitCount)
        return bitArr
        
Time Complexity : O(N)

Space Complexity : O(N)


    
