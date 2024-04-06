# File : No1_2272008.py
# Penulis : Elmosius Suli
# Program aplikasi yang meminta pengguna untuk memasukan 
# bilangan bulat jikalau genap akan menampilkan pola persergi
# dan jikalau ganjil pola segitiga
# Kamus Data
# n : var. input N(int)
# i : var. parameter for (int)
# j : var. parameter for2 (int)
def main():
    n = int(input("N : "))
    
    # Segiempat (genap)
    if (n % 2 == 0):
        for i in range(n):
            for j in range(n):
                print("*", end=" ")
            print()
            
    # # Segitiga sama sisi(ganjil) 
    else:
        for i in range(n):
            for j in range(i):
                print("*", end=" ")
            print()
    
if __name__ == "__main__":
    main()