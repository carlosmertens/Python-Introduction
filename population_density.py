"""Population Density.

The density of a population is calculated by dividing the population by
the area of the land.
"""


def population_density(population, land_area):
    """Calculate the population density of an area.

        population: int. The population of the area
        land_area: int or float. This function is unit-agnostic, if you pass
                   in values in terms of square km or square miles the
                   function will return a density in those units.
        """
    return population / land_area


# Get values and storage into variables
country_population = int(input("Population: "))
country_area = int(input("Land's area: "))

# Call the function
density = population_density(country_population, country_area)

# Display the result using the .format method

print("Population of {} and area of {}, gives a density of {}".format(
    country_population, country_area, density))
