#Amanda Rismawati
#101019005
#LATIHAN 3 : Mengurutkan daftar buku berdasarkan jumlah halaman secara ascending 

def bubble_sort_books(DaftarBuku):
    n = len(DaftarBuku)
    for i in range(n):
        for j in range(0, n-i-1):
            if DaftarBuku[j]["JumHal"] > DaftarBuku[j+1]["JumHal"]:
               DaftarBuku[j], DaftarBuku[j+1] = DaftarBuku[j+1], DaftarBuku[j]

DaftarBuku = [
    {"judul": "Harry Potter and the Sorcerer's Stone", "penulis": "J.K. Rowling", "JumHal": 320},
    {"judul": "To Kill a Mockingbird", "penulis": "Harper Lee", "JumHal": 281},
    {"judul": "The Great Gatsby", "penulis": "F. Scott Fitzgerald", "JumHal": 180},
    {"judul": "Pride and Prejudice", "penulis": "Jane Austen", "JumHal": 432},
    {"judul": "1984", "penulis": "George Orwell", "JumHal": 328}
]

bubble_sort_books(DaftarBuku)
print("Daftar buku yang diurutkan berdasarkan jumlah halaman secara ascending:")
for buku in DaftarBuku:
    print("Judul:", buku["judul"])
    print("Penulis:", buku["penulis"])
    print("Jumlah Halaman:", buku["JumHal"])
    print()