from collections import namedtuple

class UndergroundSystem:
    def __init__(self):
        self.traveling_now = {}
        self.average_times = {}
        self.TraverlingRecord = namedtuple('TraverlingRecord', 'stationName t')
        self.AverageTimeWithCount = namedtuple('AverageTimeWithCount', 'averageTime count')
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.traveling_now[f"{id}"] = self.TraverlingRecord(stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation = self.traveling_now[f"{id}"].stationName
        startTime = self.traveling_now[f"{id}"].t
        endStation = stationName
        endTime = t
        delta = endTime - startTime

        route = f'{startStation}-{endStation}'
        if route in self.average_times:
            # updated
            curr_avg_time = self.average_times[route].averageTime
            curr_count = self.average_times[route].count
            
            self.average_times[route] = self.AverageTimeWithCount(((curr_avg_time * curr_count) + delta) / (curr_count + 1), curr_count + 1)
        else:
            # create new
            self.average_times[route] = self.AverageTimeWithCount(delta, 1)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.average_times[f'{startStation}-{endStation}'].averageTime


# Your UndergroundSystem object will be instantiated and called as such:
obj = UndergroundSystem()
obj.checkIn(555,'Berkeley',5)
obj.checkOut(555,'SF',10)
print(obj.getAverageTime('Berkeley','SF'))
obj.checkIn(777,'Berkeley',6)
obj.checkOut(777,'SF',43)

print(obj.getAverageTime('Berkeley','SF'))