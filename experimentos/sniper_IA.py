import numpy as np
from sklearn import preprocessing#ayuda a preprocesar los datos de entrada
from sklearn.preprocessing import MinMaxScaler
#input_data = np.array([2.1, -1.9, 5.5],#xyz seeker1
#                      [-1.5, 2.4, 3.5])#xyz seeker2

# input_data = np.array([2.1, -1.9, 5.5],
#                       [-1.5, 2.4, 3.5],
#                       [0.5, -7.9, 5.6],
#                       [5.9, 2.3, -5.8])
input_data = ([13, 50, 200],
			  [802, 23, 38],
              [0, 0, 1240])#1240 es el valor maximo para calibrar el resto de numeros inferiores
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print ("\nMin max scaled data:\n", data_scaled_minmax)
print (input_data[0])
print (input_data[1])

#create NumPy array
data = np.array([[620, 0, 1240]])

#normalize all values in array
data_norm = (data - data.min())/ (data.max() - data.min())

print (data_norm)
