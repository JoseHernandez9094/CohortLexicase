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

    for row in df:
        treat = row[POS_TREATMENT].split('__') 
        prob = treat[0][len('PROBLEM_'):]
        sel = treat[1][4:]
        cn = int(treat[2].strip('CN_'))
        cs = int(treat[3].strip('CS_'))
        cnt = row[4]

        if prob not in count:
            count[prob] = {}
            if cn not in count[prob]:
                count[prob][cn] = {}
                if sel not in count[prob][cn]:
                    count[prob][cn][sel] = cnt
                else:
                    count[prob][cn][sel] = cnt
            else:
                if sel not in count[prob][cn]:
                    count[prob][cn][sel] = cnt
                else:
                    count[prob][cn][sel] = cnt
        else:
            if cn not in count[prob]:
                count[prob][cn] = {}
                if sel not in count[prob][cn]:
                    count[prob][cn][sel] = cnt
                else:
                    count[prob][cn][sel] = cnt
            else:
                if sel not in count[prob][cn]:
                    count[prob][cn][sel] = cnt
                else:
                    count[prob][cn][sel] = cnt

    FULL_LEX = 1

    #  Used to verify that the dictionary is being set correctly
    problem = []
    dims = []
    counter = []
    for prob in count.keys():
        print(prob, ': ')
        for cn in count[prob].keys():
            print('    ', cn, ': ')
            for sel,cnt in count[prob][cn].items():
                if sel == "COHORT_LEX":
                    problem.append(prob)
                    dims.append(DIMS[cn])
                    counter.append(cnt)
                    print('        ', sel, ': ', cnt)

    raw_data = {'problem':problem, 'dims':dims, 'count':counter}
    df = pd.DataFrame(raw_data, columns=['problem', 'dims', 'count'])
    df.to_csv(write_directory+'Problem'+'Evaluations'+'.csv')
    print()


if __name__ == "__main__":
    main()