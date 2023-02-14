import fish
import seal_function
import matplotlib.pyplot as plt
import pandas as pd

#population numbers
seal_pop_number = 100
fish_pop_number = seal_pop_number * 100

#parameters for the disease 
#antibodies parameters ('initial' or 'cumulative')
elephant_seals_antibodies = 'initial'
#amount of immunity that is added (put 0 if it's not applicable)
elephant_seals_cumulative = 0
#basic(non age based) or nonbasic infected
elephant_seals_infection_type = 'basic'
#benchmark for elephant seals infection odds
elephant_infection_odds_basic = 0.1
#infection rate for older seals
elephant_infection_odds_old = 0.5
#infection rate for younger seals
elephant_infection_odds_young = 0.5
#amount the immunity decreases by
elephant_seal_immunity_decrease = 0
#the amount of immunity the seal starts with
elephant_seal_initial_immunity = 1

#parameters for the disease 
#antibodies parameters ('initial' or 'cumulative')
harbour_seals_antibodies = 'initial'
#amount of immunity that is added (put 0 if it's not applicable)
harbour_seals_cumulative = 0
#basic(non age based) or nonbasic infected
harbour_seals_infection_type = 'basic'
#benchmark for elephant seals infection odds
harbour_infection_odds_basic = 0.1
#infection rate for older seals
harbour_infection_odds_old = 0.5
#infection rate for younger seals
harbour_infection_odds_young = 0.5
#amount the immunity decreases by
harbour_seal_immunity_decrease = 0
#the amount of immunity the seal starts with
harbour_seal_initial_immunity = 1

#age gap of young seals
young_param = [0, 3]
#age gap of old seals
old_param = [8, 10]

#length of model
len_mod = 100

# which models you want to run
elephant_seal_model = False
harbour_seal_model = False
combined_model = True

#what info you want to print/graph
infected_seals = True
infected_younger_seals = False
infected_older_seals = False

#insert csv path here
csv_path = ""

#lists to graph with
infected_elephant_seals = []
infected_harbour_seals = []
infected_younger_elephant_seals = []
infected_younger_harbour_seals = []
infected_older_elephant_seals = []
infected_older_harbour_seals = []
total_antibodies_elephant_seals = []
younger_antibodies_elephant_seals = []
older_antibodies_elephant_seals = []
total_antibodies_harbour_seals = []
younger_antibodies_harbour_seals = []
older_antibodies_harbour_seals = []
harbour_seals_fish = []
elephant_seals_fish = []

infected_elephant_seals_comb_mod = []
infected_harbour_seals_comb_mod = []
infected_younger_elephant_seals_comb_mod = []
infected_younger_harbour_seals_comb_mod = []
infected_older_elephant_seals_comb_mod = []
infected_older_harbour_seals_comb_mod = []
total_antibodies_elephant_seals_comb_mod = []
younger_antibodies_elephant_seals_comb_mod = []
older_antibodies_elephant_seals_comb_mod = []
total_antibodies_harbour_seals_comb_mod = []
younger_antibodies_harbour_seals_comb_mod = []
older_antibodies_harbour_seals_comb_mod = []
combined_model_fish = []



