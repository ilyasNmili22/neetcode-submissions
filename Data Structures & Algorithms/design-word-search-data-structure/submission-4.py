class WordDictionary:

    def __init__(self):
        self.data = set()

    def addWord(self, word: str) -> None:
        self.data.add(word)

    def search(self, word: str) -> bool:
        for x in self.data:
            if len(x) != len(word):
                continue
            i = 0
            while(i < len(x) and i < len(word) and (word[i] == '.' or word[i] == x[i])):
                i += 1
            if i == len(word) == len(x):
                    return True    
        return False
