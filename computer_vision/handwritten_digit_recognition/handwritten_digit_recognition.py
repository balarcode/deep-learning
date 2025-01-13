################################################
# Title     : Handwritten Digit Recognition
# Author    : balarcode
# Version   : 1.0
# Date      : 12th January 2025
# File Type : Python Script / Program
# File Test : Verified on Python 3.12.6
# Comments  : Handwritten digit recognition is a multiclass classification problem. The objective is to detect the handwritten
#             numbers 0 to 9 from the input images. A neural network using softmax regression algorithm to generate output
#             probabilities for all possible numbers 0 to 9 and then choosing the probability that is close to 1.0 would
#             classify or detect the handwritten digit as one of 0 through 9.
#             A labeled dataset is considered as a training dataset in order to build a sequential model in the neural network.
#             The neural network is architected to include two hidden layers with ReLU activation and one output layer with
#             linear activation.
#             For the given dataset of size = N x D, N is the number of data points or training examples in the dataset and
#             D is the dimension of the data point in the dataset. For the handwritten digit recognition problem, the dimension
#             of the dataset will be sqrt(D) pixels X sqrt(D) pixels for each of the images in the dataset.
#
# All Rights Reserved.
################################################
# %%
# Import packages and libraries
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import warnings
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# %%
# Load the dataset
X = np.load("data/X.npy") # Image data (20 x 20 grayscale images)
y = np.load("data/y.npy") # Labeled data
print ('The shape of X is: ' + str(X.shape))
print ('The shape of y is: ' + str(y.shape))

# %%
# Visualize the dataset
warnings.simplefilter(action='ignore', category=FutureWarning)

m, n = X.shape

fig, axes = plt.subplots(8, 8, figsize=(5, 5))
fig.tight_layout(pad=0.13, rect=[0, 0.03, 1, 0.91]) #[left, bottom, right, top]
fig.canvas.toolbar_visible = False
fig.canvas.header_visible = False
fig.canvas.footer_visible = False

for i, ax in enumerate(axes.flat):
    # Select a random index
    random_index = np.random.randint(m)

    # Select the row corresponding to the random index and reshape the image
    X_random_reshaped = X[random_index].reshape((20, 20)).T

    # Display the random image
    ax.imshow(X_random_reshaped, cmap='gray')

    # Display the label above the image
    ax.set_title(y[random_index, 0])
    ax.set_axis_off()
    fig.suptitle("Label, image", fontsize=14)

# %%
# Define the model
tf.random.set_seed(1234)
model = Sequential(
[
    tf.keras.Input(shape=(400, )), # This line forms the input layer to indicate the expected input vector
    Dense(units=25, activation='relu', name='l1'),
    Dense(units=15, activation='relu', name='l2'),
    Dense(units=10, activation='linear', name='l3')
], name = "handwritten_digit_recognition" )

model.summary()

# %%
# Compile and train the model
model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
)

history = model.fit(
    X, y, epochs=100
)

# Plot cost function of the model
fig, ax = plt.subplots(1, 1, figsize=(4, 3))
fig.canvas.toolbar_visible = False
fig.canvas.header_visible = False
fig.canvas.footer_visible = False
ax.plot(history.history['loss'], label='cost')
ax.set_ylim([0, 2])
ax.set_xlabel('Epoch')
ax.set_ylabel('Cost (average loss)')
ax.legend()
ax.grid(True)
plt.show()

# %%
# Predict and visualize the output from the model
warnings.simplefilter(action='ignore', category=FutureWarning)

m, n = X.shape

fig, axes = plt.subplots(8, 8, figsize=(5, 5))
fig.tight_layout(pad=0.13, rect=[0, 0.03, 1, 0.91]) #[left, bottom, right, top]
fig.canvas.toolbar_visible = False
fig.canvas.header_visible = False
fig.canvas.footer_visible = False

for i, ax in enumerate(axes.flat):
    # Select a random index
    random_index = np.random.randint(m)

    # Select the row corresponding to the random index and reshape the image
    X_random_reshaped = X[random_index].reshape((20, 20)).T

    # Display the random image
    ax.imshow(X_random_reshaped, cmap='gray')

    # Predict using the trained Neural Network
    prediction = model.predict(X[random_index].reshape(1, 400))
    prediction_probabilities = tf.nn.softmax(prediction) # Softmax regression algorithm
    yhat = np.argmax(prediction_probabilities)

    # Display the label above the image
    ax.set_title(f"{y[random_index, 0]}, {yhat}", fontsize=10)
    ax.set_axis_off()
fig.suptitle("Label, yhat", fontsize=14)
plt.show()
# %%
