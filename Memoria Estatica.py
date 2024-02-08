def main():
    calificaciones = []
    for i in range(5):
        calificacion = int(input("Captura la calificación {}: ".format(i + 1)))
        calificaciones.append(calificacion)
    print("Calificaciones ingresadas:", calificaciones)
if __name__ == "__main__":
    main()

