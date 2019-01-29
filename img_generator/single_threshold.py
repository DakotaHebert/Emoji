import cv2, random, glob, itertools, sys, os
import numpy as np

# transform, horizontally or vertically
def flip_img(input_img, count):

	img = cv2.imread(input_img, 0)
	#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# -1 = both, 0 = horizontal, 1 = vertical
	transforms = [1, None]
	choice = random.choice(transforms)

	if choice != None:
		transformed_img = cv2.flip(img, choice)
	else:
		transformed_img = img
	
	threshold(transformed_img, count)

def threshold(img, count):
	img = cv2.medianBlur(img, 5)
	img_threshold = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
					cv2.THRESH_BINARY, 11, 2)
	rotate(img_threshold, count)

# rotate
def rotate(img, count):
	(h,w) = img.shape[:2]

	# random rescale 
	scale = random.uniform(0.5, 1.15)
	center = (w/2, h/2)
	angle_to_rotate = random.choice(list(range(-25,25)))

	M = cv2.getRotationMatrix2D(center, angle_to_rotate, scale)
	
	# crop by delta
	delta_w = random.choice(list(range(-60, 60)))
	delta_h = random.choice(list(range(-30, 30)))
	rotated_img = cv2.warpAffine(img, M, (w + delta_w, h + delta_h), flags=cv2.INTER_LINEAR)
	cv2.imwrite(sys.argv[3] + str(count) + str(random.randint(0,1000000)) + '.jpg', rotated_img)

input_imgs = os.listdir(sys.argv[2])

# create this many mutations of each input image
num_imgs_per_input = list(range(0,round(int(sys.argv[1])/len(input_imgs))))

for img in input_imgs:
	print('Creating ' + str(len(num_imgs_per_input)) + ' mutations of ' + img + '...')
	img_path = sys.argv[2] + img
	for i in num_imgs_per_input:
		flip_img(img_path, i)
