# import the necessary packages
import cv2
import numpy as np



class ShapeDetector:
	def __init__(self):
		pass

	def isCircle(self, c):
		# initialize the shape name and approximate the contour
		shape = False 
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)

		# if the shape is a triangle, it will have 3 vertices
		if(len(approx)>3):
			shape= True
		
		# return the name of the shape
		return shape



	
