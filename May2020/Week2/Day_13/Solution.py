# Using stack
# Remove if previous index valus is greater than the next index until the k comes 0

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        noOfDigits = len(num)
        start = 0
        while(start < noOfDigits):
            while(k and len(stack) and stack[-1] > num[start]):
                stack.pop()
                k -= 1
            stack.append(num[start])
            start += 1
            
        while(k>0):
            stack.pop()
            k-=1
        
        val = ''.join(stack).lstrip('0')
        if(len(val)):
            return val
        return "0"
        
Time Complexity : O(N)
Space Complexity : O(N)

# method -2

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if(len(num)==k):
            return '0'
        minNum = 0
        noOfDigits = len(num)
        for digit in num:
            val = ord(digit)-48
            minNum = minNum *10 + val
        
        while(k):
            number = minNum
            for i in range(noOfDigits):
                newMin = (int(number//(10**(noOfDigits-i))))*(10**(noOfDigits-i-1)) + (number%(10**(noOfDigits-i-1)))
                if(minNum > newMin):
                    minNum = newMin
            
            noOfDigits -= 1
            k -= 1
        return str(minNum)
        
Time Complexity : O(N*K)
Space Complexity : O(1)

Note: Above method gives the Time limit exceeded. But, it is a correct method to get result
