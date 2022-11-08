import fish
import seal_function
import matplotlib.pyplot as plt

#population numbers
seal_pop_number = 100
fish_pop_number = seal_pop_number * 100

#parameters for the cycles 
#antibodies parameters ('initial' or 'cumulative')
elephant_seals_antibodies = 'initial'
#amount of immunity that is added (put 0 if it's not applicable)
elephant_seals_cumulative = 0
#basic(non age based) or nonbasic infected
elephant_seals_infection_type = 'basic'
#benchmark for elephant seals infection odds
elephant_infection_odds_basic = 0.01
#infection rate for older seals
elephant_infection_odds_old = 0.5
#infection rate for younger seals
elephant_infection_odds_young = 0.5
#amount the immunity decreases by
elephant_seal_immunity_decrease = 0
#the amount of immunity the seal starts with
elephant_seal_initial_immunity = 1

#parameters for the cycles 
#antibodies parameters ('initial' or 'cumulative')
northern_harbour_seals_antibodies = 'initial'
#amount of immunity that is added (put 0 if it's not applicable)
northern_harbour_seals_cumulative = 0.33
#basic(non age based) or nonbasic infected
northern_harbour_seals_infection_type = 'basic'
#benchmark for elephant seals infection odds
northern_harbour_infection_odds_basic = 0.25
#infection rate for older seals
northern_harbour_infection_odds_old = 0.5
#infection rate for younger seals
northern_harbour_infection_odds_young = 0.5
#amount the immunity decreases by
northern_harbour_seal_immunity_decrease = 0
#the amount of immunity the seal starts with
northern_harbour_seal_initial_immunity = 1

# which models you want to run
elephant_seal_model = True
northern_harbour_seal_model = True
combined_model = False

#what info you want to print/graph
infected_seals = True
infected_younger_seals = False
infected_older_seals = False
#this will only print, not graph
infected_fish = True

#lists to graph with
infected_elephant_seals = []
infected_northern_harbour_seals = []
infected_younger_elephant_seals = []
infected_younger_northern_harbour_seals = []
infected_older_elephant_seals = []
infected_older_northern_harbour_seals = []




if elephant_seal_model == True:
  elephant_seals_pop = seal_function.seals_generate(seal_pop_number)
  fishpop = fish.generate_fish(fish_pop_number)

  #this for loop runs the cycle 100 times for the elephant seals
  for x in range(0,100):
    #this for loop is meant to make every instance undergo the code they need to
    for m in elephant_seals_pop:
      #This code allows the seals to hunt fish, poop, and adds age as well as removes older seals
      seal_function.hunt(m, fishpop, elephant_seals_infection_type,elephant_infection_odds_basic,elephant_infection_odds_old,elephant_infection_odds_young)
      seal_function.poop(m, fishpop)
      m.age += 1
      if m.age > 10:
        elephant_seals_pop.remove(m)

    #prints necessary information and stores important 
    if infected_seals == True:
      hi = seal_function.print_infected_seal(elephant_seals_pop)
      infected_elephant_seals.append(hi)
      print(hi)
    if infected_younger_seals == True:
      hi = seal_function.print_infected_young_seals(elephant_seals_pop)
      infected_younger_elephant_seals.append(hi)
      print(hi)
    if infected_older_seals == True:
      hi = seal_function.print_infected_old_seals(elephant_seals_pop)
      infected_older_elephant_seals.append(hi)
      print(hi)
    print()
      #this code provides maintenance on the infection status
    seal_function.increase_oto_length(elephant_seals_pop,elephant_seals_antibodies,elephant_seals_cumulative,elephant_seal_immunity_decrease,elephant_seal_initial_immunity)
        
    #this code kills off 10% of fish and regenerates the fishpop and northern_harbour_seal_pop
    fish.other_causes(fishpop)
    fish.regenerate_fishpop(fishpop,fish_pop_number)
    seal_function.replace_seal_pop(elephant_seals_pop,seal_pop_number)





