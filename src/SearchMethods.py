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

    def reconstruct_path(self,came_from, start, end, cost):
        end = self._searchCity(end)
        current = end
        path = [current]
        while current != start:
            current = came_from[current]
            if current != None:
                path.append(current)
        constructedPath = start.name
        while len(path)>1:
            node = path.pop(len(path)-2)
            if node != None:
                constructedPath += f" -> {node.name} "
        constructedPath += f" = {cost}"
        print(constructedPath)
        
        return path

    def aStarSearch(self, beginCity, endCity="Faro"):

        queue = PriorityQueue()
        beginCity = self._searchCity(beginCity)
        queue.put(beginCity, 0)
        cameFrom= {beginCity: None}
        costSoFar = {beginCity: 0}
 
        while not queue.empty():
            current = queue.get()

            if current.name == endCity:
                break

            for node in current.neighbours:

                newCost = costSoFar[current] + node.distance

                if self._searchCity(node.name) not in costSoFar or newCost < costSoFar[self._searchCity(node.name)]:
                    costSoFar[self._searchCity(node.name)] = newCost
                    priority = newCost + abs(current.distanceFaro - self._searchCity(node.name).distanceFaro)
                    queue.put(self._searchCity(node.name), priority)
                    cameFrom[self._searchCity(node.name)] = current

        self.reconstruct_path(cameFrom,beginCity,endCity, costSoFar[self._searchCity(endCity)])

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
