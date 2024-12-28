import random

# -------------------------------
# CLASS DEFINITION
# -------------------------------

class elephant_seals:
    """
    Represents an elephant seal with attributes for age, infection status,
    location, infection duration, and antibody levels.
    """
    def __init__(self, age, oto_infection, location):
        self.age = age  # Age of the seal (in arbitrary units, e.g., years)
        self.oto_infection = oto_infection  # Infection status (1 = infected, 0 = not infected)
        self.location = location  # Current location (index representing a fish population location)
        self.oto_length = 0  # Duration (cycles) of ongoing infection
        self.antibodies = 0  # Antibody level for immunity against infection


# -------------------------------
# GLOBAL VARIABLES
# -------------------------------

# Duration (in cycles) that Otostrongylus circumlitis infection persists in a seal
length_of_oto_in_seal = 1

# Probability of infection for fish exposed to infected seal feces
oto_infection_chance = 0.25


# -------------------------------
# POPULATION GENERATION
# -------------------------------

def seals_generate(number):
    """
    Generates a population of seals with random ages and locations.
    
    Args:
        number (int): Number of seals to generate.
    
    Returns:
        list: List of elephant_seals objects.
    """
    newpop = []
    for x in range(0, number):
        newpop.append(elephant_seals(random.randint(0, 10), 0, random.randint(0, 99)))
    return newpop


# -------------------------------
# SEAL HUNTING BEHAVIOR
# -------------------------------

def hunt(seal, fishpop, calc_oto_infection, oddsoverallofsealsgettingoto,
         oddsofoldsealgettingoto, oddsofyoungsealgettingoto):
    """
    Simulates a seal's hunting behavior and potential infection from prey.
    
    Args:
        seal (elephant_seals): The seal object performing hunting.
        fishpop (list): A list of fish populations by location.
        calc_oto_infection (str): Method for calculating infection ('basic' or 'age').
        oddsoverallofsealsgettingoto (float): Base infection chance.
        oddsofoldsealgettingoto (float): Infection chance for older seals.
        oddsofyoungsealgettingoto (float): Infection chance for younger seals.
    """
    for x in range(0, 10):
        # Seal moves to a random fish population location
        seal.location = random.randint(0, len(fishpop) - 1)
        
        # Select prey from the fish population at the current location
        preypop = fishpop[seal.location]
        prey = preypop[random.randint(0, len(preypop) - 1)]
        
        # Calculate infection based on the chosen method
        if calc_oto_infection == 'basic':
            calc_oto_infection_basic(prey, seal, oddsoverallofsealsgettingoto)
        else:
            calc_oto_infection_age(prey, seal, oddsofyoungsealgettingoto, oddsofoldsealgettingoto)
        
        # Remove prey from the fish population after being eaten
        fishpop[seal.location].remove(prey)


def calc_oto_infection_basic(prey, seal, oddsoverallofsealsgettingoto):
    """
    Basic infection calculation without considering seal age.
    
    Args:
        prey (object): The prey fish object.
        seal (elephant_seals): The seal object.
        oddsoverallofsealsgettingoto (float): Probability of infection.
    """
    if prey.oto_infection == 1 and random.random() < oddsoverallofsealsgettingoto and seal.antibodies < random.random():
        seal.oto_infection = 1
        seal.oto_length = 1


def calc_oto_infection_age(prey, seal, oddsofyoungsealgettingoto, oddsofoldsealgettingoto):
    """
    Infection calculation considering seal's age.
    
    Args:
        prey (object): The prey fish object.
        seal (elephant_seals): The seal object.
        oddsofyoungsealgettingoto (float): Infection chance for younger seals.
        oddsofoldsealgettingoto (float): Infection chance for older seals.
    """
    if seal.age <= 3 and random.random() < oddsofyoungsealgettingoto and seal.antibodies == 0:
        seal.oto_infection = 1
        seal.oto_length = 1
    elif seal.age >= 4 and random.random() < oddsofoldsealgettingoto and seal.antibodies == 0:
        seal.oto_infection = 1
        seal.oto_length = 1


# -------------------------------
# INFECTION DYNAMICS
# -------------------------------

def increase_oto_length(sealpop, antibodies, cumulative_immunity_addon_amount, immunity_decrease, initial_immunity):
    """
    Updates infection duration, clears infection after a threshold, and adjusts antibodies.
    
    Args:
        sealpop (list): List of seal objects.
        antibodies (str): Antibody adjustment strategy ('initial' or other).
        cumulative_immunity_addon_amount (float): Amount of immunity added per infection cycle.
        immunity_decrease (float): Rate of immunity loss.
        initial_immunity (float): Initial immunity provided after infection.
    """
    for x in sealpop:
        if random.random() < 0.02:
            sealpop.remove(x)  # Random seal death simulation
        
        if x.oto_length > 0:
            x.oto_length += 1
            if x.oto_length > length_of_oto_in_seal and x.antibodies < 1:
                x.oto_length = 0
                x.oto_infection = 0
                if antibodies == 'initial':
                    x.antibodies = initial_immunity
                else:
                    x.antibodies += cumulative_immunity_addon_amount
        
        decrease_antibody(x, immunity_decrease)


# -------------------------------
# DATA REPORTING FUNCTIONS
# -------------------------------

def print_infected_seal(sealpop):
    """Returns the number of infected seals."""
    return sum(1 for x in sealpop if x.oto_infection == 1)


def print_infected_young_seals(sealpop, young_param):
    """Returns the number of infected young seals within the given age range."""
    return sum(1 for x in sealpop if x.oto_infection == 1 and young_param[0] < x.age < young_param[1])


def print_infected_old_seals(sealpop, old_param):
    """Returns the number of infected old seals within the given age range."""
    return sum(1 for x in sealpop if x.oto_infection == 1 and old_param[0] < x.age < old_param[1])


# -------------------------------
# POPULATION MAINTENANCE
# -------------------------------

def replace_seal_pop(sealpop, sealnumber):
    """Replenishes the seal population if below the desired number."""
    while len(sealpop) < sealnumber:
        sealpop.append(elephant_seals(0, 0, random.randint(0, 99)))


def poop(seal, fishpop):
    """Simulates seal feces spreading infection to fish."""
    for _ in range(2):
        if seal.oto_infection == 1:
            seal.location = random.randint(0, len(fishpop) - 1)
            random.shuffle(fishpop[seal.location])
            for x in fishpop[seal.location]:
                if random.random() < oto_infection_chance:
                    x.oto_infection = 1


def decrease_antibody(seal, immunity_decrease_amounts):
    """Reduces antibody levels in a seal."""
    if seal.antibodies > 0:
        seal.antibodies -= immunity_decrease_amounts
    return seal


def print_antibody_seals(seal_pop, age_param):
    """Returns the number of seals with antibodies in the specified age range."""
    return sum(1 for x in seal_pop if age_param[0] < x.age < age_param[1] and x.antibodies > 0)
