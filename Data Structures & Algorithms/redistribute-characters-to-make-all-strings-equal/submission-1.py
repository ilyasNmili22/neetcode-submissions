class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        my_dict = {}
        for x in words:
            for c in x:
                if c in my_dict:
                    my_dict[c] += 1
                else:
                    my_dict[c] = 1
        return all(x % len(words) == 0 for x in my_dict.values())