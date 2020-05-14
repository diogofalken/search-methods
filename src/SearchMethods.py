from queue import PriorityQueue
import collections


class SearchMethods:
    def __init__(self, _cities):
        self.cities = _cities

    def uniformCostSearch(self, beginCity, endCity):
        # Check if input cities are valid
        if self._cityExists(beginCity) == 0 or self._cityExists(endCity) == 0:
            exit()

        visited = set()
        queue = PriorityQueue()

        beginCity = self._searchCity(beginCity)
        queue.put((0, beginCity, beginCity.name))

        # Start algorithm
        while queue:
            cost, node, path = queue.get()
            if node.name not in visited:
                visited.add(node.name)

                if node.name == endCity:
                    print(f"{path} = {cost}")
                    break

                for i in node.neighbours:
                    if i.name not in visited:
                        total_cost = cost + i.distance
                        cur = self._searchCity(i.name)
                        queue.put((total_cost, cur, path + f" -> {i.name}"))

    def depthLimitedSearch(beginCity, endCity):
        pass

    def sofregaSearch(self, beginCity, endCity="Faro", distance=0):
        # Check if input cities are valid
        if self._cityExists(beginCity) == 0 or self._cityExists(endCity) == 0:
            exit()

        beginCity = self._searchCity(beginCity)

        if(beginCity.name == beginCity.name):
            print(
                f" We are currently at {beginCity.name} with a total distance of: {distance}.")

        if(beginCity.name == endCity):
            print(
                f"\n {endCity} was found with the optimal distance of: {distance}.")
            exit()

        # Heuristic value -> beginCity.distanceFaro
        lowestDistance = self._searchCity(
            beginCity.neighbours[0].name).distanceFaro

        childrenDictionary = {}
        orderedChildrenDictionary = {}

        for neighbour in range(len(beginCity.neighbours)):
            row = self._searchCity(
                beginCity.neighbours[neighbour].name)
            childrenDictionary[row.name] = row.distanceFaro
            orderedChildrenDictionary = sorted(
                childrenDictionary.items(), key=lambda x: x[1])

        for neighbour in orderedChildrenDictionary:
            distance += neighbour[1]
            self.sofregaSearch(neighbour[0], "Faro", distance)

    def aStarSearch(self, beginCity, endCity="Faro", distance=0):
        # Check if input cities are valid
        if self._cityExists(beginCity) == 0 or self._cityExists(endCity) == 0:
            exit()

        # dictionary to store values
        aStarDictionary = []

        self.checkAStar(beginCity, endCity, aStarDictionary)

    def checkAStar(self, beginCity, endCity, aStarDictionary, distance=0):
        beginCity = self._searchCity(beginCity)

        if(beginCity == endCity):
            print(
                f"\n {endCity} was found with the optimal distance of: {distance}.")
            return

        # Dictionary
        childrenDictionary = {}
        orderedChildrenDictionary = {}

        for neighbour in range(len(beginCity.neighbours)):
            row = self._searchCity(
                beginCity.neighbours[neighbour].name)

            childrenDictionary[row.name] = row.distanceFaro + \
                beginCity.neighbours[neighbour].distance

            orderedChildrenDictionary = sorted(
                childrenDictionary.items(), key=lambda x: x[1])

        for key, value in orderedChildrenDictionary:
            row = self._searchCity(key)
            distance += value - row.distanceFaro
            self.checkAStar(key, "Faro", distance)

    def _searchCity(self, name):
        for city in self.cities:
            if city.name == name:
                return city

    def _cityExists(self, _city):
        city = self._searchCity(_city)

        if not city:
            print(f"City {_city} is not valid.")
            return 0
        return 1
