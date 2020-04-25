import numpy

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.activations import relu, linear


imageResize = (80,30)

print('loading image data...')
img_data = numpy.load('modelImageData.npy', allow_pickle=True)
print('loaded!!')

x = numpy.array([i for i in img_data[0]])
y = numpy.array([i for i in img_data[1]])

x = x / 255

def myLoss(y_pred, y_ac):
    d = y_pred - y_ac
    sum = d[0] * d[0] + d[1] * d[1]
    return 2*sum

# the model

model = Sequential()

model.add(Conv2D(filters=16, kernel_size=(3, 3), kernel_initializer='normal', activation=relu, input_shape=x[0].shape))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(filters=32, kernel_size=(3, 3), kernel_initializer='normal', activation=relu))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(filters=64, kernel_size=(3, 3), kernel_initializer='normal', activation=relu))
model.add(MaxPooling2D(pool_size=(2, 2)))

#model.add(Conv2D(filters=256, kernel_size=(3, 3), activation=relu))
#model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

#model.add(Dense(units=256, kernel_initializer='normal', activation='relu'))
#model.add(Dense(units=128, kernel_initializer='normal', activation='relu'))
model.add(Dense(units=64, kernel_initializer='normal', activation=relu))

model.add(Dense(units=2, kernel_initializer='normal', activation=linear))


model.compile(optimizer='adam', loss='mse', metrics=['mse'])

model.fit(x, y, epochs=10 , validation_split=0.1, shuffle=False)


def acc(s = 0):
    for i in range(s, s+10):
        a = model.predict(x[i].reshape((1,) + x[0].shape))
        print(y[i] - a[0])

acc()

#model.save('model_imageToPrediction_augmented')