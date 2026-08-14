class TimeMap:

    def __init__(self):
        self.hmp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmp[key].append((timestamp, value))
        # print(self.hmp)

    def get(self, key: str, timestamp: int) -> str:
        val_list = self.hmp[key]
        l, r = 0, len(val_list)-1
        res = ""
        
        t = 0
        while l <= r:
            m = (l + r) // 2
            # print(l, r, m)
            if val_list[m][0] <= timestamp:
                # guaranteed value less than timestamp
                res = val_list[m][1]
                l = m + 1
            else:
                r = m - 1
        
        # print(l)
        return res
