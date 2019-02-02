#Will list all of the incomplete id's that need to finish running
#SEED_ORIGINAL & TREATMENTS  will need to be adjusted based on the problems, treatments, and seeds that the project requires. 
#Will also need to handle RANGE if different from the expected results!
#
#Input 1: file directory where data is located
#Input 2: Directory where the data will be placed
#
#Output : create a csv for each treatment we are looking at!
#
#python3

SELECTION = ['DOWN_SAMPLE_TESTS', 'TRUNCATED', 'PROG_ONLY_COHORT_LEX']
PROBLEM = ['median', 'small-or-large', 'smallest', 'compare-string-lengths']
LEX = {}

import argparse, csv
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description="Data aggregation script.")
    parser.add_argument("data_directory", type=str, help="Target experiment directory.")
    args = parser.parse_args()
    data_directory = args.data_directory
    data_directory = data_directory.strip()

    for p in PROBLEM:
        path = data_directory + p + '__COHORT_LEX__violin__eval.csv'
        #Collect Data for EVALUATIONS
        df = pd.read_csv(path)
        df = df.values.tolist()    
        EVE_DIM = []
        EVE_EVE = []
        for row in df:
            dim = row[1] #str
            eve = row[2] #str
            if dim == 'cn1_cs512':
                EVE_DIM.append(dim)
                EVE_EVE.append(eve)
        raw_data = {'dims':EVE_DIM, 'eval':EVE_EVE}
        df_eve = pd.DataFrame(raw_data, columns=['dims', 'eval'])
        
        for s in SELECTION:
            path = data_directory + p + '__'+s+'__violin__eval.csv'
            df_eve.to_csv(path, header=False, mode = 'a')

        path = data_directory + p + '__COHORT_LEX__violin__gens.csv'
        #Collect Data for GENEARATIONS
        df = pd.read_csv(path)
        df = df.values.tolist()    
        GEN_DIM = []
        GEN_EVE = []
        for row in df:
            dim = row[1] #str
            eve = row[2] #str
            if dim == 'cn1_cs512':
                GEN_DIM.append(dim)
                GEN_EVE.append(eve)
        raw_data = {'dims':GEN_DIM, 'eval':GEN_EVE}
        df_gen = pd.DataFrame(raw_data, columns=['dims', 'eval'])
        
        for s in SELECTION:
            path = data_directory + p + '__'+s+'__violin__gens.csv'
            df_gen.to_csv(path, header=False, mode = 'a')

            


if __name__ == "__main__":
    main()