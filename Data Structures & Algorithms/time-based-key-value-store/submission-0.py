class TimeMap:

    def __init__(self):
        self.my_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.my_dict:
            self.my_dict[key] = {}
        self.my_dict[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.my_dict or timestamp < min(self.my_dict[key]):
            return ""
        while (timestamp not in self.my_dict[key]):
            timestamp -= 1
        return self.my_dict[key][timestamp] 



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)