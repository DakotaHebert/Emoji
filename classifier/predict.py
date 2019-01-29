#!/usr/bin/env python3
from keras.applications import VGG19
from keras import optimizers
from keras.models import Sequential, Model
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, GlobalAveragePooling2D, Dropout
from keras import backend
from keras.callbacks import ModelCheckpoint
from keras.preprocessing import image
from io import BytesIO
from PIL import Image
import glob, sys, cv2
import numpy as np

def main(pic, weight):
	if weight == 'color':
		weight = 'color_weights.best.hdf5'
	elif weight == 'grey' or weight=='gray':
		weight = 'gray_weights.best.hdf5'
	elif weight == 'thresh':
		weight = 'thresh_transfer4.best.hdf5'
	num_classes = 5
	img_width, img_height = 64,64

	model = VGG19(weights="imagenet", include_top=False, input_shape=(img_width, img_height,3))
	x = model.output
	x = Flatten()(x)
	x = Dense(256, activation="relu")(x)
	x = Dropout(0.5)(x)
	predictions = Dense(num_classes, activation="softmax")(x)

	model_final = Model(inputs=model.input, outputs=predictions)
	model_final.load_weights(weight)
	model_final.compile(loss = "categorical_crossentropy", 
						optimizer = optimizers.SGD(lr=0.0001, 
						momentum=0.9), metrics=["accuracy"])

	if weight == 'grey' or weight=='gray':
		color = cv2.imread(pic, 0)
		gray_img = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
		img_str = cv2.imencode('.jpg', gray_img)[1].tostring()
		test_image = image.load_img(BytesIO(img_str), target_size=(img_width, img_height))

	elif weight == 'thresh':
		img = cv2.imread(pic, 0)
		img = cv2.medianBlur(img, 5)
		threshold = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
				cv2.THRESH_BINARY,11,2)
		img_str = cv2.imencode('.jpg', threshold)[1].tostring()
		test_image = image.load_img(BytesIO(img_str), target_size = (img_width, img_height))
	else:
		test_image = image.load_img(pic, target_size=(64, 64))

	#pil_img = Image.fromarray(threshold)	
	labels = ["fingers_crossed","hand_palm","okay","peace","thumbs_up"]

	test_image = image.img_to_array(test_image)
	test_image = np.expand_dims(test_image, axis = 0)
	result = model_final.predict(test_image)
	result_classes = result.argmax(axis=-1)
#	print(result[0])
	print("Prediction: ")
	print(labels[int(result_classes)])
	#print(result[0][0])
#	print('For img: ', pic)
	backend.clear_session()
	return labels[int(result_classes)]

if __name__ == '__main__':
	# Get arguments from user
	pic = sys.argv[1]
	weight = sys.argv[2]
	main(pic, weight)
