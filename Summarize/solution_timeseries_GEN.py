#python3
#This script will make csv so that graph_timeseries.py can create plots with them!
#TODO: Make the functionality for Evaluations

import pandas as p

MAX_GENS = 1000
df = p.read_csv('../Data/Raw/min_programs__update_1000.csv')
treat = {}
TREATMENT = 'treatment'
FOUND = 'solution_found'
UPDATE = 'update_found'
EVAL = 'evaluation_found'
POS_UPDATE = 0
POS_EVAL = 1

for i,row in df.iterrows():
    #If we do not have the treatment in our data dict
    if row[TREATMENT] in treat:
        if row[FOUND] == True:
            #If the row has found a solution store gen and eval
            tup = tuple([float(row[UPDATE]), float(row[EVAL])])
            treat[row[TREATMENT]].append(tup)
    else:
        if row[FOUND] == True:         
            temp = [tuple([float(row[UPDATE]), float(row[EVAL])])]
            treat[row[TREATMENT]] = temp

#Will gather data by problem into CN,CS lists for generations.
#TODO
K_PROB = 0
K_SEL = 1
K_CN = 2
K_CS = 3
data_gen = {}
for k,val in treat.items():
    k = k[8:].split('__')
    gens = [x[POS_UPDATE] for x in val]
    gens.sort()
    dimen = k[K_CN] + '-' + k[K_CS]
    prob = k[K_PROB]
    sele = k[K_SEL]

    #check if problem exists within the first layer of dict
    if prob not in data_gen:
        #If not in the dict, create an empty one for it
        data_gen[prob] = {}

        #Check if selection not within the second layer
        if sele not in data_gen[prob]:
            #Second level is the selection scheme
            data_gen[prob][sele] = {}
            #Third level is the dimensionality
            data_gen[prob][sele][dimen] = gens

        #Selection is within the second layer
        else:
            #Third level is the dimensionality
            data_gen[prob][sele][dimen] = gens

    else:
        #Check if selection not within the second layer
        if sele not in data_gen[prob]:
            #Second level is the selection scheme
            data_gen[prob][sele] = {}
            #Third level is the dimensionality
            data_gen[prob][sele][dimen] = gens

        #Selection is within the second layer
        else:
            #Third level is the dimensionality
            data_gen[prob][sele][dimen] = gens

#Go through each problem
for prob in data_gen:
    #Go through each selection scheme
    for sele in data_gen[prob]:
        #Go through each dimensionality
        for dimen in data_gen[prob][sele]:
            raw = []
            raw.append(tuple([0,0]))
            d = data_gen[prob][sele][dimen]
            #Create the coordinates
            for i in range(0, len(d)):
                # raw.append(tuple([d[i], raw[len(raw)-1][1]]))
                raw.append(tuple([d[i], raw[len(raw)-1][1]+1]))
            raw.append([MAX_GENS, raw[len(raw)-1][1]])

            gen = [x[0] for x in raw]
            cnt = [x[1] for x in raw]
            raw_data = {'Generations': gen, 'Solution_Count': cnt}
            df = p.DataFrame(raw_data, columns = ['Generations', 'Solution_Count'])
            fname = prob + '__' + sele[4:] + '__' + dimen + '.csv'
            df.to_csv('../Data/Polished/Generations/'+fname)