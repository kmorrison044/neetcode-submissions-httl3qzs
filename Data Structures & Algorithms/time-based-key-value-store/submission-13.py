class TimeMap:

    def __init__(self):
        self.tmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if (key not in self.tmap and timestamp > 1) or (key in self.tmap and len(self.tmap[key]) < timestamp):
            self.tmap.setdefault(key, [])
            self.tmap[key].extend([""] * (timestamp - 1 - len(self.tmap[key])))
        self.tmap.setdefault(key, []).append(value)
        

    def get(self, key: str, timestamp: int) -> str:
        print(self.tmap)
        print(timestamp)
        if key not in self.tmap: 
            self.tmap.setdefault(key, []).append("")
            return ""
        else:
            if timestamp == 0:
                self.tmap.setdefault(key, []).append("")
                return ""
            elif timestamp > len(self.tmap[key]): 
                i = len(self.tmap[key])-1
                while self.tmap[key][i] == "" and i >= 0:
                    i -= 1
                self.tmap.setdefault(key, []).append("")
                return self.tmap[key][i]
            elif self.tmap[key][timestamp-1] == "":
                i = timestamp - 1
                while self.tmap[key][i] == "" and i >= 0:
                    i -= 1
                self.tmap.setdefault(key, []).append("")
                return self.tmap[key][i]
            else:
                # self.tmap.setdefault(key, []).append("")
                return self.tmap[key][timestamp-1]
