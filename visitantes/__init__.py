import os 
import glob# to import multiple pythons files 
# Path 
CURR_DIR2 = os.path.dirname(os.path.realpath(__file__))
CURR_DIR2 = CURR_DIR2+"/"
#print(CURR_DIR2)
bandera_chasers = 0
bandera_beaters = 0

jugadores2 = {}
chaser1_equipo2 = {}#equipo 1 visitantes
chaser2_equipo2 = {}
chaser3_equipo2 = {}
beater1_equipo2 = {}
beater2_equipo2 = {}
keeper_equipo2  = {}
seeker_equipo2  = {}

jugador = "jugador"
r1 = 19 # range minimo
r2 = 100 #range maximo 

#for i in range(r1,r2):#es para no tener que escribir el codigo que importa cada jugador
#    print ("    if jugadores2[",i,"]==True:")
#    print ("        from visitantes.jugador",end='')
#    print (i,end='')
#    print (".jugador",end='')
#    print (i,"import *")
#    print ("        definir_jugador()")
for i in range(0,1):#se llenan los jugadores con datos por default
    for f in range (0,10): chaser1_equipo2[f] = "0"
    for f in range (0,10): chaser2_equipo2[f] = "0"
    for f in range (0,10): chaser3_equipo2[f] = "0"

    for f in range (0,10): beater1_equipo2[f] = "0"
    for f in range (0,10): beater2_equipo2[f] = "0"

    for f in range (0,10): keeper_equipo2[f]  = "0"
    for f in range (0,10): seeker_equipo2[f]  = "0"
for x in range(r1,r2):#analiza si existe jugadores en x carpeta
    number = str(x) 
    path = CURR_DIR2+jugador+number+"/"+jugador+number+".py"#/home/user/jugadorx/jugadorx.py
    isFile = os.path.isfile(path)
    if isFile == True:
      #  print("jugador",x,"detectado en:")
      #  print(path)
        jugadores2[x]=True
    else:jugadores2[x]=False
