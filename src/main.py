import sys
sys.path.append('../')

from City import City
from FileUtils import FileUtils

if __name__ == "__main__":
    # Get all the info from JSON files and save it to array cities
    fileUtils = FileUtils("./data/cities.json", "./data/citiesSL.json")
    arrayCities = fileUtils.getArrayCities()

    # Print loaded Info
    for x in arrayCities:
        x.getInfo()