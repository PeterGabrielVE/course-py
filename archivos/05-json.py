import json
from pathlib import Path 

productos = [
    {"id":1, "name":"Test 1"},
    {"id":2, "name":"Test 2"},
    {"id":3, "name":"Test 3"}
]

data = json.dumps(productos)
#print(data)
Path("productos.json").write_text(data)