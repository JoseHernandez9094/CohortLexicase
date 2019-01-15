#This python script will create graphs for each problem based on selection scheme
#python3

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_DIR = '../Data/Polished/Evaluations/'
PROBLEMS = ['for-loop-index', 'median', 'small-or-large', 'smallest']
DIMS = ['CN_1-CS_512', 'CN_2-CS_256', 'CN_4-CS_128', 'CN_8-CS_64', 'CN_16-CS_32', 'CN_32-CS_16', 'CN_64-CS_8' ,'CN_128-CS_4', 'CN_256-CS_2']
DIM_DICT = {'CN_1-CS_512': 'CN:1-CS:512', 'CN_2-CS_256':'CN:2-CS:256', 'CN_4-CS_128':'CN:4-CS:128' \
            , 'CN_8-CS_64': 'CN:8-CS:64', 'CN_16-CS_32':'CN:16-CS:32', 'CN_32-CS_16':'CN:32-CS:16', \
            'CN_64-CS_8': 'CN:64-CS:8' ,'CN_128-CS_4' : 'CN:128-CS:4', 'CN_256-CS_2': 'CN:256-CS:2'}
SELECTION = ['COHORT_LEX', 'DOWN_SAMPLE_TESTS' ,'PROG_ONLY_COHORT_LEX', 'TRUNCATED']

for prob in PROBLEMS:
    for sele in SELECTION:
        for dim in DIMS:
            
            PATH = DATA_DIR + prob + '__' + sele + '__' + dim + '.csv'
            file = Path(PATH)
            
            if file.is_file():
                data = pd.read_csv(PATH)
                gens = list(data['Evaluation'])
                cnt = list(data['Solution_Count'])
                
                plt.step(gens, cnt, where='post', label=DIM_DICT[dim])
                plt.xlabel('Evaluations')
                plt.ylabel('Solution Count')
            
        
        plt.title(prob+'_'+sele)
        plt.legend()
        plt.savefig('../Data/Figs/Evaluations/' + prob+'__'+sele+'.png')
        plt.clf()