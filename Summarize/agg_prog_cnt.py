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
file_gen = "Problem__Generations__"
file_eva = "Problem__Evaluations__"

import argparse, csv
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description="Data aggregation script.")
    parser.add_argument("data_directory", type=str, help="Target experiment directory.")
    args = parser.parse_args()
    data_directory = args.data_directory
    data_directory = data_directory.strip()

    #Collect all the full lexicase data for generations
    df = pd.read_csv(data_directory+"Problem__Generations__COHORT_LEX.csv")
    df = df.values.tolist()    
    GEN_PROB = []
    GEN_DIM = []
    GEN_CNT = []
    for row in df:
        prob = row[1] #str
        dim = row[2] #str
        cnt = int(row[3])        
        if dim == 'cn1_cs512':
            GEN_PROB.append(prob)
            GEN_DIM.append(dim)
            GEN_CNT.append(cnt)

    raw_data = {'problem':GEN_PROB, 'dims':GEN_DIM, 'count':GEN_CNT}
    df_gen = pd.DataFrame(raw_data, columns=['problem', 'dims', 'count'])
    
    for p in SELECTION:
        df_gen.to_csv(data_directory+"Problem__Generations__"+p+".csv", header=False, mode = 'a')


    #Collect Data for EVALUATIONS
    df = pd.read_csv(data_directory+"Problem__Evaluations__COHORT_LEX.csv")
    df = df.values.tolist()    
    EVE_PROB = []
    EVE_DIM = []
    EVE_CNT = []
    for row in df:
        prob = row[1] #str
        dim = row[2] #str
        cnt = int(row[3])        
        if dim == 'cn1_cs512':
            EVE_PROB.append(prob)
            EVE_DIM.append(dim)
            EVE_CNT.append(cnt)

    raw_data = {'problem':EVE_PROB, 'dims':EVE_DIM, 'count':EVE_CNT}
    df_gen = pd.DataFrame(raw_data, columns=['problem', 'dims', 'count'])
    
    for p in SELECTION:
        df_gen.to_csv(data_directory+"Problem__Evaluations__"+p+".csv", header=False, mode = 'a')
if __name__ == "__main__":
    main()