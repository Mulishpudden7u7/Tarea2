def main():
    frutas = ["Mango", "Manzana", "Banana", "Uvas"]

    print(frutas)

    del frutas[0]
    del frutas[1]
    frutas.append("sandia")

    print(frutas)

if __name__ == "__main__":
    main()
