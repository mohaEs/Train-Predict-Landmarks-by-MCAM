import os
from inference import Inference
from train_launcher import process_config
from hourglass_tiny import HourglassModel
from datagen import DataGenerator
import numpy as np
import tensorflow as tf
import cv2
import argparse


RED = (0, 0, 255)

parser = argparse.ArgumentParser()
parser.add_argument("--input_dir",  help="path to folder containing images")
parser.add_argument("--checkpoint",  help="where to ")
parser.add_argument("--output_dir",  help="where to p")
a = parser.parse_args()


if not os.path.exists(a.output_dir):
    os.makedirs(a.output_dir)

def show_prections(img, predictions,filename):
	i = 0
	for coord in predictions:
		i += 1
		#keypt = (int(coord[0]), int(coord[1]))
		keypt = (int(coord[0]), int(coord[1]))
		text_loc = (keypt[0]+5, keypt[1]+7)
		cv2.circle(img, keypt, 3, RED, -1)
		cv2.putText(img, str(i), text_loc, cv2.FONT_HERSHEY_DUPLEX, 0.5, RED, 1, cv2.LINE_AA)

	np.savetxt(a.output_dir+filename[:-4]+'_pred.csv', 
	predictions , delimiter=",", fmt='%i')
	# print(a.output_dir+filename+'_pred.csv')

	cv2.imwrite(a.output_dir+filename[:-4]+'_pred.png',img)
	# cv2.imshow('img', img)
	# cv2.waitKey(0)

if __name__ == '__main__':
	print('--Parsing Config File')
	params = process_config('config.cfg')


	from os import listdir
	ImageFileNames=listdir(a.input_dir)

	model = Inference(model=a.checkpoint)

	for i in range(len(ImageFileNames)):
	    #ImageName = a.input_dir+'/'+ImageFileNames[i]

		img = cv2.imread(os.path.join( a.input_dir, ImageFileNames[i]))

		test_img=img	
		predictions = model.predictJoints(test_img, mode='gpu')
		show_prections(test_img, predictions,ImageFileNames[i])