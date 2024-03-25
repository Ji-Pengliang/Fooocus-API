import ipdb
import numpy as np
import pickle

with open('./task_template.pkl', 'rb') as file:
    arg_template = pickle.load(file)
ipdb.set_trace()