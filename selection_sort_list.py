#Amanda Rismawati
#10109005
#LATIHAN 4 : Mengurutkan daftar angka menggunakan selection sort

def selection_sort(Milik_Andi):
    n = len(Milik_Andi)
    for i in range(n):
        min_indeks = i
        for j in range(i+1, n):
            if Milik_Andi[j] < Milik_Andi[min_indeks]:
                min_indeks = j
        Milik_Andi[i], Milik_Andi[min_indeks] = Milik_Andi[min_indeks], Milik_Andi[i]

Milik_Andi = [9, 5, 3, 8, 2]
selection_sort(Milik_Andi)
print("Daftar angka yang diurutkan:")
for DaftarAngka in Milik_Andi:
    print(DaftarAngka)