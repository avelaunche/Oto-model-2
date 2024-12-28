# Import necessary libraries
import fish
import seal_function
import matplotlib.pyplot as plt
import pandas as pd

# Population numbers
seal_pop_number = 100  # Number of seals in the population
fish_pop_number = seal_pop_number * 100  # Number of fish, scaled by seal population

# Parameters for the disease (Elephant Seals)
elephant_seals_antibodies = 'initial'  # Antibody parameter: 'initial' or 'cumulative'
elephant_seals_cumulative = 0.1  # Cumulative immunity increase
elephant_seals_infection_type = 'basic'  # Infection type: 'basic' or age-based
elephant_infection_odds_basic = 0.1  # Base infection odds
elephant_infection_odds_old = 0.01  # Infection odds for older seals
elephant_infection_odds_young = 0.1  # Infection odds for younger seals
elephant_seal_immunity_decrease = 0.2  # Immunity decay rate
elephant_seal_initial_immunity = 0.9  # Initial immunity level

# Parameters for the disease (Harbour Seals)
harbour_seals_antibodies = 'initial'
harbour_seals_cumulative = 0.1
harbour_seals_infection_type = 'basic'
harbour_infection_odds_basic = 0.1
harbour_infection_odds_old = 0.1
harbour_infection_odds_young = 0.5
harbour_seal_immunity_decrease = 0
harbour_seal_initial_immunity = 0

# Age parameters
young_param = [0, 2]  # Age range for young seals
old_param = [8, 10]  # Age range for old seals

# Model length
len_mod = 100  # Number of cycles/iterations

# Model execution toggles
elephant_seal_model = True
harbour_seal_model = True
combined_model = False

# Graph toggles
infected_seals = False
infected_younger_seals = False
infected_older_seals = True

# CSV output path
csv_path = ""

# Lists for data collection
infected_elephant_seals = []
infected_harbour_seals = []
infected_younger_elephant_seals = []
infected_younger_harbour_seals = []
infected_older_elephant_seals = []
infected_older_harbour_seals = []
total_antibodies_elephant_seals = []
total_antibodies_harbour_seals = []
harbour_seals_fish = []
elephant_seals_fish = []

# Elephant Seal Model
if elephant_seal_model:
    elephant_seals_pop = seal_function.seals_generate(seal_pop_number)
    fishpop = fish.generate_fish(fish_pop_number)

    for x in range(len_mod):
        for m in elephant_seals_pop:
            seal_function.hunt(m, fishpop, elephant_seals_infection_type,
                               elephant_infection_odds_basic, elephant_infection_odds_old,
                               elephant_infection_odds_young)
            seal_function.poop(m, fishpop)
            m.age += 1
            if m.age > 10:
                elephant_seals_pop.remove(m)
        
        # Collect data
        infected_elephant_seals.append(seal_function.print_infected_seal(elephant_seals_pop))
        infected_younger_elephant_seals.append(seal_function.print_infected_young_seals(elephant_seals_pop, young_param))
        infected_older_elephant_seals.append(seal_function.print_infected_old_seals(elephant_seals_pop, old_param))
        total_antibodies_elephant_seals.append(seal_function.print_antibody_seals(elephant_seals_pop, old_param))
        elephant_seals_fish.append(fish.print_infected_fish(fishpop))
        seal_function.increase_oto_length(elephant_seals_pop, elephant_seals_antibodies,
                                          elephant_seals_cumulative, elephant_seal_immunity_decrease,
                                          elephant_seal_initial_immunity)
        fish.other_causes(fishpop)
        fish.regenerate_fishpop(fishpop, fish_pop_number)
        seal_function.replace_seal_pop(elephant_seals_pop, seal_pop_number)

# Harbour Seal Model
if harbour_seal_model:
    fishpop = fish.generate_fish(fish_pop_number)
    harbour_seal_pop = seal_function.seals_generate(seal_pop_number)

    for x in range(len_mod):
        for m in harbour_seal_pop:
            seal_function.hunt(m, fishpop, harbour_seals_infection_type,
                               harbour_infection_odds_basic, harbour_infection_odds_old,
                               harbour_infection_odds_young)
            seal_function.poop(m, fishpop)
            m.age += 1
            if m.age > 10:
                harbour_seal_pop.remove(m)
        
        infected_harbour_seals.append(seal_function.print_infected_seal(harbour_seal_pop))
        infected_younger_harbour_seals.append(seal_function.print_infected_young_seals(harbour_seal_pop, young_param))
        infected_older_harbour_seals.append(seal_function.print_infected_old_seals(harbour_seal_pop, old_param))
        total_antibodies_harbour_seals.append(seal_function.print_antibody_seals(harbour_seal_pop, old_param))
        harbour_seals_fish.append(fish.print_infected_fish(fishpop))
        seal_function.increase_oto_length(harbour_seal_pop, harbour_seals_antibodies,
                                          harbour_seals_cumulative, harbour_seal_immunity_decrease,
                                          harbour_seal_initial_immunity)
        fish.other_causes(fishpop)
        fish.regenerate_fishpop(fishpop, fish_pop_number)
        seal_function.replace_seal_pop(harbour_seal_pop, seal_pop_number)

# Graphing results
number_of_cycles = list(range(len_mod))
if elephant_seal_model:
    if infected_older_seals:
        plt.plot(number_of_cycles, infected_older_elephant_seals)
if harbour_seal_model:
    if infected_older_seals:
        plt.plot(number_of_cycles, infected_older_harbour_seals)

plt.show()
