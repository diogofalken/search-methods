from SearchMethods import SearchMethods
from FileUtils import FileUtils
from city import City
import sys
sys.path.append('../')


if __name__ == "__main__":
    # Get all the info from JSON files and save it to array cities
    fileUtils = FileUtils("./data/cities.json", "./data/citiesSL.json")
    arrayCities = fileUtils.getArrayCities()

    # Print loaded Info
    # for x in arrayCities:
    #     x.getInfo()

    searchMethods = SearchMethods(arrayCities)

    # Uniform Cost Search
    print("\n--- Uniform Cost Search Algorithm --- \n")
    searchMethods.uniformCostSearch("Viseu", "Faro")

    # A* Search
    print("\n--- A* Search Algorithm --- \n")
    searchMethods.aStarSearch("Viseu", "Faro")

    # Sofrega Search
    print("\n--- Sofrega Search Algorithm --- \n")
    searchMethods.sofregaSearch("Viseu", "Faro")
