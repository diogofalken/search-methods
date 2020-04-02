from neighbour import Neighbour


class City:
    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def addNeighbour(self, city, distance):
        if self.name == city:
            print("Boy")
            return

        if (len(list(filter(lambda cur: cur.name == city, self.neighbours))) >
                0):
            print("Girl")
            return

        self.neighbours.append(Neighbour(city, distance))

    def getNeighbours(self):
        for neighbour in self.neighbours:
            print(f"{self.name} -> {neighbour.name}: {neighbour.distance}km")
