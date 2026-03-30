class TimeMap:

    def __init__(self):
        self.tmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap.setdefault(key, []).append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tmap or len(self.tmap[key]) == 0:
            return ""

        vals = self.tmap[key]
        res = ""
        l, r = 0, len(vals) - 1
        while l <= r:
            m = l + (r-l) // 2
            if vals[m][1] == timestamp:
                return vals[m][0]

            if vals[m][1] < timestamp:
                res = vals[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


        
