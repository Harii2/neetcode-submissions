from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        search = self.d[key]
        l, r = 0, len(search) - 1
        ans = ""
        while l <= r:
            mid = (l + r) // 2 
            curr_timestamp = search[mid][0]
            if curr_timestamp == timestamp:
                return search[mid][1]
            elif curr_timestamp <= timestamp:
                l = mid + 1 
                ans = search[mid][1]
            else:
                r = mid - 1 
        return ans
