#!/usr/bin/env python3
from keras import applications
from keras import optimizers
from keras.models import Sequential, Model
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, GlobalAveragePooling2D, Dropout
from keras.callbacks import ModelCheckpoint
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

num_classes = 5

img_width, img_height = 64,64
#train_dir = "training_set"
#validation_dir = "test_set"

num_train_samples = 2500
number_test_samples = 500

batch_size = 16
epochs = 20


model = applications.VGG19(weights="imagenet", include_top=False, input_shape = (img_width, img_height, 3)) 

# freeze layers that do not need to be retrained 
for layer in model.layers[:5]:
	layer.trainable = False

x = model.output
x = Flatten()(x)
x = Dense(256, activation="relu")(x)
x = Dropout(0.5)(x)
#x = Dense(1024, activation="relu")(x)
predictions = Dense(num_classes, activation="softmax")(x)


model_final = Model(inputs = model.input, outputs = predictions)
model_final.compile(loss = "categorical_crossentropy", optimizer = optimizers.SGD(lr=0.0001, momentum=0.9), metrics=["accuracy"])

model_final.summary()

#load the transfer_model weights 
filepath = "weights.best.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose = 1, \
				save_best_only=True, mode = 'max')
 
callbacks_list = [checkpoint]
 
train_datagen = ImageDataGenerator(
rescale = 1./255,
horizontal_flip = True,
fill_mode = "nearest",
zoom_range = 0.3,
width_shift_range = 0.3,
height_shift_range=0.3,
rotation_range=30)
 
test_datagen = ImageDataGenerator(
rescale = 1./255,
horizontal_flip = True,
fill_mode = "nearest",
zoom_range = 0.3,
width_shift_range = 0.3,
height_shift_range=0.3,
rotation_range=30)


training_set = train_datagen.flow_from_directory('./training_set', \
				target_size = (img_height, img_width), batch_size = batch_size, class_mode = "categorical")

test_set = test_datagen.flow_from_directory('./test_set', target_size = (img_height, img_width), \
				batch_size = batch_size, class_mode = "categorical")


history = model_final.fit_generator(training_set, steps_per_epoch = num_train_samples, \
			epochs = epochs, validation_data = test_set, validation_steps = number_test_samples,\
			callbacks=callbacks_list)

print(history.history.keys())

plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Accuracy for Gray Scale')
plt.ylabel('Accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
plt.savefig('gray_scale_accuracy.png')

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Loss for Gray Scale')
plt.ylabel('Loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
plt.savefig('gray_scale_loss.png')
