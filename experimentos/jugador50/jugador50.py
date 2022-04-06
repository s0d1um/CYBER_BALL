import pickle#to load the archive containing the IA
import glob# to import multiple pythons files
import sys#to change the apend to select correctly betwen folders
import os#to set where we are
nombre = "name last_name"
numero = "50"
clase = "chaser"#seeker keeper beater chaser
team = "N "
# setting path
#sys.path.append('/media/root/C64E-F9151/TRABAJO/CYBER_BALL')

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
CURR_DIR=CURR_DIR+"/red_neuronal_"+numero
#CURR_DIR = os.getcwd()


CURR_DIR2 = os.path.dirname(os.path.realpath(__file__))
text = '/jugador'+numero
text2 = '/locales'
text3 = '/visitantes'
text4 = '/experimentos'
CURR_DIR2 = CURR_DIR2.removesuffix(text)
CURR_DIR2 = CURR_DIR2.removesuffix(text2)
CURR_DIR2 = CURR_DIR2.removesuffix(text3)
CURR_DIR2 = CURR_DIR2.removesuffix(text4)
sys.path.append(CURR_DIR2)#used to give him the exact potition of motos other wise it doesnt compile of his own
#sys.path.append("./.") #That's two directories up from the current ("./.")=1 (".../...")=3

from motos import *
moto = MV9600
#sys.path.append(os.path.abspath('../CYBER_BALL'))
moto_name="MV9600      "#
velocidad = (moto[0]*1000)/3600#Km/h convertido a m/s
aceleracion = moto[1]#de 0 a 100 en x segundos
maniobrabilidad = moto[2]#%
suerte = 13#probabilidad con la que te puede golpear o no algo si llega  a 0 la probabilidad es 100%
fuerza = 99# capacidad de empujar golpear o mover algun objeto
agilidad = 5# define que tantos movimientos puedes hacer en un determinado tiempo 1segundo
resistencia = 100#capacidad para resistir golpes y mantener stats cuando cae todos los demas stats lo hacen porporcionalmente

print(numero,clase,moto_name,team,nombre)

lista = [.1, .2, .3, .4, .5, .6, .7, .8, .9, .10, .11, .12]

isFile = os.path.isfile(CURR_DIR)#buscando IA en CURR_DIR

if isFile == True:
    with open(CURR_DIR, 'rb') as f:#lectura del conocimiento recabado de la IA
        listaRecuperada = pickle.load(f)
else:
    with open(CURR_DIR, 'wb') as f:#creacion de el archivo donde se almacena el conocimiento de la IA
        pickle.dump(lista, f)
    with open(CURR_DIR, 'rb') as f:#lectura del conocimiento recabado de la IA
        listaRecuperada = pickle.load(f)

def guardar_IA50():
    #listaRecuperada[0]+=1
    with open(CURR_DIR+"_backup.txt", 'w') as f:
    #with open("/red_neuronal"+numero+".py", 'a') as f:
        #f.write(str(listaRecuperada))
        f.write(str(listaRecuperada[0]))
        f.write(",")
        f.write(str(listaRecuperada[1]))
        f.write(",")
        f.write(str(listaRecuperada[2]))
        f.write(",")
        f.write(str(listaRecuperada[3]))
        f.write(",")
        f.write(str(listaRecuperada[4]))
        f.write(",")
        f.write(str(listaRecuperada[5]))
        f.write(",")
        f.write(str(listaRecuperada[6]))
        f.write(",")
        f.write(str(listaRecuperada[7]))
        f.write(",")
        f.write(str(listaRecuperada[8]))
        f.write(",")
        f.write(str(listaRecuperada[9]))
        f.write(",")
        f.write(str(listaRecuperada[10]))
        f.write(",")
        f.write(str(listaRecuperada[11]))

    with open(CURR_DIR, 'wb') as f:#saves the file where is located the knoledge of the IA
            #f.write(listaRecuperada, f)
            pickle.dump(listaRecuperada, f)
            print("guardando IA50")
            print(listaRecuperada)
guardar_IA50()
