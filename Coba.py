# Buat coba2 aja biar langsung run file ini & ga muter2 lewatin program utama

from CRUD import Operasi
from CRUD import Database
import time

def read():
    try:
        # data string di file.txt dibaca jadi list yg tiap isi listnya dipisah sama garis baru (\n)
        with open("data.txt", "r") as file:
            daftar_buku = file.readlines()
            return daftar_buku
    except:
        # bikin data baru yg kosong (Kalo gagal read kemungkinan ga ada filenya)
        with open("data.txt", "w", encoding="utf-8") as file:
            file.write("")
            return []   # return list kosong, persis kayak file.readlines() tapi isi filenya kosong

# print(read())


def bikin_kunci_primer():
    daftar_buku = len(read()) + 1
    nomor = str(daftar_buku).zfill(4)
    kode = "BUKU"
    kunci_primer = kode + nomor
    
    return kunci_primer


def isi_body(daftar_buku):
    tipe_data = daftar_buku.type()

    return print(f"Tipe data: {tipe_data}")


# tampil_daftar_buku = Operasi.read(index=1)
# # tampil_daftar_buku = Operasi.read()
# print(f"Tampil Daftar Buku: {tampil_daftar_buku}")
# # isi_body(tampil_daftar_buku)


"""
Ini cara update yg di tutorialnya.
Cara delete di tutorialnya jg beda sama yg saya.

Saya nulis banyak komen di kodenya biar sekalian pahamin kodenya
sampe akhirnya nemu cara lain buat update sama delete.
Soalnya yg di tutorial, isi file.txt di judul & penulis jadi banyak
spasi sampe total karakter judul & penulis jumlahnya 255.
contoh yg di tutorial:
yNOJlG,17-09-2024,Menangkap Capung                                                                                                                                                                                                                                               ,Ucup Surucup                                                                                                                                                                                                                                                   ,1999
NScepG,17-09-2024,Menangkap dan Melatih Jangkrik                                                                                                                                                                                                                                 ,Otong Surotong                                                                                                                                                                                                                                                 ,1998

Kalo file.txt saya isinya normal, ga ada spasi banyak gitu
contoh yang saya:
QOkEZf,18-09-2024,Menangkap Capung,Ucup Surucup,1998
SNGhbc,18-09-2024,Menangkap dan Melatih Jangkrik,Otong Surotong,1989
"""
def update(nomor_buku, pk, tgl_ditambahkan, judul, penulis, tahun):
    data = Database.TEMPLATE_DATA.copy()

    data["pk"] = pk
    data["tgl_ditambahkan"] = tgl_ditambahkan
    data["judul"] = judul + Database.TEMPLATE_DATA["judul"][len(judul):]
    data["penulis"] = penulis + Database.TEMPLATE_DATA["penulis"][len(penulis):]
    data["tahun"] = str(tahun)

    # Data input user yg asalnya dictionary, digabungin jadi data string tanpa dictionary key-nya
    # tiap data string yg masuk ini jadi satu list di databasenya file.txt nya
    data_buku = f'{data["pk"]},{data["tgl_ditambahkan"]},{data["judul"]},{data["penulis"]},{data["tahun"]}\n'
    panjang_data = len(data_buku)
    cari = panjang_data * (nomor_buku - 1)

    try:
        with open(Database.DB_NAME, "r+", encoding="utf-8") as file:
            # print(f"(operasi.py) data_buku: {data_buku}")
            # print(f"(operasi.py) cari: {cari}")
            # print(f"(operasi.py) panjang_data: {panjang_data}")

            # kode seek di bawah nganggep garis baru di file.txt jadi "\n" gitu?
            # "\n" itu 2 karakter. Kalo garis baru / enter itu 1 karakter
            # Makanya harus tambah (nomor_buku - 1) di akhir kodenya
            # Atau gimana ya? Pokoknya kode ini berhasil
            file.seek(cari + (nomor_buku - 1))  # memilih data yg mau diubah
            file.write(data_buku)   # Data yg dipilih lalu diubah
        
        return print("Data berhasil diubah")
    except:
        return print("Data gagal diubah")

"""
data["judul"] = judul + Database.TEMPLATE_DATA["judul"][len(judul):]
titik dua di akhir biar otomatis nambahin spasi sisanya sampe
jumlahnya sesuai template.
Tapi ini ga jadi dipake, update sama delete saya pake cara yg lebih simpel

Penjelasan lanjut kenapa ada titik dua di akhir [len(judul):]
https://stackoverflow.com/questions/4012340/colon-in-python-list-index
"""

# Nyoba cari alesan kenapa method seek kayak gitu
# tapi pusing ga nemu jawabannya
print("\n" + 30*"=")
print("Kenapa seek kayak gini?")
with open("data.txt", "r+", encoding="utf-8") as file:
    file.seek(1605 - 3)
    print(file.read())
    # file.write(data_buku)



"""
Hati hati, pas dirun bakal langsung ngehapus data
"""
print("\n" + 30*"=")
print("coba hapus")
with open("data.txt", "r", encoding="utf-8") as file:
    data = file.readlines()
    data.pop(3)

data_buku = "".join(data)

with open("data.txt", "w", encoding="utf-8") as file:
    file.write(str(data_buku))
