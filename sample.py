from __future__ import division
from __future__ import print_function
from scipy.special import expit
from pickle_test import *
import sys

import cPickle
import pickle
import numpy as np
import matplotlib.pyplot as plt


import sklearn
import sklearn.datasets
import sklearn.linear_model
# 


train_x = data['train_data']
train_y = data['train_labels']
test_x = data['test_data']
test_y = data['test_labels']
	
num_examples, input_dims = train_x.shape
num_tests, test_dims = test_x.shape
input_size = train_x.shape[1]

para_list = (input_size,num_hidden,output_size)
ans = LinearTransform(para_list,num_hidden)

## several processes ............ ## 
##................................##
ans.backward(set_train_x[j],set_train_y[j],learning_rate,momentum,reg)
