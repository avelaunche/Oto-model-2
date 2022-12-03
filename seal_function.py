import random
#This establishes the class and the attribtues for 
class elephant_seals:
  def __init__(self, age, oto_infection, location):
    self.age = age
    self.oto_infection = oto_infection
    self.location = location
    self.oto_length = 0
    self.antibodies = 0
#This is the amount of cycles that oto persists for
length_of_oto_in_seal = 1
#The is the chance of oto infection for a fish that eats oto poop
oto_infection_chance = 0.25

#Code for generating seal population
def seals_generate(number):
  newpop = []
  for x in range(0,number):
    newpop.append(elephant_seals(random.randint(0,10),0,random.randint(0,99)))
  return newpop
#Code for how seals hunt
def hunt(seal, fishpop, calc_oto_infection, oddsoverallofsealsgettingoto,oddsofoldsealgettingoto,oddsofyoungsealgettingoto):
  for x in range(0,10):
    #changed the location
    seal.location = random.randint(0,len(fishpop)-1)
    #pulls up available fish at that location
    preypop = fishpop[seal.location]
    #calculate which fish ends up as prey
    prey = preypop[random.randint(0,len(preypop)-1)]
    if calc_oto_infection == 'basic':
      calc_oto_infection_basic(prey, seal,oddsoverallofsealsgettingoto)
    else:
      calc_oto_infection_age(prey, seal,oddsofyoungsealgettingoto,oddsofoldsealgettingoto)
    fishpop[seal.location].remove(prey)
#This calculates if a seal gets oto or not because of the fish they eat. This one has no factors.
def calc_oto_infection_basic(prey, seal,oddsoverallofsealsgettingoto):
  if prey.oto_infection == 1 and random.random() < oddsoverallofsealsgettingoto and seal.antibodies < random.random():
    seal.oto_infection = 1
    seal.oto_length = 1
#This calculates if a seal gets oto or not because of the fish they eat. This one has an age factor.
def calc_oto_infection_age(prey,seal,oddsofyoungsealgettingoto,oddsofoldsealgettingoto):              
  if seal.age <= 3 and random.random() < oddsofyoungsealgettingoto and seal.antibodies == 0:
    seal.oto_infection = 1
    seal.oto_length = 1
  elif seal.age >= 4 and random.random() < oddsofoldsealgettingoto and seal.antibodies == 0:
    seal.oto_infection = 1
    seal.oto_length = 1

#This increases everything about the oto infection. It increases antibodies, it gives antibodies, does everything
def increase_oto_length(sealpop,antibodies,cumulative_immunity_addon_amount, immunity_decrease,initial_immunity):
  for x in sealpop:
    if random.random() < 0.02:
      sealpop.remove(x)
    if x.oto_length > 0:
      x.oto_length += 1
      if x.oto_length > length_of_oto_in_seal and x.antibodies < 1:
        x.oto_length = 0
        x.oto_infection = 0
        #this codes for the initial immunity after infection
        if antibodies == 'initial':
          x.antibodies = initial_immunity

        else:
          x.antibodies += cumulative_immunity_addon_amount
    #this decreases antibodies
    decrease_antibody(x,immunity_decrease)

#The next few variables print the numbers of what they describe
def print_infected_seal(sealpop):
  number_of_infected = 0
  for x in sealpop:
    if x.oto_infection == 1:
      number_of_infected += 1

  return number_of_infected

def print_infected_young_seals(sealpop, young_param):
  number_of_infected = 0
  for x in sealpop:
    if x.oto_infection == 1 and x.age < young_param[1] and x.age > young_param[0]:
      number_of_infected += 1
  return number_of_infected

def print_infected_old_seals(sealpop, old_param):
  number_of_infected = 0
  for x in sealpop:
    if x.oto_infection == 1 and x.age > old_param[0] and x.age < old_param[1]:
      number_of_infected += 1
  return number_of_infected

#This replaces dead seals
def replace_seal_pop(sealpop, sealnumber):
  while len(sealpop) < sealnumber:
    sealpop.append(elephant_seals(0,0, random.randint(0,99)))

#This is how seals poop
def poop(seal, fishpop):
  for x in range(0,2):
    if seal.oto_infection == 1:
      seal.location = random.randint(0,len(fishpop)-1)
      random.shuffle(fishpop[seal.location])
      for x in fishpop[seal.location]:
        if random.random() < oto_infection_chance:
          x.oto_infection = 1

#This decreases antibodies accordint to the immunity_decrease_amounts
def decrease_antibody(seal,immunity_decrease_amounts):
  if seal.antibodies > 0:
    seal.antibodies -= immunity_decrease_amounts
  return seal

#this returns a variable for number of seals with antibodies in the age_param range, including partials
def print_antibody_seals(seal_pop, age_param):
  antibody_count = 0
  for x in seal_pop:
    if x.age < age_param[1] and x.age > age_param[0] and x.antibodies > 0:
      antibody_count += 1
  return antibody_count
