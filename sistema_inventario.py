# sistema_inventario.py

class Producto:
    """
    Clase que representa un producto individual en el inventario.
    """
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.set_nombre(nombre)
        self.actualizar_precio(precio)
        self.actualizar_cantidad(cantidad)

    def set_nombre(self, nombre: str):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self.nombre = nombre.strip()

    def actualizar_precio(self, nuevo_precio: float):
        if not isinstance(nuevo_precio, (int, float)):
            raise TypeError("El precio debe ser un número válido.")
        if nuevo_precio < 0:
            raise ValueError("El precio debe ser mayor o igual a cero.")
        self.precio = float(nuevo_precio)

    def actualizar_cantidad(self, nueva_cantidad: int):
        if not isinstance(nueva_cantidad, int):
            raise TypeError("La cantidad debe ser un número entero.")
        if nueva_cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual a cero.")
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self) -> float:
        return self.precio * self.cantidad

    def __str__(self) -> str:
        return (f"Nombre: {self.nombre:<15} | "
                f"Precio: ${self.precio:>8.2f} | "
                f"Cantidad: {self.cantidad:>4} | "
                f"Valor Total: ${self.calcular_valor_total():>9.2f}")


class Inventario:
    """
    Clase que gestiona la colección de productos.
    """
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos de tipo Producto al inventario.")
        
        # Verificar si el producto ya existe para evitar duplicados
        existente = self.buscar_producto(producto.nombre)
        if existente:
            raise ValueError(f"El producto '{producto.nombre}' ya existe en el inventario.")
            
        self.productos.append(producto)

    def buscar_producto(self, nombre: str):
        if not isinstance(nombre, str):
            return None
        nombre_normalizado = nombre.strip().lower()
        for prod in self.productos:
            if prod.nombre.lower() == nombre_normalizado:
                return prod
        return None

    def calcular_valor_inventario(self) -> float:
        return sum(prod.calcular_valor_total() for prod in self.productos)

    def listar_productos(self):
        if not self.productos:
            print("\n[!] El inventario está vacío.")
            return

        print("\n" + "=" * 65)
        print(f"{'LISTADO DE PRODUCTOS':^65}")
        print("=" * 65)
        for i, prod in enumerate(self.productos, 1):
            print(f"{i}. {prod}")
        print("=" * 65)


def menu_principal():
    """
    Función que despliega el menú interactivo por consola.
    """
    inventario = Inventario()

    while True:
        print("\n" + "—" * 40)
        print("    SISTEMA DE GESTIÓN DE INVENTARIO    ")
        print("—" * 40)
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")
        print("—" * 40)

        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            print("\n--- AGREGAR NUEVO PRODUCTO ---")
            try:
                nombre = input("Ingrese el nombre del producto: ")
                precio_input = input("Ingrese el precio del producto: ")
                cantidad_input = input("Ingrese la cantidad inicial: ")

                # Validaciones previas de conversión de tipo
                try:
                    precio = float(precio_input)
                except ValueError:
                    raise TypeError("El precio ingresado debe ser un número decimal o entero válidos.")

                try:
                    cantidad = int(cantidad_input)
                except ValueError:
                    raise TypeError("La cantidad ingresada debe ser un número entero válido.")

                nuevo_producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(nuevo_producto)
                print(f"\n[✓] ¡Producto '{nuevo_producto.nombre}' agregado con éxito!")

            except (ValueError, TypeError) as e:
                print(f"\n[X] Error al agregar producto: {e}")

        elif opcion == "2":
            print("\n--- BUSCAR PRODUCTO ---")
            nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
            
            try:
                producto_encontrado = inventario.buscar_producto(nombre_buscar)
                if producto_encontrado:
                    print("\n[✓] Producto encontrado:")
                    print(f"    {producto_encontrado}")
                else:
                    print(f"\n[!] No se encontró ningún producto con el nombre '{nombre_buscar.strip()}'.")
            except Exception as e:
                print(f"\n[X] Ocurrió un error en la búsqueda: {e}")

        elif opcion == "3":
            inventario.listar_productos()

        elif opcion == "4":
            valor_total = inventario.calcular_valor_inventario()
            print("\n" + "=" * 45)
            print(f" VALOR TOTAL DEL INVENTARIO: ${valor_total:,.2f}")
            print("=" * 45)

        elif opcion == "5":
            print("\n¡Gracias por utilizar el sistema de inventario! Hasta luego.\n")
            break

        else:
            print("\n[X] Opción inválida. Por favor, ingrese un número del 1 al 5.")


if __name__ == "__main__":
    menu_principal()
