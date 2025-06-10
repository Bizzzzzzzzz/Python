from .pemilih import listPemilih
from .calon import listCalon

def lakukan_voting():
    idPemilih = input("Masukan ID Pemilih: ")
    for i in listPemilih:
        if i["id"] == idPemilih:
            if i["sudah_memilih"] == True:
                print("Pemilih sudah Memilih")
                return
            else:
                idCalon = input("Masukan ID Calon: ")
                for j in listCalon:
                    if j["id"] == idCalon:
                        j["jumlah_suara"] += 1
                        i["sudah_memilih"] = True
                        print("suara telah di input")
                        return
                    else:
                        print("Id calon tidak valid")
                        return
        else:
            print("id Pemilih tidak valid")
            return

def tampilkan_hasil():
    for i in listCalon:
        print(i)