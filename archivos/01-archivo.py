from pathlib import Path
from time import ctime

archivo = Path("archivo-prueba.txt")

print("acceso", ctime(archivo.stat().st_atime))
print("creacion", ctime(archivo.stat().st_ctime))
print("modificacion", ctime(archivo.stat().st_mtime))