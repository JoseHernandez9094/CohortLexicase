#!/bin/bash
#This part of the script will create all the evaluation data for the solution counts.
python3 ../Summarize/prob_solution_cnt_eval.py ../Data/Raw/100_Or_Less/min_programs__eval_26214400__solutions_summary.csv ../Data/Raw/100_Or_Less/
python3 ../Summarize/prob_solution_cnt_eval.py ../Data/Raw/300_Or_Less/min_programs__eval_78643200__solutions_summary.csv ../Data/Raw/300_Or_Less/
python3 ../Summarize/prob_solution_cnt_eval.py ../Data/Raw/HalfLife/min_programs__eval_131072000__solutions_summary.csv ../Data/Raw/HalfLife/
python3 ../Summarize/prob_solution_cnt_eval.py ../Data/Raw/FullLife/min_programs__eval_262144000__solutions_summary.csv ../Data/Raw/FullLife/

#This part of the script will create all the generation data for the solution counts.
python3 ../Summarize/prob_solution_cnt_gens.py ../Data/Raw/100_Or_Less/min_programs__update_100__solutions_summary.csv ../Data/Raw/100_Or_Less/
python3 ../Summarize/prob_solution_cnt_gens.py ../Data/Raw/300_Or_Less/min_programs__update_300__solutions_summary.csv ../Data/Raw/300_Or_Less/
python3 ../Summarize/prob_solution_cnt_gens.py ../Data/Raw/HalfLife/min_programs__update_500__solutions_summary.csv ../Data/Raw/HalfLife/
python3 ../Summarize/prob_solution_cnt_gens.py ../Data/Raw/FullLife/min_programs__update_1000__solutions_summary.csv ../Data/Raw/FullLife/

#This part of the script will aggregate all the problem count data together, generations and evaluations respectivley.
python3 ../Summarize/agg_prog_cnt.py ../Data/Raw/100_Or_Less/
python3 ../Summarize/agg_prog_cnt.py ../Data/Raw/300_Or_Less/
python3 ../Summarize/agg_prog_cnt.py ../Data/Raw/HalfLife/
python3 ../Summarize/agg_prog_cnt.py ../Data/Raw/HalfLife/

#This part of the script will create all the evaluation data for the violin plots. 
python3 ../Summarize/violin_eval.py ../Data/Raw/100_Or_Less/min_programs__eval_26214400.csv ../Data/Raw/100_Or_Less/
python3 ../Summarize/violin_eval.py ../Data/Raw/300_Or_Less/min_programs__eval_78643200.csv ../Data/Raw/300_Or_Less/
python3 ../Summarize/violin_eval.py ../Data/Raw/HalfLife/min_programs__eval_131072000.csv ../Data/Raw/HalfLife/
python3 ../Summarize/violin_eval.py ../Data/Raw/FullLife/min_programs__eval_262144000.csv ../Data/Raw/FullLife/

#This part of the script will create all the generation data for the violin plots.
python3 ../Summarize/violin_gen.py ../Data/Raw/100_Or_Less/min_programs__update_100.csv ../Data/Raw/100_Or_Less/
python3 ../Summarize/violin_gen.py ../Data/Raw/300_Or_Less/min_programs__update_300.csv ../Data/Raw/300_Or_Less/
python3 ../Summarize/violin_gen.py ../Data/Raw/HalfLife/min_programs__update_500.csv ../Data/Raw/HalfLife/
python3 ../Summarize/violin_gen.py ../Data/Raw/FullLife/min_programs__update_1000.csv ../Data/Raw/FullLife/

#This part of the script will aggregate all the violin data, generations and evaluations respectivley
python3 ../Summarize/agg_violin.py ../Data/Raw/100_Or_Less/
python3 ../Summarize/agg_violin.py ../Data/Raw/300_Or_Less/
python3 ../Summarize/agg_violin.py ../Data/Raw/HalfLife/
python3 ../Summarize/agg_violin.py ../Data/Raw/HalfLife/