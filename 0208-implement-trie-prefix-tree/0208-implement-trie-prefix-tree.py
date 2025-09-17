class Trie:

    def __init__(self):
        self.words = []
       # self.prefixes = set()

    
    def insert(self, word: str) -> None:
        return self.words.append(word)
        

    def search(self, word: str) -> bool:
        return word in self.words
 
        

    def startsWith(self, prefix: str) -> bool:
        for i in range(len(self.words)):
            if prefix == self.words[i][0:len(prefix)]:
                return True
        
        return False
        



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)