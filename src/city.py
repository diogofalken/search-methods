from Neighbour import Neighbour


class City:
    def __init__(self, name):
        self.name = name
        self.neighbours = []
        self.distanceFaro = 0

    def addNeighbour(self, city, distance):
        if self.name == city:
            return

        if (len(list(filter(lambda cur: cur.name == city, self.neighbours))) >
                0):
            return

        self.neighbours.append(Neighbour(city, distance))

    def setDistanceFaro(self, distance):
        self.distanceFaro = distance

    def getNeighbours(self):
        for neighbour in self.neighbours:
            print(f"{self.name} -> {neighbour.name}: {neighbour.distance}km")

    def getFaroDistance(self):
        print(f"{self.name} -> Faro: {self.distanceFaro}")
