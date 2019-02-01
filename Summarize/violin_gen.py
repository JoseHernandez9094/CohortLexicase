#Will list all of the incomplete id's that need to finish running
#SEED_ORIGINAL & TREATMENTS  will need to be adjusted based on the problems, treatments, and seeds that the project requires. 
#Will also need to handle RANGE if different from the expected results!
#
#Input 1: file directory along with name, expecting Alex's solution_summary file
#Input 2: Directory where the data will be placed
#
#Output : create a csv for each treatment we are looking at!
#
#python3

SELECTION = {'DOWN_SAMPLE_TESTS':'Down Sample', 'TRUNCATED':'Truncated', 'PROG_ONLY_COHORT_LEX':'Prog-Only Cohort', 'COHORT_LEX':'Cohort-Lexicase', 'FULL_LEXICASE':'Lexicase'}
DIMS = {1:"cn1_cs512", 16:'cn16_cs32', 128:'cn128_cs4', 256:'cn256_cs2', 2:'cn2_cs256', 32:'cn32_cs16', 4:'cn4_cs128', 64:'cn64_cs8', 8:'cn8_cs64'}

POS_TREATMENT=0
POS_SOLUTION=4

import argparse
import pandas as pd
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(description="Data aggregation script.")
    parser.add_argument("data_directory", type=str, help="Target experiment directory.")
    parser.add_argument("dump_directory", type=str, help="Target dump directory")

    args = parser.parse_args()
    data_directory = args.data_directory
    write_directory = args.dump_directory

    df = pd.read_csv(data_directory)
    df = df.values.tolist()
    count = {}
    count2 = {}

    gens = ["Update"]
    dims = ["Dimension"]

    for row in df:
        treat = row[POS_TREATMENT].split('__') 
        update = (row[8])
        prob = treat[0][len('PROBLEM_'):]
        sel = treat[1][4:]
        cn = int(treat[2].strip('CN_'))
        cnt = row[4]

        if prob not in count:
            if prob == 'for-loop-index' or prob == 'sum-of squares':
                continue
            count[prob] = {}
            if sel not in count[prob]:
                count[prob][sel] = {}
                if cn not in count[prob][sel]:
                    count[prob][sel][cn] = [update]
                else:
                    count[prob][sel][cn].append(update)
            else:
                if cn not in count[prob][sel]:
                    count[prob][sel][cn] = [update]
                else:
                    count[prob][sel][cn].append(update)
        else:
            if sel not in count[prob]:
                count[prob][sel] = {}
                if cn not in count[prob][sel]:
                    count[prob][sel][cn] = [update]
                else:
                    count[prob][sel][cn].append(update)
            else:
                if cn not in count[prob][sel]:
                    count[prob][sel][cn] = [update]
                else:
                    count[prob][sel][cn].append(update)

    for prob in count.keys():
        if prob == 'sum-of-squares':
            continue
        print(prob)
        for sel in count[prob].keys():
            dims = []
            gens = []
            for cn,cnt in count[prob][sel].items():
                for up in cnt:
                    if up != "NONE":
                        dims.append(DIMS[cn])
                        gens.append(int(float(up)))

            print(sel)
            print(dims, len(dims))
            print(gens, len(gens))
            print()

            raw_data = {'dims':dims, 'gens':gens}
            df = pd.DataFrame(raw_data, columns=['dims', 'gens'])
            df.to_csv(write_directory+prob+'__'+sel+'__violin__gens.csv')

    
if __name__ == "__main__":
    main()