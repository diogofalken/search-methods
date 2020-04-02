from city import City

if __name__ == "__main__":
    city = City("Aveiro")

    city.addNeighbour("Porto", 68)
    city.addNeighbour("Viseu", 95)
    city.addNeighbour("Coimbra", 68)
    city.addNeighbour("Leiria", 115)

    city.getNeighbours()
