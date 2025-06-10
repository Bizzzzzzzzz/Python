from .pemilih import listPemilih
from .calon import listCalon

def tampilkan_statistik():
    totalPemilih = 0
    totalPemilihValid = 0
    for i in listPemilih:
        totalPemilih += 1
    for i in listPemilih:
        if i["sudah_memilih"] == True:
            totalPemilihValid +=1
    pemenang = max(listCalon, key=lambda x: x["jumlah_suara"])
    persentasePemilih = totalPemilihValid / totalPemilih
    persentasePemilih = persentasePemilih * 100
    print(f"total pemilih adalah {totalPemilih} peserta")
    print(f"total pemilih yang sudah memilih adalah {totalPemilihValid} peserta")
    print(f"dari data tersebut, jumlah persentase pemilih adalah {persentasePemilih}%")
    print(f"calon dengan suara terbanyak adalah {pemenang}")