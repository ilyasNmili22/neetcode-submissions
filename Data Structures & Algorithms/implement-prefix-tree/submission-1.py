class PrefixTree:

    def __init__(self):
        self.my_trie = {}

    def insert(self, word: str) -> None:
        curr = self.my_trie
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['.'] = '.'

            
    def search(self, word: str) -> bool:
        curr = self.my_trie
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        return '.' in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.my_trie
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        return True
        