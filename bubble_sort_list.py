#Amanda Rismawati
#1010905
#LATIHAN : Mengurutkan daftar angka secara descending Bubble Sort

def bubble_sort(DaftarAngka): 
    n = len(DaftarAngka)
    for i in range(n-1):
        for j in range(n-i-1):
            if DaftarAngka[j] < DaftarAngka[j+1]:
               DaftarAngka[j], DaftarAngka[j+1] = DaftarAngka[j+1], DaftarAngka[j]
                
DaftarAngka = [42, 19, 33, 8, 55]
bubble_sort(DaftarAngka)
print("Hasil pengurutan : ", DaftarAngka)