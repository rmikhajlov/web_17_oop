# TODO: сделать класс экскурсий
# TODO: написать ручные тесты 




class Transport:
    def __init__(self, fuel):
        self.fuel = fuel
        self.trips = []
    
    def add_trip(self, trip):
        self.trips.append(trip)

    def sum_trips_distances(self):
        return sum(self.trips)

    def calc_remained_distance(self):
        raise NotImplementedError()

class CarTransport(Transport):
    FUEL_PER_100KM = 12

    def calc_remained_distance(self):
        distance = self.sum_trips_distances()
        fuel_wasted = distance / 100 * self.FUEL_PER_100KM
        return (self.fuel - fuel_wasted) / self.FUEL_PER_100KM * 100

class AirTransport(Transport):
    FUEL_PER_HOUR = 200

    def calc_remained_distance(self):
        distance = self.sum_trips_distances()
        fuel_wasted = distance * self.FUEL_PER_HOUR
        return (self.fuel - fuel_wasted) / self.FUEL_PER_HOUR

car1 = CarTransport(100)
car1.add_trip(150)
print(car1.calc_remained_distance())

air1 = AirTransport(100)
air1.add_trip(150)
print(air1.calc_remained_distance())
