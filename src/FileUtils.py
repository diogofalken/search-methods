import json
from city import City


class FileUtils:
    def __init__(self, _firstPath, _secondPath):
        self.arrayCities = []
        self.loadJsonCities(_firstPath)
        self.loadJsonCitiesSL(_secondPath)

    def loadJsonCities(self, _dirname):
        with open(_dirname) as file:
            data = json.load(file)

        for city in data:
            currentCity = self.findCity(city["name"])

            if not currentCity:
                currentCity = City(city["name"])
                self.arrayCities.append(currentCity)

            for neighbour in city["neighbours"]:
                currentNeighbour = self.findCity(neighbour["name"])

                if not currentNeighbour:
                    currentNeighbour = City(neighbour["name"])
                    self.arrayCities.append(currentNeighbour)
                currentCity.addNeighbour(currentNeighbour.name,
                                         neighbour["distance"])
                currentNeighbour.addNeighbour(currentCity.name,
                                         neighbour["distance"])

    def loadJsonCitiesSL(self, _dirname):
        # Get data from file
        with open(_dirname) as file:
            data = json.load(file)

        # Go through the array of data
        for city in data:
            currentCity = self.findCity(
                city["name"])  # Get the city from the array

            currentCity.setDistanceFaro(city["distance"])

    def getArrayCities(self):
        return self.arrayCities

    def findCity(self, name):
        for city in self.arrayCities:
            if city.name == name:
                return city
