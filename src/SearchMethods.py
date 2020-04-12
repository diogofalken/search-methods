from queue import PriorityQueue


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

    def sofregaSearch(beginCity, endCity="Faro"):
        pass

    def aStarSearch(beginCity, endCity="Faro"):
        pass

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
