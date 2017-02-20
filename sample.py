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



	for i in range(0, num_epochs):

		for j in range(0,10):
			ans.backward(set_train_x[j],set_train_y[j],learning_rate,momentum,reg)
		# evaluate test sample
		many = ans.testing(test_x)
		count_accuracy = 0
			
		count_accuracy = np.sum(many == test_y.T)
		test_acc_rate = count_accuracy / 2000
		test_accuracy = test_acc_rate
		test_loss = len(test_y.T)- test_accuracy

		# evaluate training sample
		many = ans.testing(train_x)
		count_accuracy = 0
			
		count_accuracy = np.sum(many == train_y.T)
		train_acc_rate = count_accuracy / 10000
		train_accuracy = train_acc_rate
		train_loss = len(train_y.T)- train_accuracy

		print()
		print('    Train Loss: {:.3f}    Train Acc.: {:.2f}%'.format(
			train_loss,
			100. * train_accuracy,
		))
		print('    Test Loss:  {:.3f}    Test Acc.:  {:.2f}%'.format(
			test_loss,
			100. * test_accuracy,
		))
		
		
		
		
