import sys#to change the apend to select correctly betwen folders
import pickle#to load the archive containing the IA
import glob# to import multiple pythons files 
nombre = "Kimberly Reed Lopez"
numero = "53"
clase = "keeper"#runner keeper defender chaser
team = "S "
#from carpeta1.subcarpeta1.archivo3 import VERSION_REL, VERSION_ABS
# setting path
#sys.path.append('/media/root/C64E-F9151/TRABAJO/CYBER_BALL')
sys.path.append("./.") #That's two directories up from the current ("./.")=1 (".../...")=3
from motos import *
#sys.path.append(os.path.abspath('../CYBER_BALL'))
moto = MV9600
moto_name="MV9600      "#siempre deben ser 16 caracteres
velocidad = (moto[0]*1000)/3600#Km/h convertido a m/s
aceleracion = moto[1]#de 0 a 100 en x segundos
maniobrabilidad = moto[2]#%
suerte = 13#probabilidad con la que te puede golpear o no algo si llega  a 0 la probabilidad es 100%
fuerza = 99# capacidad de empujar golpear o mover algun objeto
agilidad = 5# define que tantos movimientos puedes hacer en un determinado tiempo 1segundo
resistencia = 100#capacidad para resistir golpes y mantener stats cuando cae todos los demas stats lo hacen porporcionalmente
#cara# archivo que muestra su cara
#entrada1  x posicion de quafle
#entrada2  y posicion de quafle
#entrada3  z posicion de quafle
#entrada4  x posicion de bulldozer1
#entrada5  y posicion de bulldozer1
#entrada6  z posicion de bulldozer1
#entrada7  x posicion de bulldozer2
#entrada8  y posicion de bulldozer2
#entrada9  z posicion de bulldozer2
#entrada10 x distancia de aros o otro cazador
#entrada11 y distancia de aros o otro cazador
#entrada12 z distancia de aros o otro cazador

#listaRecuperada[0] 
#listaRecuperada[1] 
#listaRecuperada[2] 
#listaRecuperada[3] 
#listaRecuperada[4] 
#listaRecuperada[5] 
#listaRecuperada[6] 
#listaRecuperada[7] 
#listaRecuperada[8] 
#listaRecuperada[9] 
#listaRecuperada[10]
#listaRecuperada[11]
#listaRecuperada[12]

#salida[0] direccion en x con rango de 0 a 1 .5 = sin movimiento
#salida[1] direccion en y con rango de 0 a 1 .5 = sin movimiento
#salida[2] direccion en z con rango de 0 a 1 .5 = sin movimiento

backup = 0

import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
CURR_DIR=CURR_DIR+"/red_neuronal"+numero
#print(CURR_DIR)

#import os
#CURR_DIR = os.getcwd()
print(numero,clase,moto_name,team,nombre)
#print(suerte,fuerza,agilidad)

lista = [.1, .2, .3, .4, .5, .6, .7, .8, .9, .10, .11, .12]
#with open('/media/root/C64E-F9151/TRABAJO/CYBER_BALL/visitantes/jugador1/red_neuronal19', 'wb') as f:#creacion de el archivo donde se almacena el conocimiento de la IA
#    pickle.dump(lista, f)
#with open('/media/root/C64E-F9151/TRABAJO/CYBER_BALL/visitantes/jugador1/red_neuronal19', 'rb') as f:#lectura del conocimiento recabado de la IA
#    listaRecuperada = pickle.load(f)
isFile = os.path.isfile(CURR_DIR)
#print("buscando IA en",CURR_DIR)
if isFile == False:
    with open(CURR_DIR, 'wb') as f:#creacion de el archivo donde se almacena el conocimiento de la IA
        pickle.dump(lista, f)
else:
    with open(CURR_DIR, 'rb') as f:#lectura del conocimiento recabado de la IA
        listaRecuperada = pickle.load(f)
#print(listaRecuperada[1])  #>> Devolver??a la lista [1, 2, 3, 4, 5, 6] guardada en 'listaRecuperada'
#print(velocidad)

def guardar_IA53():
    #listaRecuperada[0]+=1
    with open(CURR_DIR, 'wb') as f:#guarda el archivo donde se almacena el conocimiento de la IA
            pickle.dump(listaRecuperada, f)
            #print(listaRecuperada19[1]) 
            print("guardando IA53")
            print(listaRecuperada)
            
    
       

