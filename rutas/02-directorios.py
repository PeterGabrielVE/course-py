from pathlib import Path

path = Path("rutas")
#path.exists()
#path.mkdir()
#path.rmdir()
#path.rename("pepe feliz")
#print(path.iterdir())

for p in path.iterdir():
    print(p)