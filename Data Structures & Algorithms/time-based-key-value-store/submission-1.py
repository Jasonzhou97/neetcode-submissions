class TimeMap:

    def __init__(self):
        self.keystore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore.keys():
            self.keystore[key]= [(value,timestamp)]
        else:
            self.keystore[key].append((value,timestamp))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keystore.keys():
            return ""
        else:
            value = self.keystore[key]
            l,r = 0, len(value)-1
            res = ""
            while r>=l:
                m = (l+r)//2
                v = value[m]
                if v[1] == timestamp:
                    return v[0]
                elif v[1] > timestamp:
                    r = m-1
                else:
                    res = v[0]
                    l = m+1
            
            return res
            
