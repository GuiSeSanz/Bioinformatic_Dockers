import numpy as np
import pickle
import sys, os, pdb
import pandas as pd
import argparse
os.environ["CUDA_VISIBLE_DEVICES"]=""
import torch
from jind import JindLib
from matplotlib import pyplot as plt
import argparse
from datetime import datetime
import argparse


parser = argparse.ArgumentParser(description='Launch Jind to train the NN.')
parser.add_argument('-path',  type=str, help='the path to the jind objetc')
parser.add_argument('-val_frac',  type=float,  help='the path to the jind objetc')
parser.add_argument('-seed',  type=int, help='the path to the jind objetc')
parser.add_argument('-batch_size',  type=int,  help='the path to the jind objetc')
parser.add_argument('-cuda',  type=bool, help='the path to the jind objetc')
parser.add_argument('-epochs',  type=int, help='the path to the jind objetc')
parser.add_argument('-cmat',  type=bool, help='the path to the jind objetc')

args = parser.parse_args()

train_config = {'val_frac': args.val_frac, 'seed': args.seed, 
                'batch_size': args.batch_size, 'cuda': args.cuda, 
                'epochs': args.epochs}

print(args)

obj = pd.read_pickle(args.path)
obj.dim_reduction(5000, 'Var')
obj.train_classifier(config=train_config, cmat=args.cmat) # Creates confusion matrix on the validation data

# python JindWrapper_Train.py -path ./data/JIND/1234.pkl -val_frac 0.2 -seed 0 -batch_size 100 -cuda True -epochs 10 -cmat True

# train_config = {'val_frac' : 0.2 ,
# 'seed' : 0 ,
# 'batch_size' : 100 ,
# 'cuda' : True ,
# 'epochs' : 10 }