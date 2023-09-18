from io import open

#texto = "Hola mundo"

#archivo = open("hola-mundo.txt","w")
#archivo.write(texto)
#archivo.close()

archivo = open("hola-mundo.txt","r")
texto = archivo.read()
archivo.close()

print(texto)