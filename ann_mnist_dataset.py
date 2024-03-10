# -*- coding: utf-8 -*-
"""ANN_MNIST_Dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-fkUz5NINta1gbLjIVgtpNVOZCpAtcDB
"""

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Load MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train

X_test

y_train

y_test

# Preprocess data (normalize pixel values to range 0-1)
X_train = X_train.astype('float32') / 255

X_test = X_test.astype('float32') / 255

X_train

X_test

# Reshape input data for dense layers (flatten 28x28 images to 784-dimensional vectors)
X_train = X_train.reshape((X_train.shape[0], 784))

X_train

X_test = X_test.reshape((X_test.shape[0], 784))

X_test

# Define a simple ANN architecture with less than 10,000 trainable parameters
model = Sequential()

model.add(Dense(512, activation='relu', input_shape=(784,)))  # First layer with 512 neurons and ReLU activation
model.add(Dense(10, activation='softmax'))  # Output layer with 10 neurons (one for each digit class) and softmax activation

# Compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(learning_rate=0.001), metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Evaluate the model on test data
test_loss, test_acc = model.evaluate(X_test, y_test)

print('Test accuracy:', test_acc)

# Count the total number of trainable parameters
total_params = model.count_params()

print('Total trainable parameters:', total_params)

