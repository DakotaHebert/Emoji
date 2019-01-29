Prototype for emoji classification 
===================================
The classifier takes a long
time to train (for just two classes it was 6 hours for one epoch),
but there may be a way to optimize the keras model. Also, if someone
has tensorflow-gpu installed on their computer, which is what keras uses,
then the training should be much faster. The file 
"weights.best.hdf5" in the classifier folder can be used with the predict.py
script to classify a photo of a thumbs up or ok symbol. I used 50,000
photos for each class generated with the img_gen.py script in the img_generator
folder. 
