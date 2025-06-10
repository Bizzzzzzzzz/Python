listPemilih = []

def tambah_pemilih():
    idPemilih = input("Masukan ID Pemilih: ")
    if any(i["id"] == idPemilih for i in listPemilih):
        print("ID sudah Terdaftar")
        return
    namaPemilih = input("Masukan Nama Pemilih: ")
    jurusanPemilih = input("Masukan Jurusan Pemilih: ")
    listPemilih.append({"id": idPemilih, "nama": namaPemilih, "jurusan": jurusanPemilih, "sudah_memilih": False})
    print("Pemilih Telah di Daftarkan")
    print(listPemilih)