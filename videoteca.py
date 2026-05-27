videoteca = [
    ["Inception", 2010, 9, "Ciencia Ficción"],
    ["Avatar", 2022, 8, "Acción"],
    ["Titanic", 1997, 9, "Drama"],
    ["Interstellar", 2014, 10, "Ciencia Ficción"],
    ["Joker", 2019, 8, "Drama"],
    ["The Batman", 2022, 7, "Acción"],
    ["Dune", 2021, 9, "Ciencia Ficción"],
     ["Oppenheimer", 2023, 9, "Drama"],
    ["Spider-Man: No Way Home", 2021, 8, "Acción"],
    ["Soul", 2020, 8, "Animación"]
]




def contar_populares_recientes(matriz, umbral_calificacion, anio_limite):
    contador = 0
    for titulo, anio, calificacion, genero in matriz:
        if calificacion >= umbral_calificacion and anio >= anio_limite:
            contador += 1
    return contador
umbral = float(input("Ingrese la calificación mínima: "))
anio_limite = int(input("Ingrese el año límite: "))
resultado = contar_populares_recientes(videoteca, umbral, anio_limite)
print("Cantidad de títulos populares y recientes:", resultado)



# Preguntar si desea ver la lista
mostrar = input("¿Desea ver cuáles son las películas que cumplen con los criterios? (s/n): ")

if mostrar.lower() == "s":
    peliculas_validas = [(titulo, anio, calificacion, genero) 
                         for titulo, anio, calificacion, genero in videoteca
                         if calificacion >= umbral and anio >= anio_limite]
    
    print("\nPelículas que cumplen con los criterios:")
    for titulo, anio, calificacion, genero in peliculas_validas:
        print(f"{titulo} - Año: {anio}, Calificación: {calificacion}, Género: {genero}")
else:
    print("No se mostrará la lista de películas.")
