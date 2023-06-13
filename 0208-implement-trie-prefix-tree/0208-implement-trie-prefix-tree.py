class Trie:

    def __init__(self):
        self.alpha = [[0,None] for i in range(27)]

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.alpha[26][0] = 1
            self.alpha[26][1] = Trie()
            return
        index = ord(word[0]) - 97
        self.alpha[index][0] = 1
        if not self.alpha[index][1]:
            self.alpha[index][1] = Trie()
        self.alpha[index][1].insert(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0:
            if self.alpha[26][0] == 1:
                return True
            else:
                return False
        index = ord(word[0]) - 97
        if self.alpha[index][0] == 0:
            return False
        return self.alpha[index][1].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True
        index = ord(prefix[0]) - 97
        if self.alpha[index][0] == 0:
            return False
        return self.alpha[index][1].startsWith(prefix[1:])
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)