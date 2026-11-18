class TrieNode :
    def __init__(self) :
        self.children = {}
        self.is_end = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for w in word :
            if w not in node.children :
                #dne then add it to the children
                node.children[w] = TrieNode()
            node = node.children[w]
        node.is_end = True
        
    def _walk(self, s) :
        node = self.root 
        for ch in s :
            if ch not in node.children :
                return None
            node = node.children[ch]
        return node #where the walk ended
    
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self._walk(word)
        return node is not None and node.is_end

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self._walk(prefix)
        return node is not None
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)