class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node = [None]*26
        self.isWord = False
    
    
    def charToIndex(self,letter):
        return ord(letter)-ord('a')

    
    def insert(self, word: str) -> None:
        for letter in word:
            index = self.charToIndex(letter)
            if(not self.node[index]):
                self.node[index] = Trie() 
            self = self.node[index]
        self.isWord = True


    def searchPrefix(self,word):
        for letter in word:
            index = self.charToIndex(letter)
            if(not self.node[index]):
                return None
            self = self.node[index]
        return self
    
    
    def search(self, word: str) -> bool:
        result = self.searchPrefix(word)
        return result != None and result.isWord
        

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix)!=None
        
Time Complexity : O(N) N - no.of char's in a word
Space Complexity : O(1)



