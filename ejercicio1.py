# ejercicio #1

# class Rutina:
#     def __init__(self):
#         self.actividades = {}

#     def agregar_actividad(self, actividad, tiempo):
#         self.actividades[actividad] = tiempo
#     def mostrar_rutina(self):
#         for actividad, tiempo in self.actividades.items():

#             print(f"{actividad}: {tiempo} minutos")

# rutina = Rutina()
# rutina.agregar_actividad('Despertarse', 15)
# rutina.agregar_actividad('Desayunar', 30)
# rutina.agregar_actividad('Tomar un autobús a la universidad', 55)
# rutina.agregar_actividad('Entrar a Clases', 120)
# rutina.agregar_actividad('Tomo un receso', 120)
# rutina.agregar_actividad('Finalización de clases', 0)
# rutina.mostrar_rutina()

# ejercicio #2

# class GrafoMusical:
#     def __init__(self):
#         self.grafo = {}

#     def agregar_cancion(self, cancion):
#         if cancion not in self.grafo:
#             self.grafo[cancion] = []
#     def agregar_transicion(self, cancion_origen, cancion_destino):
#         if cancion_origen in self.grafo and cancion_destino in self.grafo:
#             self.grafo[cancion_origen].append(cancion_destino)
#     def mostrar_grafo(self):
#         for cancion, transiciones in self.grafo.items():
#             print(f"{cancion} puede saltar a: {', '.join(transiciones) if transiciones
#             else 'Ninguna'}")
# def buscar_cancion(self, cancion):
#     if cancion in self.grafo:
#         transiciones = self.grafo[cancion]
#     return f"{cancion} puede saltar a: {', '.join(transiciones) if transiciones
# else 'Ninguna'}"
#     return f"{cancion} no se encuentra en el grafo."
# reproductor = GrafoMusical()
# reproductor.agregar_cancion('Jesus Adrian Romero')
# reproductor.agregar_cancion('Nancy Ramirez')
# reproductor.agregar_cancion('Gladys Munoz')
# reproductor.agregar_cancion('Album')
# reproductor.agregar_transicion('Jesus Adrian Romero', 'Album')
# reproductor.agregar_transicion('Nancy Ramirez', 'Album')
# reproductor.agregar_transicion('Gladys Munoz', 'Album')
# reproductor.mostrar_grafo()

# ejercicio #3

# class GrafoProductos:
#     def __init__(self):
#         self.grafo = {}

#     def agregar_producto(self, producto):
#         if producto not in self.grafo:
#             self.grafo[producto] = []

#     def agregar_relacion(self, producto_origen, producto_destino):
#         if producto_origen in self.grafo and producto_destino in self.grafo:
#             self.grafo[producto_origen].append(producto_destino)

#     def mostrar_grafo(self):
#         for producto, relaciones in self.grafo.items():
#             print(f"{producto} se relaciona con: {', '.join(relaciones) if relaciones else 'Ninguno'}")

#     def buscar_producto(self, producto):
#         if producto in self.grafo:
#             relaciones = self.grafo[producto]
#             return f"{producto} se relaciona con: {', '.join(relaciones) if relaciones else 'Ninguno'}"
#         return f"{producto} no se encuentra en el grafo."


# reproductor = GrafoProductos()

# reproductor.agregar_producto('Electrónicos')
# reproductor.agregar_producto('Bocinas')
# reproductor.agregar_producto('Audífonos')
# reproductor.agregar_producto('Laptop')
# reproductor.agregar_producto('Walmart')
# reproductor.agregar_producto('Vestimenta')
# reproductor.agregar_producto('Suéteres')
# reproductor.agregar_producto('Camisetas')
# reproductor.agregar_producto('Vestidos')
# reproductor.agregar_producto('Frutas')
# reproductor.agregar_producto('Bananas')
# reproductor.agregar_producto('Uvas Verdes')
# reproductor.agregar_producto('Fresas')

# reproductor.agregar_relacion('Electrónicos', 'Bocinas')
# reproductor.agregar_relacion('Electrónicos', 'Audífonos')
# reproductor.agregar_relacion('Electrónicos', 'Laptop')
# reproductor.agregar_relacion('Walmart', 'Electrónicos')
# reproductor.agregar_relacion('Walmart', 'Vestimenta')
# reproductor.agregar_relacion('Walmart', 'Frutas')
# reproductor.agregar_relacion('Frutas', 'Bananas')
# reproductor.agregar_relacion('Frutas', 'Uvas Verdes')
# reproductor.agregar_relacion('Frutas', 'Fresas')
# reproductor.agregar_relacion('Vestimenta', 'Suéteres')
# reproductor.agregar_relacion('Vestimenta', 'Camisetas')
# reproductor.agregar_relacion('Camisetas', 'Vestidos')

# reproductor.mostrar_grafo()

# producto_buscar = input("Ingrese el nombre del producto que desea buscar: ")
# resultado = reproductor.buscar_producto(producto_buscar)
# print(resultado)
