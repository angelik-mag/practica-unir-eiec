import os
import sys

# función sin parámetros o retorno de valores

def leerArchivo(): 
  f = open(sys.argv[1])
  mensaje = f.read()
  print(mensaje) 
  f.close()
 

leerArchivo()