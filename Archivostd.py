# archivos.py

import csv

def guardar_inventario(nombre_archivo, productos):
    with open(nombre_archivo, 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        for producto in productos:
            writer.writerow([
                producto['codigo'],
                producto['nombre'],
                producto['marca'],
                producto['precio'],
                producto['existencias'],
                producto['proveedor']['codigo'],
                producto['proveedor']['nombre'],
                producto['proveedor']['pais']
            ])

def cargar_inventario(nombre_archivo):
    productos = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            reader = csv.reader(archivo)
            for fila in reader:
                producto = {
                    'codigo': fila[0],
                    'nombre': fila[1],
                    'marca': fila[2],
                    'precio': float(fila[3]),
                    'existencias': int(fila[4]),
                    'proveedor': {
                        'codigo': fila[5],
                        'nombre': fila[6],
                        'pais': fila[7]
                    }
                }
                productos.append(producto)
    except FileNotFoundError:
        print("El archivo no existe. Comenzando con un inventario vacío.")
    return productos