if elephant_seal_model == True:
  elephant_seals_pop = seal_function.seals_generate(seal_pop_number)
  fishpop = fish.generate_fish(fish_pop_number)

  #this for loop runs the cycle 100 times for the elephant seals
  for x in range(0,len_mod):
    #this for loop is meant to make every instance undergo the code they need to
    for m in elephant_seals_pop:
      #This code allows the seals to hunt fish, poop, and adds age as well as removes older seals
      seal_function.hunt(m, fishpop, elephant_seals_infection_type,elephant_infection_odds_basic,elephant_infection_odds_old,elephant_infection_odds_young)
      seal_function.poop(m, fishpop)
      m.age += 1
      if m.age > 10:
        elephant_seals_pop.remove(m)

    #prints necessary information and stores important 
    hi = seal_function.print_infected_seal(elephant_seals_pop)
    infected_elephant_seals.append(hi)
    hi = seal_function.print_infected_young_seals(elephant_seals_pop, young_param)
    infected_younger_elephant_seals.append(hi)
    hi = seal_function.print_infected_old_seals(elephant_seals_pop, old_param)
    infected_older_elephant_seals.append(hi)
    antibodies = seal_function.print_antibody_seals(elephant_seals_pop, [0,11])
    total_antibodies_elephant_seals.append(antibodies)
    antibodies = seal_function.print_antibody_seals(elephant_seals_pop, young_param)
    younger_antibodies_elephant_seals.append(antibodies)
    antibodies = seal_function.print_antibody_seals(elephant_seals_pop, old_param)
    older_antibodies_elephant_seals.append(antibodies)

    elephant_seals_fish.append(fish.print_infected_fish(fishpop))
      #this code provides maintenance on the infection status
    seal_function.increase_oto_length(elephant_seals_pop,elephant_seals_antibodies,elephant_seals_cumulative,elephant_seal_immunity_decrease,elephant_seal_initial_immunity)
        
    #this code kills off 10% of fish and regenerates the fishpop and arbour_seal_pop
    fish.other_causes(fishpop)
    fish.regenerate_fishpop(fishpop,fish_pop_number)
    seal_function.replace_seal_pop(elephant_seals_pop,seal_pop_number)

if harbour_seal_model == True:
  #this generates a fish population and a new seal population for a fresh start
  fishpop = fish.generate_fish(fish_pop_number)
  harbour_seal_pop = seal_function.seals_generate(seal_pop_number)
  
  for x in range(0, len_mod):
    # this makes the seals hunt, poop, and adds age
    for m in harbour_seal_pop:
      seal_function.hunt(m, fishpop, harbour_seals_infection_type,harbour_infection_odds_basic,harbour_infection_odds_old,harbour_infection_odds_young)
      seal_function.poop(m, fishpop)
      m.age += 1
      if m.age > 10:
        harbour_seal_pop.remove(m)

    #prints necessary information and stores important 
    hi = seal_function.print_infected_seal(harbour_seal_pop)
    infected_harbour_seals.append(hi)
    hit = seal_function.print_infected_young_seals(harbour_seal_pop, young_param)
    infected_younger_harbour_seals.append(hi)
    hil = seal_function.print_infected_old_seals(harbour_seal_pop, old_param)
    infected_older_harbour_seals.append(hi)

    antibodies = seal_function.print_antibody_seals(harbour_seal_pop, [0,11])
    total_antibodies_harbour_seals.append(antibodies)
    antibodies = seal_function.print_antibody_seals(harbour_seal_pop, young_param)
    younger_antibodies_harbour_seals.append(antibodies)
    antibodies = seal_function.print_antibody_seals(harbour_seal_pop, old_param)
    older_antibodies_harbour_seals.append(antibodies)

    harbour_seals_fish.append(fish.print_infected_fish(fishpop))
        
      #this provides maintenance on infection status
    seal_function.increase_oto_length(harbour_seal_pop,harbour_seals_antibodies,harbour_seals_cumulative,harbour_seal_immunity_decrease,harbour_seal_initial_immunity)
        
      # this kills off 10% of fish as well as regens seal and fish populations
    fish.other_causes(fishpop)
    fish.regenerate_fishpop(fishpop,fish_pop_number)
    seal_function.replace_seal_pop(harbour_seal_pop, seal_pop_number)

