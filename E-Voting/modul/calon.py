listCalon = []

def tambah_calon():
    idCalon = input("Masukan ID Calon: ")
    if any(i["id"] == idCalon for i in listCalon):
        print("ID sudah Terdaftar")
        return
    namaCalon = input("Masukan Nama Calon: ")
    visiCalon = input("Masukan Visi Calon: ")
    listCalon.append({"id": idCalon, "nama": namaCalon, "visi": visiCalon, "jumlah_suara": 0})
    print("Calon Telah di Daftarkan")