import os
x=r'visitantes'
for r,d,f in os.walk(x):
   for i in f:
      print(os.path.join(r,i))







      x=r'visitantes'
for r,d,f in os.walk(x):
   for i in f:
    jugadorx = CURR_DIR+r+'/*.py'
    print(jugadorx)
    #modules = glob.glob(jugadorx)
    glob.glob(jugadorx)