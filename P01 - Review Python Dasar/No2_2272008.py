# File : No2_2272008.py
# Penulis : Elmosius Suli
# Membuat dua buah fungsi, di mana fungsi pertama akan menghitungkan
# dan mengembalikan jumlah nilai dari list yang dimasukan ke dalam fungsi
# lalu fungsi kedua akan menghitung dan mengembalikan rata-rata
# (mean) dari list yang dimasukan ke dalam fungsi.

# Definisi Fungsi sumList()
# Kamus data
# total : var. total hasil dari perjumlahan(int) 
# num L  var. angka pada di list (int)
def sumList(list_data):
    total = 0
    for num in list_data:
        total += num
    return total

# Definisi Fungsi meanList()
# Kamus data
# total : var. total hasil dari perjumlahan(int)
# mean : var. menghitung rata-rata
def meanList(list_data):
    total = sumList(list_data)
    mean = total / len(list_data)
    return mean

## Program utama ##
# Kamus lokal :
# list_data : var. list penyimpanan datanya (list)
# n : var. input jumlah data (int)
# i : var. parameter for (int)
# data : var. input data untuk list(int)
def main():
    list_data = []
    n = int(input("Masukkan jumlah data: "))

    # input
    for i in range(n):
        data = int(input("Data ke-%d: " % (i + 1)))
        list_data.append(data)

    # hasil
    print("Jumlah:", sumList(list_data))
    print("Rata-rata:", meanList(list_data))

if __name__ == "__main__":
  main()
