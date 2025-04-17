from servicio_peliculas import ServicioPeliculas



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
                pass
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
    

    

