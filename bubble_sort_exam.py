#Amanda Rismawati
#10109005
#LATIHAN 1 : Mengurutkan daftar nilai 

def bubble_sort(DaftarNilai):
    n = len(DaftarNilai)
    for i in range(n-1):
        for j in range(n - i - 1):
            if DaftarNilai[j] > DaftarNilai[j+1]:
                DaftarNilai[j], DaftarNilai[j+1] = DaftarNilai[j+1], DaftarNilai[j]


DaftarNilai = [78, 65, 90, 82, 70]
bubble_sort(DaftarNilai)
print("Hasil pengurutan daftar nilai siswa secara ascending : ", DaftarNilai)
