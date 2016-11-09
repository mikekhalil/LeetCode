class TrieNode(object):
    def __init__(self):
        self.key = None     #a-z char
        self.children = {}  #maps a-z char to node

        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        prev = self.root
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else:
                cur = TrieNode()
                cur.key = char
                prev.children[char] = cur
            prev = cur

        cur.children[None] = True #valid word end
        
        

    def search(self, word):
        cur = self.root
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else: 
                return False
                
        return cur.children.get(None, False)
            

    def startsWith(self, prefix):
        cur = self.root
        for char in prefix:
            if char in cur.children:
                cur = cur.children[char]
            else :
                return False

        return True

if __name__ == "__main__":
    #initialize and populate trie
    trie = Trie()
    trie.insert("somestring")
    trie.insert("derp")             
  
    print trie.search("derp")       #true
    print trie.search("derz")       #false
    print trie.startsWith("dek")    #false
    print trie.startsWith("de")     #true
    print trie.startsWith("some")   #true