from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.init_dest_map = defaultdict(list)
        self.user_map = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user_map[id].append((stationName, t))

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        init = self.user_map[id][-1]
        # append to init dest map
        self.user_map[id].append((stationName, t))
        # from user map get init
        self.init_dest_map[(init[0], stationName)].append(t - init[1])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        entry = self.init_dest_map[(startStation, endStation)]
        val = sum(entry)
        c = len(entry)
        ans = val / c
        return ans

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
