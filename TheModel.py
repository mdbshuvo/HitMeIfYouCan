import tensorflow as tf
import numpy as np

data = np.load('modelData.npy')

size = len(data)

#size = 1000
#data = data[: size]

test_percent = 0.9

x = []
y = []

for i in range(size):
    x.append([data[i][0], data[i][1]])
    y.append(data[i][2:])
    
x = np.array(x)
y = np.array(y)
    
x_train = x[:round(size * test_percent)]
y_train = y[:round(size * test_percent)]

x_test = x[round(size * test_percent):]
y_test = y[round(size * test_percent):]

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(2, kernel_initializer='normal',input_dim = x_train.shape[1], activation='relu'))
model.add(tf.keras.layers.Dense(64, kernel_initializer='normal', activation='relu'))
model.add(tf.keras.layers.Dense(128, kernel_initializer='normal', activation='relu'))
model.add(tf.keras.layers.Dense(64, kernel_initializer='normal', activation='relu'))
model.add(tf.keras.layers.Dense(2, kernel_initializer='normal', activation='linear'))

model.compile(optimizer = 'adam',
              loss = 'mean_squared_error',
              metrics = ['mean_squared_error'])

model.fit(x, y, epochs=5)
model.evaluate(x_test, y_test)

def getPredicted(c):
    d = model.predict([c])
    return d[0][0], d[0][1]

def acc(k=0):
    for i in range(k,10+k):
        c = [data[i][0] , data[i][1]]
#        print(c)
        d = getPredicted(c)
        diff = (d[0] - data[i][2]), (d[1] - data[i][3])
        print(diff, data[i][2:], d)


#model.save('model9')
acc()