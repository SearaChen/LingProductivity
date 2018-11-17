#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --account=def-timod
#SBATCH --job-name=clusterTest
#SBATCH --mem=1G
source ~/ENV/bin/activate
python learning.py baysian_input_1.0.tsv -n 2 
