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
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()