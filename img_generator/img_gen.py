#!/usr/bin/env python3
from multiprocessing import Pool
import cv2, random, glob, itertools, sys, os
import numpy as np

# transform, horizontally or vertically
def flip_img(input_img, count):

	img = cv2.imread(input_img)
	# -1 = both, 0 = horizontal, 1 = vertical
	transforms = [1, None]
	choice = random.choice(transforms)

	if choice != None:
		transformed_img = cv2.flip(img, choice)
	else:
		transformed_img = img

	rotate(transformed_img, count)

# rotate
def rotate(img, count):
	(h,w) = img.shape[:2]

	# random rescale 
	scale = random.uniform(0.5, 1.2)
	center = (w/2, h/2)
	angle_to_rotate = random.choice(list(range(-35,35)))

	M = cv2.getRotationMatrix2D(center, angle_to_rotate, scale)
	
	# crop by delta
	delta_w = random.choice(list(range(-60, 60)))
	delta_h = random.choice(list(range(-30, 30)))
	rotated_img = cv2.warpAffine(img, M, (w + delta_w, h + delta_h), flags=cv2.INTER_LINEAR)

	cv2.imwrite(sys.argv[3] + str(count) + str(random.randint(0,1000000)) + '.jpg', rotated_img)


input_imgs = os.listdir(sys.argv[2])

# create this many mutations of each input image
num_imgs_per_input = list(range(0,round(int(sys.argv[1])/len(input_imgs))))

pool = Pool(12)

for img in input_imgs:
	print('Creating ' + str(len(num_imgs_per_input)) + ' mutations of ' + img + '...')
	img_path =  sys.argv[2] + img
	results = pool.starmap(flip_img, zip(itertools.repeat(img_path), num_imgs_per_input))

pool.close()
pool.join() 
