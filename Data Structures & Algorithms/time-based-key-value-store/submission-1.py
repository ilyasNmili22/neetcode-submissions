class TimeMap:

    def __init__(self):
        self.my_dict = defaultdict(list)  #key:[timestamp,value]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.my_dict[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.my_dict:
            return ""
        times = self.my_dict[key]
        #[[1, 'bar'], [4, 'bar2']]: plus grand petit
        ret = ""
        l, r = 0, len(times) - 1
        while l <= r:
            m = (l + r) // 2
            if times[m][0] <= timestamp:
                ret = times[m][1]
                l = m + 1
            else:
                r = m - 1
        return ret