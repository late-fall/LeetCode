class Trie:

    def __init__(self):
        self.alpha = [None] * 27

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.alpha[26] = Trie()
            return
        index = ord(word[0]) - 97
        if not self.alpha[index]:
            self.alpha[index] = Trie()
        self.alpha[index].insert(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.alpha[26] != None
        index = ord(word[0]) - 97
        if self.alpha[index] == None:
            return False
        return self.alpha[index].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True
        index = ord(prefix[0]) - 97
        if self.alpha[index] == None:
            return False
        return self.alpha[index].startsWith(prefix[1:])
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)