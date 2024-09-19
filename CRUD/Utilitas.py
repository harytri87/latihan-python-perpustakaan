# Operasi - operasi sampingan

from . import Operasi
from . import View
import random
import string
import time

# Bikin primary key random
def random_string(panjang):
    hasil_random = "".join(random.choice(string.ascii_letters) for i in range(panjang))
    return hasil_random
    
# Bikin primary key custom
def bikin_kunci_primer():
    daftar_buku = len(Operasi.read()) + 1
    nomor = str(daftar_buku).zfill(4)
    kode = "BUKU"
    kunci_primer = kode + nomor
    
    return kunci_primer

# Buat validasi tahun dari input user
def validasi_tahun():
    tahun_skrg = int(time.strftime("%Y", time.localtime()))

    while True:
        try:
            tahun = int(input("Tahun: "))
            if tahun >= 1300 and tahun <= tahun_skrg:
                break
            elif tahun == 0:
                return "batal"  # ini bisa False atau string, bebas
            else:
                print("Tidak dapat memasukkan tahun tersebut")
        except:
            print("Tahun hanya dapat diisi empat angka")
    
    return tahun

# Data buku yg asalnya string panjang displit jadi tuples
def split_data_buku(data):
    data_break = data.split(",")
    pk = data_break[0]
    tgl_ditambahkan = data_break[1]
    judul = data_break[2]
    penulis = data_break[3]
    # tahun = data_break[4][:-1]                  # ga termasuk 1 karakter di paling akhir
    tahun = data_break[4].replace("\n", "")   # ngilangin \n di akhir
                                                        # hasilnya sama aja, beda cara doang
    return pk, tgl_ditambahkan, judul, penulis, tahun


# Bikin isi body daftar buku
def isi_body(**kwargs):
    if "index" in kwargs:
        tampil_daftar_buku = Operasi.read(index=kwargs["index"])
        data_buku = split_data_buku(tampil_daftar_buku)
        
        print(f"| {kwargs["index"]:^4} | {data_buku[2]:40} | {data_buku[3]:40} | {data_buku[4]:^5} |")
    
        return kwargs["index"]

    else:
        tampil_daftar_buku = Operasi.read()     # manggil semua buku
        jumlah_buku = len(tampil_daftar_buku)

        for index, data in enumerate(tampil_daftar_buku, 1): # enumerate buat nampilin nomor tanpa kode
            # tampil_daftar_buku itu data bukunya (key, judul, penulis, dll)
            # masih dianggap jadi 1 data string yg panjang:
            # ["key1, date_add1, judul1, penulis1, tahun1\n", "key2, date_add2, judul2, penulis2, tahun2\n"]    <- tampil_daftar_buku = [contoh isinya 2 list disamping]

            # Terus sama perulangan dipisahin data antar bukunya.
            # Tapi tetep masih data string yg panjang:
            # "key1, date_add1, judul1, penulis1, tahun1\n"     <- masih sama cuma dipisah dari list tampil_daftar_buku
            # "key2, date_add2, judul2, penulis2, tahun2\n"

            data_buku = split_data_buku(data)
            # Nah kalo data_buku ini ngebikin string data buku di atas jadi list:
            # ["key1", "judul1", "penulis1", "tahun1"]      <- buku_satu = [isi listnya kayak disamping]
            # ["key2", "judul2", "penulis2", "tahun2"]      <- buku_dua = [isi listnya kayak disamping]

            # Perhatiin penempatan tanda kurung kotak sama tanda kutipnya beda
            # antara di tampil_daftar_buku, data sama data_break
            # Catatan: kurung kotak artinya list. Tanda kutip artinya data string

            print(f"| {index:^4} | {data_buku[2]:40} | {data_buku[3]:40} | {data_buku[4]:^5} |")

        return jumlah_buku
    
def pilih_buku(mode):
    jumlah_buku = View.read_console()    # nampilin daftar buku sekalian nyimpen hasil return ke variable
    while True:
        try:
            print(f"{'- -':^36}")
            print("Masukan 0 untuk batal.")
            nomor_buku = int(input(f"Pilih nomor buku yang ingin di{mode}: "))
            match nomor_buku:
                case _ as nomor if nomor > 0 and nomor <= jumlah_buku:
                    break
                case 0: return None
                case _: print("Buku tidak tersedia.")
        except:
            print("Masukan nomor buku.")
    
    return nomor_buku

"""
Maaf komennya panjang. Itu kode di dalem for cuma 2 baris, sisanya banyak komen.
Komen itu cara saya ngejelasin ulang kodenya pas lagi belajar biar saya bener2
paham kodenya. Sama kalo kedepannya butuh referensi dari sini, ingetan saya bisa
kerefresh dari bacain komennya
"""