def definir_jugador():#se definen los datos dependiendo del jugador
    global bandera_beaters
    global bandera_chasers
    global numero,clase
    global chaser1_equipo2_IA,chaser2_equipo2_IA,chaser3_equipo2_IA,beater1_equipo2_IA,beater2_equipo2_IA,keeper_equipo2_IA,seeker_equipo2_IA
    if clase == "chaser":
        bandera_chasers += 1
        if bandera_chasers == 1:
            chaser1_equipo2[0] = numero
            chaser1_equipo2[1] = clase
            chaser1_equipo2[2] = nombre
            chaser1_equipo2[3] = moto_name
            chaser1_equipo2[4] = velocidad#(moto[0]*1000)/3600#Km/h convertido a m/s
            chaser1_equipo2[5] = aceleracion# moto[1]#de 0 a 100 en x segundos
            chaser1_equipo2[6] = maniobrabilidad# moto[2]#%
            chaser1_equipo2[7] = fuerza#capacidad de empujar golpear o mover algun objeto
            chaser1_equipo2[8] = suerte#probabilidad con la que te puede golpear o no algo si llega  a 0 la probabilidad es 100%
            chaser1_equipo2[9] = resistencia#capacidad para resistir golpes y mantener stats cuando cae todos los demas stats lo hacen porporcionalmente
            chaser1_equipo2[10]= team
            chaser1_equipo2_IA = listaRecuperada
        if bandera_chasers == 2:
            chaser2_equipo2[0] = numero
            chaser2_equipo2[1] = clase
            chaser2_equipo2[2] = nombre
            chaser2_equipo2[3] = moto_name
            chaser2_equipo2[4] = velocidad#(moto[0]*1000)/3600#Km/h convertido a m/s
            chaser2_equipo2[5] = aceleracion# moto[1]#de 0 a 100 en x segundos
            chaser2_equipo2[6] = maniobrabilidad# moto[2]#%
            chaser2_equipo2[7] = fuerza#capacidad de empujar golpear o mover algun objeto
            chaser2_equipo2[8] = suerte#probabilidad con la que te puede golpear o no algo si llega  a 0 la probabilidad es 100%
            chaser2_equipo2[9] = resistencia#capacidad para resistir golpes y mantener stats cuando cae todos los demas stats lo hacen porporcionalmente
            chaser2_equipo2[10]= team
            chaser2_equipo2_IA = listaRecuperada
        if bandera_chasers == 3:
            chaser3_equipo2[0] = numero
            chaser3_equipo2[1] = clase
            chaser3_equipo2[2] = nombre
            chaser3_equipo2[3] = moto_name
            chaser3_equipo2[4] = velocidad#(moto[0]*1000)/3600#Km/h convertido a m/s
            chaser3_equipo2[5] = aceleracion# moto[1]#de 0 a 100 en x segundos
            chaser3_equipo2[6] = maniobrabilidad# moto[2]#%
            chaser3_equipo2[7] = fuerza#capacidad de empujar golpear o mover algun objeto
            chaser3_equipo2[8] = suerte#probabilidad con la que te puede golpear o no algo si llega  a 0 la probabilidad es 100%
            chaser3_equipo2[9] = resistencia#capacidad para resistir golpes y mantener stats cuando cae todos los demas stats lo hacen porporcionalmente
            chaser3_equipo2[10]= team
            chaser3_equipo2_IA = listaRecuperada
    if clase == "beater":
        bandera_beaters += 1
        if bandera_beaters == 1:
            beater1_equipo2[0] = numero
            beater1_equipo2[1] = clase
            beater1_equipo2[2] = nombre
            beater1_equipo2[3] = moto_name
            beater1_equipo2[4] = velocidad#(moto[0]*1000)/3600#Km/h convertido a m/s
            beater1_equipo2[5] = aceleracion# moto[1]#de 0 a 100 en x segundos
            beater1_equipo2[6] = maniobrabilidad# moto[2]#%
            beater1_equipo2[7] = fuerza#capacidad de empujar golpear o mover algun objeto
            beater1_equipo2[8] = suerte#probabilidad con la que te puede golpear o no algo si llega  a 0 la probabilidad es 100%
            beater1_equipo2[9] = resistencia#capacidad para resistir golpes y mantener stats cuando cae todos los demas stats lo hacen porporcionalmente
            beater1_equipo2[10]= team
            beater1_equipo2_IA = listaRecuperada
        if bandera_beaters == 2:
            beater2_equipo2[0] = numero
            beater2_equipo2[1] = clase
            beater2_equipo2[2] = nombre
            beater2_equipo2[3] = moto_name
            beater2_equipo2[4] = velocidad#(moto[0]*1000)/3600#Km/h convertido a m/s
            beater2_equipo2[5] = aceleracion# moto[1]#de 0 a 100 en x segundos
            beater2_equipo2[6] = maniobrabilidad# moto[2]#%
            beater2_equipo2[7] = fuerza#capacidad de empujar golpear o mover algun objeto
            beater2_equipo2[8] = suerte#probabilidad con la que te puede golpear o no algo si llega  a 0 la probabilidad es 100%
            beater2_equipo2[9] = resistencia#capacidad para resistir golpes y mantener stats cuando cae todos los demas stats lo hacen porporcionalmente
            beater2_equipo2[10]= team
            beater2_equipo2_IA = listaRecuperada
    if clase == "keeper":
        keeper_equipo2[0] = numero
        keeper_equipo2[1] = clase
        keeper_equipo2[2] = nombre
        keeper_equipo2[3] = moto_name
        keeper_equipo2[4] = velocidad#(moto[0]*1000)/3600#Km/h convertido a m/s
        keeper_equipo2[5] = aceleracion# moto[1]#de 0 a 100 en x segundos
        keeper_equipo2[6] = maniobrabilidad# moto[2]#%
        keeper_equipo2[7] = fuerza#capacidad de empujar golpear o mover algun objeto
        keeper_equipo2[8] = suerte#probabilidad con la que te puede golpear o no algo si llega  a 0 la probabilidad es 100%
        keeper_equipo2[9] = resistencia#capacidad para resistir golpes y mantener stats cuando cae todos los demas stats lo hacen porporcionalmente
        keeper_equipo2[10]= team
        keeper_equipo2_IA = listaRecuperada
    if clase == "seeker":
        seeker_equipo2[0] = numero
        seeker_equipo2[1] = clase
        seeker_equipo2[2] = nombre
        seeker_equipo2[3] = moto_name
        seeker_equipo2[4] = velocidad#(moto[0]*1000)/3600#Km/h convertido a m/s
        seeker_equipo2[5] = aceleracion# moto[1]#de 0 a 100 en x segundos
        seeker_equipo2[6] = maniobrabilidad# moto[2]#%
        seeker_equipo2[7] = fuerza#capacidad de empujar golpear o mover algun objeto
        seeker_equipo2[8] = suerte#probabilidad con la que te puede golpear o no algo si llega  a 0 la probabilidad es 100%
        seeker_equipo2[9] = resistencia#capacidad para resistir golpes y mantener stats cuando cae todos los demas stats lo hacen porporcionalmente
        seeker_equipo2[10]= team
        seeker_equipo2_IA = listaRecuperada
