from servicio_peliculas import ServicioPeliculas
from pelicula import Pelicula


class AppCatalogoPeliculas:

    # Declaramos el constructor de las clase
    def __init__(self):
        self.servicio_peliculas = ServicioPeliculas()
    

    #  Funcion que nos va a mostrar la peliculas que hay 
    def catalogo_peliculas(self):
        salir = False
        print("*** Bienvenido al catalogo de peliculas ***")
        self.servicio_peliculas.listar_peliculas()
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception  as e:
                print(f"Ocurrio un error: {e}")

    # Funcion que nos mostrara en pantalla el menu  junto con un imput 
    # donde vamos a introducir la opcion que queremos 
    def mostrar_menu(self):
        print(f"""Menu:
              1. Agregar pelicula
              2. Listar peliculas
              3. Eliminar peliculas
              4. Salir
              """)
        return int(input("Elige una opcion: "))
    
    # Funcion que recoge la opcion y ejecuta el metodo correspondiente
    def ejecutar_opcion(self,opcion):
        if opcion == 1:
            self.agregar_pelicula()
        elif opcion == 2:
            self.servicio_peliculas.listar_peliculas()
        elif opcion == 3:   
            pass
        elif opcion == 4:
            print("Hasta la proxima !")
            return True
        else:
            print(f"Opcion no valida: {opcion}")
        return False
    
    # Funcion para agregar snacks 
    def agregar_pelicula(self):
        nombre = input("Nombre de la pelicula:   ")
        nueva_pelicula = Pelicula(nombre)
        self.servicio_peliculas.agregar_pelicula(nueva_pelicula)
        print("Pelicula agregada correcttamente")

# Programa principal
if __name__ == "__main__":
    app_catalogo_peliculas = AppCatalogoPeliculas()
    app_catalogo_peliculas.catalogo_peliculas()
    

