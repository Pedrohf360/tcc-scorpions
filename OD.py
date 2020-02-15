import cv2 as cv
import numpy as np
#import os path

# Write down conf, nms thresholds, inp width/height
confThreshold = 0.25
nmsThreshold = 0.40
inpWidth = 416
inpHeight = 416

# Load names of classes and turn that into a list