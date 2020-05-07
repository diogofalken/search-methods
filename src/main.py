import sys
sys.path.append('../')

from SearchMethods import SearchMethods
from FileUtils import FileUtils
from city import City

if __name__ == "__main__":
    # Get all the info from JSON files and save it to array cities
    fileUtils = FileUtils("../data/cities.json", "../data/citiesSL.json")
    arrayCities = fileUtils.getArrayCities()

    # Print loaded Info
    # for x in arrayCities:
    #     x.getInfo()

    searchMethods = SearchMethods(arrayCities)

    # Uniform Cost Search
    searchMethods.uniformCostSearch("Viana do Castelo", "Faro")

    # Sofrega Search
    searchMethods.sofregaSearch("Viseu", "Faro")
    
    # Depth Limit Search
    searchMethods.depthLimitSearch("Viana do Castelo", "Faro",5)