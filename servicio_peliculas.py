import os.path
from pelicula import Pelicula

class ServicioPeliculas:

    NOMBRE_ARCHIVO = "peliculas.txt"

    def __init__(self):
        #Inicializamos la lista para guardar las peliculas
        self.peliculas = []

        # Revisar si ya existe el archivo peliculas
        # Si ya existe, obtenemos las peliculas del archivo
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.peliculas = self.obtener_peliculas()
        else:
            print("No hay peliculas todavia")


    # Funcion que utilzamos 
    def obtener_peliculas(self):
        peliculas = []

        try: 
            # Abrimos el archivo para recorrelo y sacar los nombres de las peliculas
            with open(self.NOMBRE_ARCHIVO, "r") as archivo:
                # Recorremos linea a linea el archivo para recoger los nombres
                for linea in archivo:
                    nombre = linea.strip()
                    pelicula = Pelicula(nombre)
                    peliculas.append(pelicula)

        except Exception as e:
            print(f"Error al leer el archivo {e}")

        return peliculas

    #Voy a crear la funcion que guarda las peliculas en el archivo 
    def guardar_peliculas_archivo(self,peliculas):
        try:
            with open(self.NOMBRE_ARCHIVO, "a") as archivo:
                for pelicula in peliculas:
                    archivo.write(f"{pelicula.nombre}\n")
        except Exception as e:
            print(f"No se pudo guardar la pelicula en el archivo:{e}")
    
    # Metodo  para agregar_pelicula()
    def agregar_pelicula(self,pelicula):
        self.peliculas.append(pelicula)
        self.guardar_peliculas_archivo([pelicula])


    # Metodo para listar_peliculas()
    def listar_peliculas(self):
        print("--- Peliculas en el catalogo ---")
        for pelicula in self.peliculas:
            print(pelicula)

    # Metodo eliminar_peliculas()