for i in range(0,1):#importar caracteristicas 1 por 1
    if jugadores2[ 19 ]==True:
        from visitantes.jugador19.jugador19 import *
        definir_jugador()
    if jugadores2[ 20 ]==True:
        from visitantes.jugador20.jugador20 import *
        definir_jugador()
    if jugadores2[ 21 ]==True:
        from visitantes.jugador21.jugador21 import *
        definir_jugador()
    if jugadores2[ 22 ]==True:
        from visitantes.jugador22.jugador22 import *
        definir_jugador()
    if jugadores2[ 23 ]==True:
        from visitantes.jugador23.jugador23 import *
        definir_jugador()
    if jugadores2[ 24 ]==True:
        from visitantes.jugador24.jugador24 import *
        definir_jugador()
    if jugadores2[ 25 ]==True:
        from visitantes.jugador25.jugador25 import *
        definir_jugador()
    if jugadores2[ 26 ]==True:
        from visitantes.jugador26.jugador26 import *
        definir_jugador()
    if jugadores2[ 27 ]==True:
        from visitantes.jugador27.jugador27 import *
        definir_jugador()
    if jugadores2[ 28 ]==True:
        from visitantes.jugador28.jugador28 import *
        definir_jugador()
    if jugadores2[ 29 ]==True:
        from visitantes.jugador29.jugador29 import *
        definir_jugador()
    if jugadores2[ 30 ]==True:
        from visitantes.jugador30.jugador30 import *
        definir_jugador()
    if jugadores2[ 31 ]==True:
        from visitantes.jugador31.jugador31 import *
        definir_jugador()
    if jugadores2[ 32 ]==True:
        from visitantes.jugador32.jugador32 import *
        definir_jugador()
    if jugadores2[ 33 ]==True:
        from visitantes.jugador33.jugador33 import *
        definir_jugador()
    if jugadores2[ 34 ]==True:
        from visitantes.jugador34.jugador34 import *
        definir_jugador()
    if jugadores2[ 35 ]==True:
        from visitantes.jugador35.jugador35 import *
        definir_jugador()
    if jugadores2[ 36 ]==True:
        from visitantes.jugador36.jugador36 import *
        definir_jugador()
    if jugadores2[ 37 ]==True:
        from visitantes.jugador37.jugador37 import *
        definir_jugador()
    if jugadores2[ 38 ]==True:
        from visitantes.jugador38.jugador38 import *
        definir_jugador()
    if jugadores2[ 39 ]==True:
        from visitantes.jugador39.jugador39 import *
        definir_jugador()
    if jugadores2[ 40 ]==True:
        from visitantes.jugador40.jugador40 import *
        definir_jugador()
    if jugadores2[ 41 ]==True:
        from visitantes.jugador41.jugador41 import *
        definir_jugador()
    if jugadores2[ 42 ]==True:
        from visitantes.jugador42.jugador42 import *
        definir_jugador()
    if jugadores2[ 43 ]==True:
        from visitantes.jugador43.jugador43 import *
        definir_jugador()
    if jugadores2[ 44 ]==True:
        from visitantes.jugador44.jugador44 import *
        definir_jugador()
    if jugadores2[ 45 ]==True:
        from visitantes.jugador45.jugador45 import *
        definir_jugador()
    if jugadores2[ 46 ]==True:
        from visitantes.jugador46.jugador46 import *
        definir_jugador()
    if jugadores2[ 47 ]==True:
        from visitantes.jugador47.jugador47 import *
        definir_jugador()
    if jugadores2[ 48 ]==True:
        from visitantes.jugador48.jugador48 import *
        definir_jugador()
    if jugadores2[ 49 ]==True:
        from visitantes.jugador49.jugador49 import *
        definir_jugador()
    if jugadores2[ 50 ]==True:
        from visitantes.jugador50.jugador50 import *
        definir_jugador()
    if jugadores2[ 51 ]==True:
        from visitantes.jugador51.jugador51 import *
        definir_jugador()
    if jugadores2[ 52 ]==True:
        from visitantes.jugador52.jugador52 import *
        definir_jugador()
    if jugadores2[ 53 ]==True:
        from visitantes.jugador53.jugador53 import *
        definir_jugador()
    if jugadores2[ 54 ]==True:
        from visitantes.jugador54.jugador54 import *
        definir_jugador()
    if jugadores2[ 55 ]==True:
        from visitantes.jugador55.jugador55 import *
        definir_jugador()
    if jugadores2[ 56 ]==True:
        from visitantes.jugador56.jugador56 import *
        definir_jugador()
    if jugadores2[ 57 ]==True:
        from visitantes.jugador57.jugador57 import *
        definir_jugador()
    if jugadores2[ 58 ]==True:
        from visitantes.jugador58.jugador58 import *
        definir_jugador()
    if jugadores2[ 59 ]==True:
        from visitantes.jugador59.jugador59 import *
        definir_jugador()
    if jugadores2[ 60 ]==True:
        from visitantes.jugador60.jugador60 import *
        definir_jugador()
    if jugadores2[ 61 ]==True:
        from visitantes.jugador61.jugador61 import *
        definir_jugador()
    if jugadores2[ 62 ]==True:
        from visitantes.jugador62.jugador62 import *
        definir_jugador()
    if jugadores2[ 63 ]==True:
        from visitantes.jugador63.jugador63 import *
        definir_jugador()
    if jugadores2[ 64 ]==True:
        from visitantes.jugador64.jugador64 import *
        definir_jugador()
    if jugadores2[ 65 ]==True:
        from visitantes.jugador65.jugador65 import *
        definir_jugador()
    if jugadores2[ 66 ]==True:
        from visitantes.jugador66.jugador66 import *
        definir_jugador()
    if jugadores2[ 67 ]==True:
        from visitantes.jugador67.jugador67 import *
        definir_jugador()
    if jugadores2[ 68 ]==True:
        from visitantes.jugador68.jugador68 import *
        definir_jugador()
    if jugadores2[ 69 ]==True:
        from visitantes.jugador69.jugador69 import *
        definir_jugador()
    if jugadores2[ 70 ]==True:
        from visitantes.jugador70.jugador70 import *
        definir_jugador()
    if jugadores2[ 71 ]==True:
        from visitantes.jugador71.jugador71 import *
        definir_jugador()
    if jugadores2[ 72 ]==True:
        from visitantes.jugador72.jugador72 import *
        definir_jugador()
    if jugadores2[ 73 ]==True:
        from visitantes.jugador73.jugador73 import *
        definir_jugador()
    if jugadores2[ 74 ]==True:
        from visitantes.jugador74.jugador74 import *
        definir_jugador()
    if jugadores2[ 75 ]==True:
        from visitantes.jugador75.jugador75 import *
        definir_jugador()
    if jugadores2[ 76 ]==True:
        from visitantes.jugador76.jugador76 import *
        definir_jugador()
    if jugadores2[ 77 ]==True:
        from visitantes.jugador77.jugador77 import *
        definir_jugador()
    if jugadores2[ 78 ]==True:
        from visitantes.jugador78.jugador78 import *
        definir_jugador()
    if jugadores2[ 79 ]==True:
        from visitantes.jugador79.jugador79 import *
        definir_jugador()
    if jugadores2[ 80 ]==True:
        from visitantes.jugador80.jugador80 import *
        definir_jugador()
    if jugadores2[ 81 ]==True:
        from visitantes.jugador81.jugador81 import *
        definir_jugador()
    if jugadores2[ 82 ]==True:
        from visitantes.jugador82.jugador82 import *
        definir_jugador()
    if jugadores2[ 83 ]==True:
        from visitantes.jugador83.jugador83 import *
        definir_jugador()
    if jugadores2[ 84 ]==True:
        from visitantes.jugador84.jugador84 import *
        definir_jugador()
    if jugadores2[ 85 ]==True:
        from visitantes.jugador85.jugador85 import *
        definir_jugador()
    if jugadores2[ 86 ]==True:
        from visitantes.jugador86.jugador86 import *
        definir_jugador()
    if jugadores2[ 87 ]==True:
        from visitantes.jugador87.jugador87 import *
        definir_jugador()
    if jugadores2[ 88 ]==True:
        from visitantes.jugador88.jugador88 import *
        definir_jugador()
    if jugadores2[ 89 ]==True:
        from visitantes.jugador89.jugador89 import *
        definir_jugador()
    if jugadores2[ 90 ]==True:
        from visitantes.jugador90.jugador90 import *
        definir_jugador()
    if jugadores2[ 91 ]==True:
        from visitantes.jugador91.jugador91 import *
        definir_jugador()
    if jugadores2[ 92 ]==True:
        from visitantes.jugador92.jugador92 import *
        definir_jugador()
    if jugadores2[ 93 ]==True:
        from visitantes.jugador93.jugador93 import *
        definir_jugador()
    if jugadores2[ 94 ]==True:
        from visitantes.jugador94.jugador94 import *
        definir_jugador()
    if jugadores2[ 95 ]==True:
        from visitantes.jugador95.jugador95 import *
        definir_jugador()
    if jugadores2[ 96 ]==True:
        from visitantes.jugador96.jugador96 import *
        definir_jugador()
    if jugadores2[ 97 ]==True:
        from visitantes.jugador97.jugador97 import *
        definir_jugador()
    if jugadores2[ 98 ]==True:
        from visitantes.jugador98.jugador98 import *
        definir_jugador()
    if jugadores2[ 99 ]==True:
        from visitantes.jugador99.jugador99 import *
        definir_jugador()

