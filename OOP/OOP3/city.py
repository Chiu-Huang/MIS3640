class City:

    def __init__(self, arg_name = 'Unknown', pop = 0 ,GDP = 0):
        self.name = arg_name
        self.population  =pop
        self.GDP = GDP

    def __str__(self):
        return "{} hsa {} people, with GDP per capita ${}.".format(self.name, self.population, self.GDP)


    def __gt__(self, another_city):
        if self.GDP > another_city.GDP:
            return True
        elif self.GDP == another_city.GDP:
            if self.population > another_city.population:
                return True
        return False

    def __add__(self, p):
        city = City()
        city.name = self.name + " and " + p.name
        city.GDP = self.GDP + p.GDP
        city.population = self.population + p.population
        return city
    
    def __eq__ (self, p):
        return self.population == p.population and self.GDP == p.GDP

new_york = City()

# print (new_york.name, new_york.population)


new_york1 = City("New York", 8500000,1.85)
boston = City ("Boston", 600000, 75000)


# print (new_york1.name, new_york1.population)

print (new_york1)

print (boston + new_york1)
print (boston)