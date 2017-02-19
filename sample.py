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


for(inputlayer, outputlater) in zip(self.int_hidded_out[:-1],self.int_hidded_out[1:]):
	self.weight.append(np.random.normal(0,scale = 0.001,size=(inputlayer,outputlater) ) )
		self.prev_delta_weight.append(np.zeros((inputlayer,outputlater)))