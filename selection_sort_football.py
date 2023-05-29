#Amanda Rismawati
#10109005
#LATIHAN 5 : Mengurutkan daftar pemain sesuai dengan jumlah gol yang dicetak menggunakan selection sort descending

def selection_sort(NamaPemain):
    n = len(NamaPemain)
    for i in range(n):
        max_indeks = i
        for j in range(i+1, n):
            if NamaPemain[j]["CetakGol"] > NamaPemain[max_indeks]["CetakGol"]:
                max_indeks = j
        NamaPemain[i], NamaPemain[max_indeks] = NamaPemain[max_indeks], NamaPemain[i]

NamaPemain = [
    {"Nama": "Kylian Mbappe", "Klub": "Paris Saint-Germain", "CetakGol": 40},
    {"Nama": "Victor Osimhen", "Klub": "Napoli", "CetakGol": 28},
    {"Nama": "Robert Lewandowski", "Klub": "Barcelona", "CetakGol": 33},
    {"Nama": "Erling Haaland", "Klub": "Manchester City", "CetakGol": 52},
    {"Nama": "Christopher Nkunku", "Klub": "RB Leipzig", "CetakGol": 22}
]

selection_sort(NamaPemain)
print("Hasil Pengurutan daftar Pemain berdasarkan Jumlah Gol yang di cetak :" )
print(" ")
for pemain in NamaPemain:
    print("Nama Pemain:", pemain["Nama"])
    print("Klub Pemain:", pemain["Klub"])
    print("Jumlah Gol:", pemain["CetakGol"])
    print("-------------------------------")


