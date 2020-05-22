from queue import PriorityQueue
import collections


class SearchMethods:
    def __init__(self, _cities):
        self.cities = _cities

    def uniformCostSearch(self, beginCity, endCity):
        # Check if input cities are valid
        if self._cityExists(beginCity) == 0 or self._cityExists(endCity) == 0:
            exit()

        iterations = 0

        queue = PriorityQueue()

        beginCity = self._searchCity(beginCity)
        queue.put((0, beginCity, beginCity.name))

        # Start algorithm
        while queue:
            iterations += 1
            cost, node, path = queue.get()

            if node.name == endCity:
                print(f"Origem: {beginCity.name}")
                print(f"Destino: {endCity}")
                print(f"Foram necessárias {iterations} iterações")
                print(f"{path} = {cost}")
                break

            for i in node.neighbours:
                total_cost = cost + i.distance
                cur = self._searchCity(i.name)
                queue.put((total_cost, cur, path + f" -> {i.name}"))

    def uniformCostSearchVisited(self, beginCity, endCity):
        # Check if input cities are valid
        if self._cityExists(beginCity) == 0 or self._cityExists(endCity) == 0:
            exit()

        iterations = 0

        visited = set()
        queue = PriorityQueue()

        beginCity = self._searchCity(beginCity)
        queue.put((0, beginCity, beginCity.name))

        # Start algorithm
        while queue:
            iterations += 1
            cost, node, path = queue.get()
            if node.name not in visited:
                visited.add(node.name)

                if node.name == endCity:
                    print(f"Origem: {beginCity.name}")
                    print(f"Destino: {endCity}")
                    print(f"Foram necessárias {iterations} iterações")
                    print(f"{path} = {cost}")
                    break

                for i in node.neighbours:
                    if i.name not in visited:
                        total_cost = cost + i.distance
                        cur = self._searchCity(i.name)
                        queue.put((total_cost, cur, path + f" -> {i.name}"))

    def depthLimitSearch(self, beginCity, endCity, limit):
        limitIterations = limit
        limit -= 1
        # Flag to identify the begining of a new depth level
        flag = object()
        success = False
        beginCity = self._searchCity(beginCity)
        # Set beginCity as visited node
        visitedStack = [beginCity]
        # Structure to store the path
        path = []
        # Start algorithm
        while visitedStack:
            node = visitedStack.pop()
            if node == flag:
                # Finished this level; go back up one level
                limit += 1
                path.pop()

            # Check if current node is equals to the endCity
            elif node.name == endCity:
                path.append(node.name)
                print(self.calculateDistance(path))
                success = True
                break

            elif limit != 0:
                # go one level deeper, push sentinel
                limit -= 1
                path.append(node.name)
                # Put flag to mark the begining of the level
                visitedStack.append(flag)
                # Get all the neighbours of the current node
                for i in node.neighbours:
                    cur = self._searchCity(i.name)
                    visitedStack.append(cur)
        if not success:
            print(
                f"Impossible to reach {endCity} for the limit of {limitIterations} iterations"
            )

    # Function to calculate distance of a given path
    def calculateDistance(self, path):
        totalCost = 0
        constructedPath = ""
        while len(path) > 1:
            node = path.pop(0)
            node = self._searchCity(node)
            constructedPath += f"{node.name} -> "
            for i in node.neighbours:
                if i.name == path[0]:
                    if len(path) == 1:
                        constructedPath += i.name
                    totalCost = totalCost + i.distance
        constructedPath += f" = {totalCost}"
        return constructedPath

    def sofregaSearch(self, beginCity, endCity="Faro", distance=0):
        # Check if input cities are valid
        if self._cityExists(beginCity) == 0 or self._cityExists(endCity) == 0:
            exit()

        beginCity = self._searchCity(beginCity)

        if (beginCity.name == beginCity.name):
            print(
                f" We are currently at {beginCity.name} with a total distance of: {distance}."
            )

        if (beginCity.name == endCity):
            print(
                f"\n {endCity} was found with the optimal distance of: {distance}."
            )
            return False

        childrenDictionary = {}
        orderedChildrenDictionary = {}

        for neighbour in range(len(beginCity.neighbours)):
            row = self._searchCity(beginCity.neighbours[neighbour].name)
            childrenDictionary[row.name] = row.distanceFaro
            orderedChildrenDictionary = sorted(childrenDictionary.items(),
                                               key=lambda x: x[1])

        for neighbour in orderedChildrenDictionary:
            distance += neighbour[1]
            if self.sofregaSearch(neighbour[0], "Faro", distance) == False:
                return False

    def reconstruct_path(self, came_from, start, end, cost):
        end = self._searchCity(end)
        current = end
        path = [current]
        while current != start:
            current = came_from[current]
            if current != None:
                path.append(current)
        constructedPath = start.name
        while len(path) > 1:
            node = path.pop(len(path) - 2)
            if node != None:
                constructedPath += f" -> {node.name} "
        constructedPath += f" = {cost}"
        print(constructedPath)

        return path

    def aStarSearch(self, beginCity, endCity="Faro"):

        queue = PriorityQueue()
        beginCity = self._searchCity(beginCity)
        queue.put(beginCity, 0)
        cameFrom = {beginCity: None}
        costSoFar = {beginCity: 0}

        while not queue.empty():
            current = queue.get()

            if current.name == endCity:
                break

            for node in current.neighbours:

                newCost = costSoFar[current] + node.distance

                if self._searchCity(
                        node.name) not in costSoFar or newCost < costSoFar[
                            self._searchCity(node.name)]:
                    costSoFar[self._searchCity(node.name)] = newCost
                    priority = newCost + abs(
                        current.distanceFaro -
                        self._searchCity(node.name).distanceFaro)
                    queue.put(self._searchCity(node.name), priority)
                    cameFrom[self._searchCity(node.name)] = current

        self.reconstruct_path(cameFrom, beginCity, endCity,
                              costSoFar[self._searchCity(endCity)])

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
