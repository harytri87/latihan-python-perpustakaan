# Operasi-operasi yang berinteraksi dengan database (data.txt)

from . import Database
from .Utilitas import random_string, bikin_kunci_primer, validasi_tahun
import time

# Bikin data baru
def bikin_data(MODE):               # mode "w" write atau "a" append
    judul = input("Judul: ")
    match judul:
        case "0": return "batal"
    penulis = input("Penulis: ")
    match penulis:
        case "0": return "batal"
    tahun = validasi_tahun()
    match tahun:
        case "batal": return "batal"

    pk = random_string(6)        # random string
    # pk = bikin_kunci_primer()   # bikin kode sendiri
    # tgl_ditambahkan = time.strftime("%d-%m-%Y %H:%M:%S (GMT%z)", time.localtime())
    # tgl_ditambahkan = time.strftime("%d-%m-%Y-%H-%M-%S-%z", time.localtime())
    tgl_ditambahkan = time.strftime("%d-%m-%Y", time.localtime())
    tahun = str(tahun)

    # Data input user yg asalnya dictionary, digabungin jadi data string tanpa dictionary key-nya
    # tiap data string yg masuk ini jadi satu list di databasenya file.txt nya
    data_buku = f'{pk},{tgl_ditambahkan},{judul},{penulis},{tahun}\n'
    try:
        with open(Database.DB_NAME, MODE, encoding="utf-8") as file:
            file.write(data_buku)
        return True
    except:
        return False


# Ngambil satu atau semua data buku
def read(**kwargs):
    try:
        # data string di file.txt dibaca jadi list yg tiap isi listnya dipisah sama garis baru (\n)
        with open(Database.DB_NAME, "r") as file:
            daftar_buku = file.readlines()
            jumlah_buku = len(daftar_buku)

            if "index" in kwargs:
                index_buku = int(kwargs["index"]) - 1

                # Bebas mau pake match atau if. Mungkin match buat input user aja ya
                # Kalo variable biasa pake if
                # match index_buku:
                #     case _ as status if status >= 0 and status < jumlah_buku: return daftar_buku[index_buku]
                #     case _: return False

                if index_buku >= 0 and index_buku < jumlah_buku:
                    return daftar_buku[index_buku]
                    # return data satu buku berupa string
                else:
                    return False
            else:
                return daftar_buku
                # return semua data buku berupa list yg isinya masing-masing data buku berupa string
    except:
        # bikin data baru yg kosong buat kebutuhan init database
        # (Soalnya kalo gagal read kemungkinan ga ada filenya)
        with open("data.txt", "w", encoding="utf-8") as file:
            file.write("")
            return []   # return list kosong, persis kayak file.readlines() tapi isi filenya kosong


# Mengubah data sesuai index
def update(nomor_buku, pk, tgl_ditambahkan, judul, penulis, tahun):
    data_buku = f"{pk},{tgl_ditambahkan},{judul},{penulis},{tahun}\n"

    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            data = file.readlines()             # ngambil semua data jadiin list di variable baru
            data[nomor_buku - 1] = data_buku    # ngubah isi list sesuai index
            data_buku = "".join(data)           # list diubah jadi full string

            # Contoh cara debug saya. Kurang tau bener ga cara debugnya
            #         (namaFile namaMethod) apa yg mau dites
            # print(f"(operasi.py update) data: {data}")
            # print(f"(operasi.py update) data[nomor_buku - 1]: {data[nomor_buku - 1]}")
            # print(f"(operasi.py update) data_buku: {data_buku}")
    except:
        return print("(operasi.py update) Data tidak ditemukan")
    
    try:
        with open("data.txt", "w", encoding="utf-8") as file:
            file.write(str(data_buku))          # semua isi file.txt diubah/overwrite sama data_buku yg di atas
            return print("(operasi.py update) Data berhasil diubah")
    except:
        return print("(operasi.py update) Data gagal diubah")


# Menghapus data sesuai index
# Prosesnya sama kayak update, beda 1 baris kode sama tulisan di printnya
def delete(nomor_buku):
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            data = file.readlines()
            data.pop(nomor_buku - 1)    # ini yg beda sama update
            data_buku = "".join(data)
    except:
        return print("(operasi.py delete) Data tidak ditemukan")

    try:
        with open("data.txt", "w", encoding="utf-8") as file:
            file.write(str(data_buku))
            return print("Data berhasil dihapus")
    except:
        return print("(operasi.py delete) Data gagal dihapus")