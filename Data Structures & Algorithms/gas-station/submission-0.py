class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        if sum(gas) < sum(cost):
            return -1
        #Daba mt2ked kayna
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        ret = last = 0
        for i in range(len(gas)):
            if last + diff[i] >= 0:
                last += diff[i]
            else:
                ret = i + 1
                last = 0
        return ret
