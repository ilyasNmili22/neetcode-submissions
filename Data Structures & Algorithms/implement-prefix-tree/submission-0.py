class PrefixTree:

    def __init__(self):
        self.data = set()

    def insert(self, word: str) -> None:
        self.data.add(word)

    def search(self, word: str) -> bool:
        return word in self.data

    def startsWith(self, prefix: str) -> bool:
        for x in self.data:
            i = 0
            while(i < len(x) and prefix[i] == x[i]):
                i += 1
                if i == len(prefix):
                    return True
        return False        
        