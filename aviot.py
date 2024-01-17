# import tensorflow as tf
# from tensorflow.keras.applications import VGG16
# from tensorflow.keras.layers import Dense, Dropout, Flatten
# from tensorflow.keras.models import Model
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
#
# # Constants
# IMAGE_SIZE = (224, 224)
# BATCH_SIZE = 32
# EPOCHS = 20
# NUM_CLASSES = 3  # Young, Middle, Old
#
# # Load the pre-trained VGG16 model without the top (fully connected) layers
# base_model = VGG16(weights='imagenet', include_top=False, input_shape=(*IMAGE_SIZE, 3))
#
# # Freeze the pre-trained layers
# for layer in base_model.layers:
#     layer.trainable = False
#
# # Add custom fully connected layers
# x = Flatten()(base_model.output)
# x = Dense(512, activation='relu')(x)
# x = Dropout(0.5)(x)
# output = Dense(NUM_CLASSES, activation='softmax')(x)
#
# # Create the model
# model = Model(inputs=base_model.input, outputs=output)
#
# # Compile the model
# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
#
# # Preprocess and augment training data
# train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
# train_generator = train_datagen.flow_from_directory(
#     'path_to_train_directory',
#     target_size=IMAGE_SIZE,
#     batch_size=BATCH_SIZE,
#     class_mode='categorical'
# )
#
# # Preprocess validation data
# validation_datagen = ImageDataGenerator(rescale=1./255)
# validation_generator = validation_datagen.flow_from_directory(
#     'path_to_validation_directory',
#     target_size=IMAGE_SIZE,
#     batch_size=BATCH_SIZE,
#     class_mode='categorical'
# )

import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Constants
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 20
NUM_CLASSES = 3  # Young, Middle, Old

# Set the random seed for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Load the pre-trained VGG16 model without the top (fully connected) layers
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(*IMAGE_SIZE, 3))

# Freeze the pre-trained layers
for layer in base_model.layers:
    layer.trainable = False

# Add custom fully connected layers
x = Flatten()(base_model.output)
x = Dense(512, activation='relu')(x)
x = Dropout(0.5)(x)
output = Dense(NUM_CLASSES, activation='softmax')(x)

# Create the model
model = Model(inputs=base_model.input, outputs=output)

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Define the paths to the training and validation directories
train_dir = 'path_to_train_directory'
validation_dir = 'path_to_validation_directory'

# Preprocess and augment training data
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

# Preprocess validation data
validation_datagen = ImageDataGenerator(rescale=1./255)
validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

# Train the model
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // BATCH_SIZE,
    epochs=EPOCHS,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // BATCH_SIZE
)

# Save the model
model.save('age_detection_model.h5')
