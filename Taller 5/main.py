import json
Bodega = "Taller 5/productos.json"

productos= {
    "productos": [
        {
            "id": 1,
            "nombre": "Mouse",
            "precio": 10
        },
        {
            "id": 2,
            "nombre": "Pantalla",
            "precio": 50
        },
        {
            "id": 3,
            "nombre": "Teclado",
            "precio": 20
        }
    ]
}

with open(Bodega, 'w', encoding="utf-8" ) as file:
    json.dump(productos, file, indent=2)

try :
    
    with open(Bodega, "r", enconding="utf-8" ) as file:
        datos = json.load(file)

    nuevo_producto = {"id": 4, "nombre": "Webcam", "precio": 40}
    datos["productos"].append(nuevo_producto)

    with open(Bodega, "w", encoding="utf-8") as file:
        json.dump(productos, file, indent=2)

    print("Productos agregado correctamente")

except json.JSONDecodeError:
    print("Error: El archivo JSON esta mal formado.")
except FileNotFoundError:
    print("Error: El archivo no existe.")
except Exception as e:
    print("Error inesperado: {e}.")