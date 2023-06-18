class TimeMap:

    def __init__(self):
        self.stamps = {}
        self.time_stamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.stamps[key] = (value, timestamp)
        self.time_stamps[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if (key, timestamp) in self.time_stamps:
            return self.time_stamps[(key, timestamp)]
        else:
            if key in self.stamps:
                time = self.stamps[key][1]
            else:
                return ""
            while timestamp < time or (key, time) not in self.time_stamps:
                time -= 1
                if time <0:
                    return ""
                
        return self.time_stamps[(key, time)]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# neetcode solution:

