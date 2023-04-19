import json
productos = [
    { 'nombre': 'jabon', 'id': 1},
    { 'nombre': 'shampoo', 'id': 2},
    { 'nombre': 'crema de enguaje', 'id': 3},
    { 'nombre': 'acondicionador', 'id': 4}
]


# necesito que imprimas los nombres de los productos

# y los agregues a otra lista ordenados por nombre


print(json.dumps(productos, sort_keys=False, indent=4))

for producto in productos:
    print(producto['nombre'])
    
    
