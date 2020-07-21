import numpy as np
import cv2

print("hello inbar")

## machine vision pipe

# data loader
path = r'C:\Users\inked\PycharmProjects\test\dataset\image_1.jpeg'
img = cv2.imread(path)
cv2.imwrite(r'C:\Users\inked\PycharmProjects\test\saved_images\new_img.png', img)
#


# split data to training, validation and test 60%, 20%, 20%
# scipy split dataset

# data preperation, define augmentation

# train model

# save model

# test model
