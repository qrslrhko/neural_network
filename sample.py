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
		
		
current_grad_w2 = np.dot(self.Z1.T,delta3 )
grad_w2 = learning_rate *current_grad_w2 + momentum * self.prev_delta_weight[1]

delta2 = delta3.dot(self.weight[1].T) * acti_fun_R.backward(self.Z1)
current_grad_w1 = np.dot(input_value.T, delta2)
grad_w1 = learning_rate * current_grad_w1 + momentum *self.prev_delta_weight[0]

#update previous delta_weights
self.prev_delta_weight[0] = grad_w1
self.prev_delta_weight[1] = grad_w2

#update weights 
self.weight[1] -=  grad_w2
self.weight[0] -=  grad_w1
