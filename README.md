# Oto-model-2

Tool to Facilitate the Modeling of Otostrongylus Circumlitis in Seal Populations

Description: This tool is meant to allow simulation of Otostrongylus Circumlitis (Oto.) in Elephant and Northern Harbor seals. It focuses on the relationship between the parasite and the seal by allowing the user to manipulate different parameters about the infection, as well as its target population. This model was created using Python and can be maniupalted through changes in parameters by the user.

How to use the model: 

Population numbers:
The first parameters that are editable, are population numbers, which allow the user to manipulate the number of fish or seals that are generated
seal_pop_number: determines the number of seals generated
fish_pop_number: determines the number of fish generated

Disease Parameters: 
The next set of editable parameters are the parameters regarding disease.
elephant_seals_antibodies: can be set to either "initial", or "cumulative". Initial means that once a seal in infected, it will gain a certain amount of maximum resistance to the parasite which can not be increased. Cumulative means that the amount of resistance to the paraiste can accumulate through more infections instead of staying static.
elephant_seals_cumulative: if elephant_seals_antibodies is set to "cumulative", then this value determines how much resistance will be accumulated against the parasite per infection. Otherwise, pointless
elephant_seals_infection_type: can be set to either "basic" or "nonbasic". Basic means that the infection rate for the parasite will be even across age groups, while nonbasic means that the infection rate for the parasite will differ across age groups.
elephant_infection_odds_basic: If "basic" was chosen for the last parameter, then this value determines the infection rate that is applied across all saeals equally.
elephant_infection_odds_old: If "nonbasic" was chosen, this sets the sets the infection rate for the older population
elephant_infection_odds_young: If "nonbasic" was chosen, this sets the sets the infection rate for the younger population
elephant_seal_immunity_decrease: this determines how much resistance against infection decreases each cycle. If immunity decrease is not desired, set to 0.
elephant_seal_initial_immunity: if elephant_seals_antibodies was set to "initial" then this parameter determines starting immunity against infection. 0 is no protection and 1 is full protection

For the harbour seal parameters, use the above guide.

Age parameters: 
These parameters determine which seals qualify as young or old for graphing
young_param: determines which age range qualifies as a young seal. Input 2 numbers into the list. Having the first value as 0 is highly recommended
old_param: determines which age range qualifies as an old seal. Input 2 numbers into the list. Having the last value as 10 is highly recommended

Model length:
len_mod: determines the number of cycles that the model runs for

Species models: 
These parameters decide which models will be run, which allows for comparison of different models and parameters
elephant_seal_model: determines whether a model run using the parameters set for elephant seals will be run. Input True or False
harbour_seal_model = determines whether a model run using the parameters set for harbour seals will be run. Input True or False
combined_model = determines whether a combined model run using both the parameters set for elephant seals and northern harbour seals will be run. Input True or False

Graph parameters:
These parameters determine which groups of infected seals will be graphed.
infected_seals: determines whether the total infected seals will be graphed. Input True or False
infected_younger_seals: determines whether the younger infected seals will be graphed. Input True or False
infected_older_seals: determines whether the older infected seals will be graphed. Input True or False

Csv path:
csv_path: determines where in the computer a dataset of values in uploaded to

This concludes the summary of the model. Best of luck working with it. Email kaixiang.loke@gmail.com for questions or concerns regarding the model