if combined_model == True:
  harbour_seal_pop = seal_function.seals_generate(seal_pop_number)
  elephant_seals_pop = seal_function.seals_generate(seal_pop_number)
  fishpop = fish.generate_fish(fish_pop_number)

  #combined model
  for x in range(0,len_mod):
    #this for loop is meant to make every instance undergo the code they need to
    for m in range(0,len(harbour_seal_pop)-1):
      #this gets the seal to eat 10 fish and catch oto if they have to
      seal_function.hunt(elephant_seals_pop[m], fishpop, elephant_seals_infection_type,elephant_infection_odds_basic,elephant_infection_odds_old,elephant_infection_odds_young)
      seal_function.hunt(harbour_seal_pop[m], fishpop, harbour_seals_infection_type,harbour_infection_odds_basic,harbour_infection_odds_old,harbour_infection_odds_young)
      #this makes the seal poop and spread it to fish
      seal_function.poop(harbour_seal_pop[m], fishpop)
      seal_function.poop(elephant_seals_pop[m], fishpop)
      #this adds a year to every seal and kills off the older seals
      elephant_seals_pop[m].age += 1
      harbour_seal_pop[m].age += 1
    hi = []
  
    #this adds age to the seals and kills off older seals
    for x in elephant_seals_pop:
      if x.age < 10:
        hi.append(x)
    elephant_seals_pop = hi
    hi = []
    
    for x in harbour_seal_pop:
      if x.age < 10:
        hi.append(x)
    harbour_seal_pop = hi
    
    #this kills off fish. 10% every year.
    fish.other_causes(fishpop)

    #gets the data
    hi = seal_function.print_infected_seal(harbour_seal_pop)
    hit = seal_function.print_infected_young_seals(harbour_seal_pop, young_param)
    hil = seal_function.print_infected_old_seals(harbour_seal_pop, old_param)
    him = seal_function.print_infected_seal(elephant_seals_pop)
    hik = seal_function.print_infected_young_seals(elephant_seals_pop, young_param)
    hio = seal_function.print_infected_old_seals(elephant_seals_pop, old_param)
    
    #compiles the data
    infected_elephant_seals_comb_mod.append(hi)
    infected_harbour_seals_comb_mod.append(hit)
    infected_younger_elephant_seals_comb_mod.append(hil)
    infected_younger_harbour_seals_comb_mod.append(him)
    infected_older_elephant_seals_comb_mod.append(hik)
    infected_older_harbour_seals_comb_mod.append(hio)

    #antibodies
    antibodies = seal_function.print_antibody_seals(elephant_seals_pop, [0,11])
    total_antibodies_elephant_seals_comb_mod.append(antibodies)
    antibodies = seal_function.print_antibody_seals(elephant_seals_pop, young_param)
    younger_antibodies_elephant_seals_comb_mod.append(antibodies)
    antibodies = seal_function.print_antibody_seals(elephant_seals_pop, old_param)
    older_antibodies_elephant_seals_comb_mod.append(antibodies)
    antibodies = seal_function.print_antibody_seals(harbour_seal_pop, [0,11])
    total_antibodies_harbour_seals_comb_mod.append(antibodies)
    antibodies = seal_function.print_antibody_seals(harbour_seal_pop, young_param)
    younger_antibodies_harbour_seals_comb_mod.append(antibodies)
    antibodies = seal_function.print_antibody_seals(harbour_seal_pop, old_param)
    older_antibodies_harbour_seals_comb_mod.append(antibodies)

    #fish
    combined_model_fish.append(fish.print_infected_fish(fishpop))
    
    #increases oto length
    seal_function.increase_oto_length(elephant_seals_pop,"initial",0,0,1)
    seal_function.increase_oto_length(harbour_seal_pop,"initial",0,0,1)
  
      #this replaces any dead seals due to age or disease
    seal_function.replace_seal_pop(elephant_seals_pop, seal_pop_number)
    seal_function.replace_seal_pop(harbour_seal_pop, seal_pop_number)
    
    #this replaces the dead fish
    fish.regenerate_fishpop(fishpop,fish_pop_number)
    #this prints the proportion of infected young

number_of_cycles = []
for x in range(len_mod):
  number_of_cycles.append(x)

