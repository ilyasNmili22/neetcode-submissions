class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for s in strs:
            freq = 26 * [0]
            for c in s:
                freq[ord(c) - ord('a')] += 1
            freq_tuple = tuple(freq)
            if freq_tuple in my_dict:
                my_dict[freq_tuple].append(s)
            else:
                my_dict[freq_tuple] = [s]
        return list(my_dict.values())
