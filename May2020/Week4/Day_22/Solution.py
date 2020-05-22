class Solution:
    def frequencySort(self, s: str) -> str:
        charFreq = Counter(s).most_common()
        
        sortStr = ''
        for char in range(len(charFreq)):
            sortStr = sortStr+charFreq[char][0]*charFreq[char][1]
        return sortStr
        
Time Complexity : O(n log k)

Space Complexity : O(n) 


