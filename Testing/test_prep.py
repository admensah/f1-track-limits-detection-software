import cv2
import numpy as np
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk, ImageDraw, ImageFilter

def edges(filename):
    image = cv2.imread(filename)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('GreyScale (Press any key to continue)', gray)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(blurred,100,200)
    cv2.imshow('Edges (Press any key to continue)', edges)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()

    cv2.imwrite(f'edges_{filename}', edges)

for i in {1,2,3,6,7}:
    filename = str(i) + ".jpg"
    edges(filename)