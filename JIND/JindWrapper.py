from _typeshed import IdentityFunction
import numpy as np
import sys, os, pdb
import pandas as pd
import argparse
os.environ["CUDA_VISIBLE_DEVICES"]=""
import torch
from jind import JindLib
from matplotlib import pyplot as plt
import argparse
from datetime import datetime


def dict_2_cli  (dict):
    return ' '.join(['--{} {}'.format(k,v) for k,v in dict.items()])

config = {'val_frac' : 0.2, 'seed' : 0, 'batch_size' : 128, 
                     'cuda' : False, 'epochs' : 15}

def wrapper(jindObject, mode, **kargs):
    # Load data
    if mode == 'train':
        cmd = 'python JindWrapper_Train.py --path {} {}'.format('jindObject', dict_2_cli(config))
        sys.check_output(cmd, shell=True)
    if mode == 'evaluate':
        data_path = args.test_path
    if mode == 'remove_effect':
        data_path = args.removeEffect_path
    if mode == 'vis_latent':
        data_path = args.visLatent_path
    if mode == 'jind_ft':
        data_path = args.jindFt_path
