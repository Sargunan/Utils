# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 08:39:13 2018

@author: Sargunan
"""

""" Downloading the Training data """
import os
from IPython.display import clear_output
import pandas as pd  # For manipulating CSV files
import urllib.request  # For downloading files from the provided links
import time
from termcolor import colored
import numpy as np

test_dir='Test'
train_dir='Train1'

traincsv = pd.read_csv('myntra_train_dataset.csv')
testcsv = pd.read_csv('myntra_test.csv')

classes = traincsv.Sub_category.unique()

   
if not os.path.exists(train_dir):
    os.mkdir(train_dir)
    
for s in range(len(classes)):
    class_dir = os.path.join(train_dir, classes[s])
#    os.mkdir(class_dir)
    
    
    
    
start = time.time()
for i in range(traincsv.shape[0]):
    link = traincsv.iloc[i]['Link_to_the_image']
    name = (traincsv.iloc[i]['Sub_category'])
    full_name = name+'/'+str(i)+'.jpg'
    img_name = full_name
    full_name = os.path.join(train_dir, img_name)
    if not os.path.exists(full_name):
        try:
            clear_output(wait=True)
            urllib.request.urlretrieve(link, full_name)
            print(colored(img_name+' downloaded', 'green'))
        except:
            clear_output(wait=True)
            print(colored('Link Missing', color='red'))
    else:
        clear_output(wait=True)
        print(img_name,' has already been downloaded')
end = time.time()
print('Time taken: ', end-start)




""" Downloading the Testing data """

if not os.path.exists(test_dir):
    os.mkdir(test_dir)
start = time.time()
for i in range(402, testcsv.shape[0]):
    link = traincsv.iloc[i]['Link_to_the_image']
    name = str(i)+'.jpg'
    full_name = os.path.join(test_dir, name)
    if not os.path.exists(full_name):
        try:
            clear_output(wait=True)
            urllib.request.urlretrieve(link, full_name)
            print(colored(name+' downloaded', 'green'))
        except:
            clear_output(wait=True)
            print(colored('Link Missing', color='red'))
    else:
        clear_output(wait=True)
        print(name, ' has already been downloaded')
end = time.time()
print('Time taken: ', end-start)
