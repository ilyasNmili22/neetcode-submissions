class WordDictionary:

    def __init__(self):
        self.data = set()

    def addWord(self, word: str) -> None:
        self.data.add(word)

    def search(self, word: str) -> bool:
        for x in self.data:
            i = 0
            while(i < len(x) and (word[i] == '.' or word[i] == x[i])):
                i += 1
                if i == len(word) == len(x):
                    return True
                elif i == len(word):
                    break
        return False
