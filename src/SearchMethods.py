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

    def depthLimitSearch(self, beginCity, endCity, limit):
        limit -= 1
        # Flag to identify the begining of a new depth level
        flag = object()
        sucess = False
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
                sucess = True
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
        if not sucess:
            print("Impossible to reach the end city for the given limit")



    # Function to calculate distance of a given path   
    def calculateDistance(self,path):
        totalCost = 0
        constructedPath = ""
        while len(path)>1:
            node = path.pop(0)
            node = self._searchCity(node)
            constructedPath += node.name + " -> "
            for i in node.neighbours:
                if i.name == path[0]:
                    if len(path) == 1:
                        constructedPath += i.name
                    totalCost = totalCost + i.distance
        constructedPath += " = " + str(totalCost)
        return constructedPath

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
