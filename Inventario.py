#Inventario

productos = []
proveedores = [
    {'codigo': '1', 'nombre': 'Proveedor A', 'pais': 'USA'},
    {'codigo': '2', 'nombre': 'Proveedor B', 'pais': 'China'},
    {'codigo': '3', 'nombre': 'Proveedor C', 'pais': 'Germany'}
]


def mostrar_menu():
    print("\nMenú Principal")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar precio de producto")
    print("4. Listar productos")
    print("5. Buscar producto")
    print("6. Guardar inventario en archivo")
    print("7. Cargar inventario desde archivo")
    print("8. Salir")


def agregar_producto():
    codigo = input("Ingrese el código del producto: ")
    if any(p['codigo'] == codigo for p in productos):
        print("El código del producto ya existe.")
        return
    nombre = input("Ingrese el nombre del producto: ")
    marca = input("Ingrese la marca del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    existencias = int(input("Ingrese las existencias del producto: "))

    print("Proveedores disponibles:")
    for idx, proveedor in enumerate(proveedores, start=1):
        print(f"{idx}. {proveedor['nombre']} ({proveedor['pais']})")

    proveedor_idx = int(input("Seleccione un proveedor por su número: ")) - 1
    proveedor = proveedores[proveedor_idx]

    producto = {
        'codigo': codigo,
        'nombre': nombre,
        'marca': marca,
        'precio': precio,
        'existencias': existencias,
        'proveedor': proveedor
    }
    productos.append(producto)
    print("Producto agregado exitosamente.")


def eliminar_producto():
    codigo = input("Ingrese el código del producto a eliminar: ")
    global productos
    productos = [p for p in productos if p['codigo'] != codigo]
    print("Producto eliminado exitosamente.")


def actualizar_precio_producto():
    codigo = input("Ingrese el código del producto a actualizar: ")
    for producto in productos:
        if producto['codigo'] == codigo:
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            producto['precio'] = nuevo_precio
            print("Precio actualizado exitosamente.")
            return
    print("Producto no encontrado.")


def listar_productos():
    if not productos:
        print("No hay productos en el inventario.")
    for producto in productos:
        print(
            f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Marca: {producto['marca']}, Precio: {producto['precio']}, Existencias: {producto['existencias']}, Proveedor: {producto['proveedor']['nombre']}")


def buscar_producto():
    codigo = input("Ingrese el código del producto a buscar: ")
    for producto in productos:
        if producto['codigo'] == codigo:
            print(
                f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Marca: {producto['marca']}, Precio: {producto['precio']}, Existencias: {producto['existencias']}, Proveedor: {producto['proveedor']['nombre']}")
            return
    print("Producto no encontrado.")


def main():
    global productos
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            eliminar_producto()
        elif opcion == '3':
            actualizar_precio_producto()
        elif opcion == '4':
            listar_productos()
        elif opcion == '5':
            buscar_producto()
        elif opcion == '6':
            guardar_inventario('inventario.txt', productos)
        elif opcion == '7':
            productos = cargar_inventario('inventario.txt')
        elif opcion == '8':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