if northern_harbour_seal_model == True:
  #this generates a fish population and a new seal population for a fresh start
  fishpop = fish.generate_fish(fish_pop_number)
  northern_harbour_seal_pop = seal_function.seals_generate(seal_pop_number)
  
  for x in range(0, 100):
    print(str(x + 1) + 'th year')
    # this makes the seals hunt, poop, and adds age
    for m in northern_harbour_seal_pop:
      seal_function.hunt(m, fishpop, northern_harbour_seals_infection_type,northern_harbour_infection_odds_basic,northern_harbour_infection_odds_old,northern_harbour_infection_odds_young)
      seal_function.poop(m, fishpop)
      m.age += 1
      if m.age > 10:
        northern_harbour_seal_pop.remove(m)

    #prints necessary information and stores important 
    if infected_seals == True:
      hi = seal_function.print_infected_seal(northern_harbour_seal_pop)
      infected_northern_harbour_seals.append(hi)
      print(hi)
    if infected_younger_seals == True:
      hi = seal_function.print_infected_young_seals(northern_harbour_seal_pop)
      infected_younger_northern_harbour_seals.append(hi)
      print(hi)
    if infected_older_seals == True:
      hi = seal_function.print_infected_old_seals(northern_harbour_seal_pop)
      infected_older_northern_harbour_seals.append(hi)
      print(hi)
    print()
        
      #this provides maintenance on infection status
    seal_function.increase_oto_length(northern_harbour_seal_pop,northern_harbour_seals_antibodies,northern_harbour_seals_cumulative,northern_harbour_seal_immunity_decrease,northern_harbour_seal_initial_immunity)
        
      # this kills off 10% of fish as well as regens seal and fish populations
    fish.other_causes(fishpop)
    fish.regenerate_fishpop(fishpop,fish_pop_number)
    seal_function.replace_seal_pop(northern_harbour_seal_pop, seal_pop_number)
  
  



if combined_model == True:
  northern_harbour_seal_pop = seal_function.seals_generate(seal_pop_number)
  elephant_seals_pop = seal_function.seals_generate(seal_pop_number)
    
  #combined model
  for x in range(0,99):
    #this for loop is meant to make every instance undergo the code they need to
    for m in range(0,len(northern_harbour_seal_pop)-1):
      #this gets the seal to eat 10 fish and catch oto if they have to
      seal_function.hunt(elephant_seals_pop[m], fishpop, elephant_seals_infection_type,elephant_infection_odds_basic,elephant_infection_odds_old,elephant_infection_odds_young)
      seal_function.hunt(northern_harbour_seal_pop[m], fishpop,'basic',0,0,0)
      #this makes the seal poop and spread it to fish
      seal_function.poop(elephant_seals_pop[m], fishpop)
      seal_function.poop(northern_harbour_seal_pop[m], fishpop)
      #this adds a year to every seal and kills off the older seals
      elephant_seals_pop[m].age += 1
      northern_harbour_seal_pop[m].age += 1
    hi = []
  
    #this adds age to the seals and kills off older seals
    for x in elephant_seals_pop:
      if x.age < 10:
        hi.append(x)
    elephant_seals_pop = hi
    hi = []
    
    for x in northern_harbour_seal_pop:
      if x.age < 10:
        hi.append(x)
    northern_harbour_seal_pop = hi
    
    #this kills off fish. 10% every year.
    fish.other_causes(fishpop)
  
    #increases oto length
    seal_function.increase_oto_length(elephant_seals_pop,elephant_seals_antibodies,elephant_seals_cumulative,elephant_seal_immunity_decrease,elephant_seal_initial_immunity)
    seal_function.increase_oto_length(northern_harbour_seal_pop,'initial',0,0,0)
  
      #this replaces any dead seals due to age or disease
    seal_function.replace_seal_pop(elephant_seals_pop, seal_pop_number)
    seal_function.replace_seal_pop(northern_harbour_seal_pop, seal_pop_number)
    
    #this replaces the dead fish
    fish.regenerate_fishpop(fishpop,fish_pop_number)
    #this prints the proportion of infected young

number_of_cycles = []
for x in range(100):
  number_of_cycles.append(x)

if elephant_seal_model == True:
  if infected_seals == True:
    plt.plot(number_of_cycles, infected_elephant_seals)
  if infected_younger_seals == True:
    plt.plot(number_of_cycles, infected_younger_elephant_seals)
  if infected_older_seals == True:
    plt.plot(number_of_cycles, infected_older_elephant_seals)

if northern_harbour_seal_model == True:
  if infected_seals == True:
    plt.plot(number_of_cycles, infected_northern_harbour_seals)
  if infected_younger_seals == True:
    plt.plot(number_of_cycles, infected_younger_northern_harbour_seals)
  if infected_older_seals == True:
    plt.plot(number_of_cycles, infected_older_northern_harbour_seals)

plt.show()
