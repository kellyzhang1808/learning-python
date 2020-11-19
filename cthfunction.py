def maks (deret : int):
    return max(deret)

if __name__ == "__main__":
    deret=input("Bilangan\t: " ).split(" ")
    deret=list(map(int,deret))
    print(f"Nilai Max\t: {maks(deret)}")