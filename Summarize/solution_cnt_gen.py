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

    for row in df:
        treat = row[POS_TREATMENT].split('__') 
        prob = treat[0][len('PROBLEM_'):]
        sel = treat[1][4:]
        cn = int(treat[2].strip('CN_'))
        cnt = row[4]

        if cn not in count:
            count[cn] = {}
            if prob not in count[cn]:
                count[cn][prob] = {}
                if sel not in count[cn][prob]:
                    count[cn][prob][sel] = cnt
                else:
                    count[cn][prob][sel] = cnt
            else:
                if sel not in count[cn][prob]:
                    count[cn][prob][sel] = cnt
                else:
                    count[cn][prob][sel] = cnt
        else:
            if prob not in count[cn]:
                count[cn][prob] = {}
                if sel not in count[cn][prob]:
                    count[cn][prob][sel] = cnt
                else:
                    count[cn][prob][sel] = cnt
            else:
                if sel not in count[cn][prob]:
                    count[cn][prob][sel] = cnt
                else:
                    count[cn][prob][sel] = cnt

    FULL_LEX = 1

    #  Used to verify that the dictionary is being set correctly
    for cn in count.keys():
        problem = []
        selection = []
        counter = []
        print(cn, ': ')
        for prob in count[cn].keys():
            print('    ', prob, ': ')
            for sel,cnt in count[cn][prob].items():
                problem.append(prob)
                selection.append(SELECTION[sel])
                counter.append(cnt)
                print('        ', sel, ': ', cnt)

            #Add full lexicase to all data 
            if cn != FULL_LEX:
                if prob not in count[FULL_LEX]:
                    problem.append(prob)
                    selection.append(SELECTION['FULL_LEXICASE'])
                    counter.append(0)

                else:
                    problem.append(prob)
                    selection.append(SELECTION['FULL_LEXICASE'])
                    counter.append(count[FULL_LEX][prob]['COHORT_LEX'])

        raw_data = {'problem':problem, 'selection':selection, 'count':counter}
        df = pd.DataFrame(raw_data, columns=['problem', 'selection', 'count'])
        df.to_csv(write_directory+'CN_'+str(cn)+'Generations'+'.csv')
        print()


if __name__ == "__main__":
    main()