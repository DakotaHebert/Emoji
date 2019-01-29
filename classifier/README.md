Train the Classifier
======================
For training the nn, split the photos into different folders
based on the class. Set the steps per epoch to the amount of training
examples per class.

To train the model, run this from the terminal:
	
	./transfer_train.py

or
	python3 transfer_train.py



For Prediction
=================

To predict class for an input photo, run this from terminal:

	./predict.py input_photo_name	(ex. ./predict.py ok.jpg)

We can move this into a function and call it from the front end.
