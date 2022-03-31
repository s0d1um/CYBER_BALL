import os
jugadores_lista1 = {}
jugadores_lista2 = {}
jugadores = {}
i = ""
# Path 
CURR_DIR2 = os.path.dirname(os.path.realpath(__file__))
CURR_DIR2 = CURR_DIR2+"/"
file = open("numeros_ocupados.txt", "w")
for x in range(19,100):
    number = str(x) 
    path = CURR_DIR2+"visitantes/jugador"+number+".py"
    isFile = os.path.isfile(path)
    if isFile == True:
      #  print("jugador",x,"detectado")
      #  print(path)
        jugadores[x]=True
    else: jugadores[x]=False
    path = CURR_DIR2+"locales/jugador"+number+".py"
    isFile = os.path.isfile(path)
    if isFile == True:
      #  print("jugador",x,"detectado")
      #  print(path)
      if jugadores[x]==True:
        print ("conflicto 2 jugadores con el mismo numero")
      else: jugadores[x]=True
    else: jugadores[x]=False


for x in range(19,100):
    if jugadores[x] == False:
        i = str(x)
        file.write(i)
        file.write(" libre" + os.linesep)
        print (i,"libre")
    else:
        file.write(i)
        file.write(" ocupado" + os.linesep)
        print (i,"ocupado")

file.close()
