class TrieNode:
    def __init__(self):
        # Dirctionary to store child nodes :{char: TrieNode}
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here
        Creates a root node with empty children and is_end = false
        """
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie
        Time complexity: O(m) where m is the length of the word
        """
        node = self.root # start from the root

        # traversal through each character in the word
        for char in word:
            # if character does not exist in current node's children
            if char not in node.children:
                # Create a new TireNode for this character
                node.children[char] = TrieNode()
            # Move to the child node corresponding to the current chatacter
            node = node.children[char]
        node.is_end = True
        

    def search(self, word: str) -> bool:
        """
        Return if the word is in the trie
        Time complexity: O(m) where m is the length of the worf
        """
        node = self.root        # start from the root node
        
        # Traverse through each character in the word
        for char in word:
            # if character is not found in current nodes's children
            if char not in node.children:
                return False        # word do not exits
            # move to the child node
            node = node.children[char]
        
        #  Return True only if the final node marks the end of a complete word
        return node.is_end
    

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix
        Time complexity: O(m) where m is the length of the profix
        """
        node = self.root            # start from the root node

        # Teaversal through each character in the prefix
        for char in prefix:
            # if character is not found in current node's children
            if char not in node.children:
                return False        # No word starts with the prifix
            
            # move to the child node
            node = node.children[char]
        
        # if we successfully traversed all characters, prefix exists
        return True


      
        



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)