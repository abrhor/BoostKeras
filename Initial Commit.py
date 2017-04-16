#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 14:30:11 2017

@author: student
"""

"""
A module for creating and ensembling artificial neural networks
"""
import numpy as np
import random

from keras import Sequential
from keras.layers import Dense

class CreateNetworks(self):
    def __init__(self, x_data, y_data, x_training, y_training, batch_size, epoch, number):
        self.x = x_data
        self.y = y_data
        self.x_t = x_training
        self.y_t = y_training
        self.batch_size = batch_size
        self.number = number
        if len(self.x_data.shape) != 3:
            raise Exception("Data must be 3D: (instances, timesteps per instance, features")
        if len(self.x) != len(self.y) or len(self.x_t) != len(self.y_t):
            raise Exception("Length of input and output must be same")
        self.input_shape = x_data.shape[1:]

class feedforwards(CreateNetworks):
    def __init__(self, x_data, y_data, x_training, y_training, batch_size, epoch, number, method):
        CreateNetworks.__init__(self, x_data, y_data, x_training, y_training, batch_size, epoch, number)
        self.method = method
    
    def create(self):
        networks = np.array([])
        np.random.random_integers()
            
            
    

        