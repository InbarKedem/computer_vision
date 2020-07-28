import numpy as np
import pandas as pd
import cv2

print("hello inbar")

## machine vision pipe

# data loader
path = r'C:\Users\inked\PycharmProjects\computer_vision\data_set\un-labeled_images\test1.NEF'
img = cv2.imread(path)
cv2.imwrite(r'/data_set/larvea/labeled_images\new_test1.png', img)
#loop that for all of the pictures


# split data to training, validation and test 60%, 20%, 20%


# scipy split dataset

# data preperation, define augmentation

# train model

# save model

# test model
