import numpy as np
from sklearn import preprocessing#ayuda a preprocesar los datos de entrada
from sklearn.preprocessing import MinMaxScaler
#input_data = np.array([2.1, -1.9, 5.5],#xyz runner1
#                      [-1.5, 2.4, 3.5])#xyz runner2

# input_data = np.array([2.1, -1.9, 5.5],
#                       [-1.5, 2.4, 3.5],
#                       [0.5, -7.9, 5.6],
#                       [5.9, 2.3, -5.8])
for x in range (0,1):#this metod doesnt work well
	input_data = np.array([[13, 50, 200],
		[802, 23, 38],
		[0, 0, 1240]])

	#input_data = ([13, 50, 200],
	#			  [802, 23, 38],
    #    	      [0, 0, 1240])#1240 es el valor maximo para calibrar el resto de numeros inferiores
	data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0,1))
	data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
	print (input_data)	
	
	print ("Min max scaled data:\n", data_scaled_minmax)
for x in range (0,1):#this one is better and nicer
	#create NumPy array 
	data = np.array([[13, 50, 200],
			  	[802, 23, 38],
           	   [0, 0, 1240]])
	#normalize all values in array
	print ("data whit anoter normalitation")
	print ("same data as the first")
	data_norm = (data - data.min())/ (data.max() - data.min())
	print (data)
	print (data_norm)