if elephant_seal_model == True:
  data = {
    'total infected elephant seals': infected_elephant_seals,
    'infected young elephant seals': infected_younger_elephant_seals,
    'infected old elephant seals': infected_older_elephant_seals,
    'total antibodies in elephant seals': total_antibodies_elephant_seals,
    'young elephant seals with antibodies': younger_antibodies_elephant_seals,
    'infected fish in elephant seal model':elephant_seals_fish,
  }
  data = pd.DataFrame.from_dict(data)
  data.to_csv(csv_path + "/elephant_seal_df") 
if harbour_seal_model == True:
  data = {
    'total infected harbour seals': infected_harbour_seals,
    'infected young harbour seals': infected_younger_harbour_seals,
    'infected old harbour seals': infected_older_harbour_seals,
    'old elephant seals with antibodies': older_antibodies_elephant_seals,
    'total antibodues in harbour seals': total_antibodies_harbour_seals,
    'young harbour seals with antibodies':younger_antibodies_harbour_seals,
    'old harbour seals with antibodies':older_antibodies_harbour_seals,
    'infected fish in harbour seal model': harbour_seals_fish,
  }
  data = pd.DataFrame.from_dict(data)
  data.to_csv(csv_path + "/northern_harbour_seal_df") 
if combined_model == True:
  data = {
  'total infected elephant seals combined model':infected_elephant_seals_comb_mod,
  'total infected harbour seals combined model': infected_harbour_seals_comb_mod,
  'infected young elephant seals combined model': infected_younger_elephant_seals_comb_mod,
  'infected young harbour seals combined model': infected_younger_harbour_seals_comb_mod,
  'infected old elephant seals combined model': infected_older_elephant_seals_comb_mod,
  'infected old harbour seals combined model':infected_older_harbour_seals_comb_mod,
  'total antibodies in elephant seals combined model':total_antibodies_elephant_seals_comb_mod,
  'young elephant seals with antibodies combined model': younger_antibodies_elephant_seals_comb_mod,
  'old elephant seals with antibodies combined model':older_antibodies_elephant_seals_comb_mod,
  'total antibdoes in harbour seals combined model': total_antibodies_harbour_seals_comb_mod,
  'young harbour seals with antibodies combined model': younger_antibodies_harbour_seals_comb_mod,
  'old harbour seals with antibodies combined model': older_antibodies_harbour_seals_comb_mod,
  'combined model infect fish':combined_model_fish
}
  data = pd.DataFrame.from_dict(data)
  data.to_csv(csv_path + "/combined_model_df") 


if elephant_seal_model == True:
  if infected_seals == True:
    plt.plot(number_of_cycles, infected_elephant_seals)
  if infected_younger_seals == True:
    plt.plot(number_of_cycles, infected_younger_elephant_seals)
  if infected_older_seals == True:
    plt.plot(number_of_cycles, infected_older_elephant_seals)

if harbour_seal_model == True:
  if infected_seals == True:
    plt.plot(number_of_cycles, infected_harbour_seals)
  if infected_younger_seals == True:
    plt.plot(number_of_cycles, infected_younger_harbour_seals)
  if infected_older_seals == True:
    plt.plot(number_of_cycles, infected_older_harbour_seals)

if combined_model == True:
  if infected_seals == True:
    plt.plot(number_of_cycles, infected_harbour_seals_comb_mod)
    plt.plot(number_of_cycles, infected_elephant_seals_comb_mod)
  if infected_younger_seals == True:
    plt.plot(number_of_cycles, infected_younger_harbour_seals_comb_mod)
    plt.plot(number_of_cycles, infected_younger_elephant_seals_comb_mod)
  if infected_older_seals == True:
    plt.plot(number_of_cycles, infected_older_harbour_seals_comb_mod)
    plt.plot(number_of_cycles, infected_older_elephant_seals_comb_mod)

plt.show()
