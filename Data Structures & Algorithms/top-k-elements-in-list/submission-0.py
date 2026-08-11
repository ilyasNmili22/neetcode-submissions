class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Hashset = {}
        for i in nums:
            if i in Hashset:
                Hashset[i] += 1
            else:
                Hashset[i] = 1
        sorted_dict_by_values = dict(sorted(Hashset.items(), key=lambda item: item[1]))
        ret = []
        for key in sorted_dict_by_values:
            ret.append(key)
        print(ret)
        return ret[len(ret) - k :]

        