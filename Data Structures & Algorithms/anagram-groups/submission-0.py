class Solution:
    def is_anagram(self, s1, s2):
        alph1 = 26 * [0]
        alph2 = 26 * [0]
        for i in s1:
            alph1[ord(i) - ord('a')] += 1
        for i in s2:
            alph2[ord(i) - ord('a')] += 1
        for i in range(26):
            if alph1[i] != alph2[i]:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = [[strs[0]]]
        for i in range(1, len(strs)):
            b = 0
            for j in range(len(groups)):
                if self.is_anagram(strs[i], groups[j][0]):
                    groups[j].append(strs[i])
                    b = 1
            if b == 0:
                groups.append([strs[i]])
        return groups
