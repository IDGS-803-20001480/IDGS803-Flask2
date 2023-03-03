"""
f = open("alumnos.txt", "r")
nombre = f.read()
print(nombre)
f.seek(0)
nombre2 = f.read()
print(nombre2)

f.close()
"""

#lee una sola linea
"""
f = open("alumnos.txt", "r")
nombre = f.readline()
print(nombre)

f.close()
"""
#lee toda el texto separandolos en una lista
"""
f = open("alumnos.txt", "r")
nombre = f.readlines()

for item in nombre:
    print(item, end=" ")
f.close()
"""

#escribir en un archivo sustiyutendo lo anterior
"""
f=open("alumnos.txt", "w")
f.write("Hola mundo!!!")
f.close()
"""

#escribir en un archivo sin sustituir lo anterior
f=open("alumnos.txt", "a")
f.write("\n"+"!!!!!Hola mundo!!!")
f.close()
