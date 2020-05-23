import sys
from os import system, name
sys.path.append('../')

from SearchMethods import SearchMethods
from FileUtils import FileUtils
from City import City


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def validCity(arrayCities, name):
    for city in arrayCities:
        if city.name == name:
            return 1

    return 0


def askForCities(arrayCities):
    start = input("Start City: ")
    end = input("End City: ")

    if (validCity(arrayCities, start) == 0
            or validCity(arrayCities, end) == 0):
        print("Inserted a invalid city.")
        return None

    return [start, end]


if __name__ == "__main__":
    # Get all the info from JSON files and save it to array cities
    fileUtils = FileUtils("./data/cities.json", "./data/citiesSL.json")
    arrayCities = fileUtils.getArrayCities()

    searchMethods = SearchMethods(arrayCities)

    state = True

    while (state):
        clear()
        print("------------ MENU ------------")
        print()

        choice = input("""
        1: List all cities
        2: Uniform Cost Search 
        3: Uniform Cost Search with visited
        4: Depth Limited Search
        5: Sôfrega Search
        6: A*
        Q: Quit/Log Out

        Please enter your choice: """)

        clear()
        if choice == "1":
            for x in arrayCities:
                x.getInfo()
        elif choice == "2":
            cities = askForCities(arrayCities)

            if cities != None:
                print("\n--- Uniform Cost Search Algorithm --- \n")
                searchMethods.uniformCostSearch(cities[0], cities[1])

        elif choice == "3":
            cities = askForCities(arrayCities)

            if cities != None:
                print(
                    "\n--- Uniform Cost Search Algorithm with Visited --- \n")
                searchMethods.uniformCostSearchVisited(cities[0], cities[1])
        elif choice == "4":
            cities = askForCities(arrayCities)

            if cities != None:
                limit = int(input("Insert the limit: "))

                print("\n--- Depth Limit Search --- \n")
                searchMethods.depthLimitSearch(cities[0], cities[1], limit)
        elif choice == "5":
            start = input("Insert start city: ")

            if (validCity(arrayCities, start) == 1):
                print("\n--- Sôfrega Search Algorithm --- \n")
                searchMethods.sofregaSearch(start, "Faro")
        elif choice == "6":
            start = input("Insert start city: ")

            if (validCity(arrayCities, start) == 1):
                print("\n--- A* Search Algorithm --- \n")
                searchMethods.aStarSearch("Viseu", "Faro")
        elif choice == "Q" or choice == "q":
            state = False
            exit()
        else:
            print("You must only select either A,B,C, or D.")
            print("Please try again")

        input("Press Enter to continue...")