import random

# -------------------------------
# GLOBAL VARIABLES
# -------------------------------

# Probability that a newly spawned fish is infected with Otostrongylus circumlitis
fish_spawn_infection_chance = 0.1


# -------------------------------
# CLASS DEFINITION
# -------------------------------

class fish:
    """
    Represents a fish with attributes for infection status and location.
    """
    def __init__(self, oto_infection, location):
        """
        Initializes a fish object.
        
        Args:
            oto_infection (int): Infection status (1 = infected, 0 = not infected).
            location (int): Location index representing a grid or habitat.
        """
        self.oto_infection = oto_infection  # Infection status of the fish
        self.location = location  # Location of the fish in the habitat grid


# -------------------------------
# POPULATION GENERATION
# -------------------------------

def generate_fish(number):
    """
    Generates a fish population distributed across 100 locations.
    
    Args:
        number (int): Total number of fish in the population.
    
    Returns:
        list: A list of lists, where each sublist represents a fish population at a specific location.
    """
    newpop = []
    for x in range(0, 100):  # Create 100 habitat grid locations
        grid_pop = []
        for c in range(0, int(number / 100)):  # Evenly distribute fish across locations
            oto_infection_fish = 0
            # Randomly determine if a fish starts infected based on spawn chance
            if random.random() < fish_spawn_infection_chance:
                oto_infection_fish = 1
            grid_pop.append(fish(oto_infection_fish, x))  # Add fish to the grid location
        newpop.append(grid_pop)
    return newpop


# -------------------------------
# POPULATION STATISTICS
# -------------------------------

def print_fishpop(fishpop):
    """
    Prints the total number of fish in the population.
    
    Args:
        fishpop (list): A list of fish populations by location.
    """
    len_of_pop = 0
    for x in fishpop:
        len_of_pop += len(x)  # Sum up the fish count across all locations
    print(len_of_pop)


def print_infected_fish(fishpop):
    """
    Returns the number of infected fish in the population.
    
    Args:
        fishpop (list): A list of fish populations by location.
    
    Returns:
        int: Total number of infected fish.
    """
    number_of_infected = 0
    for x in fishpop:
        for c in x:
            if c.oto_infection == 1:  # Check if fish is infected
                number_of_infected += 1
    return number_of_infected


# -------------------------------
# POPULATION DYNAMICS
# -------------------------------

def other_causes(fishpop):
    """
    Simulates natural fish mortality, removing around 10% of fish per cycle.
    
    Args:
        fishpop (list): A list of fish populations by location.
    """
    for x in fishpop:
        for c in x[:]:  # Iterate over a copy of the list to avoid modification issues
            if random.random() < 0.1:  # 10% chance of death per fish
                x.remove(c)


def regenerate_fishpop(fishpop, number):
    """
    Replenishes the fish population through spawning to maintain population size.
    
    Args:
        fishpop (list): A list of fish populations by location.
        number (int): Desired total fish population size.
    """
    for x in fishpop:
        # Add uninfected fish until the population at each location matches the desired size
        while len(x) < number / 100:
            x.append(fish(0, x))  # Spawn a new, uninfected fish at the current location
