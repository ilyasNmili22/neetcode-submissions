class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for x in strs:
            sorted_x = "".join(sorted(x))
            if sorted_x in my_dict:
                my_dict[sorted_x].append(x)
            else:
                my_dict[sorted_x] = [x]
        return my_dict.values()