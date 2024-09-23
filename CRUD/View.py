# Interface lanjutan dari interface utama di main.py

from . import Operasi
from . import Utilitas
import time

# jika tanpa agrumen, nampilin semua buku
# jika ada argumen index, nampilin satu buku sesuai index
# jumlah_buku yg diterima dari Utilitas.isi_body() direturn ke View.update_console()
def read_console(**kwargs):
    # Header
    print("\n" + 102*"=")
    print(f"| {"No. ":^4} | {"Judul":40} | {"Penulis":40} | {"Tahun":5} |")
    print(102*"-")
    
    # Body
    if "index" in kwargs:
        Utilitas.isi_body(index=kwargs["index"])
        jumlah_buku = 1
    else:
        jumlah_buku = Utilitas.isi_body()   # nampilin daftar buku sekalian nyimpen hasil return ke variable

    # Footer
    print(102*"=")

    return jumlah_buku

# Interface untuk menambah data baru
def create_console():
    print("\n" + 102*"=")
    print("Silahkan masukan data buku")
    print(f"{'! Masukan 0 untuk batal !':^26}")
    print(f"{'- - - -':^26}")
    status = Operasi.create("a")
    if status == True:
        read_console()
        print("Data berhasil ditambahkan")
    elif status == False:
        read_console()
        print("Data gagal ditambahkan")
    else:
        print("Batal menambahkan data")
        return None

# Interface untuk mengubah data
def update_console():
    # nampilin semua buku buat user pilih
    nomor_buku = Utilitas.pilih_buku("ubah")
    if nomor_buku == None:
        print("Batal mengubah data")
        return None
    else:
        data_buku = Operasi.read(index=nomor_buku)

    # print (f" (view.py) nomor_buku: {nomor_buku}")
    # print (f" (view.py) data_buku: {data_buku}")

    # data buku yg user pilih berupa string lalu diubah jadi tuples 
    data_buku_tuples = Utilitas.split_data_buku(data_buku)
    pk = data_buku_tuples[0]
    tgl_ditambahkan = data_buku_tuples[1]
    judul = data_buku_tuples[2]
    penulis = data_buku_tuples[3]
    tahun = data_buku_tuples[4]

    # Interface saat proses pengubahan data
    # Di interface data sudah berubah tapi di file.txt belum
    # Data di file.txt baru keubah jika user memilih pilihan nomor 5
    while True:
        print(102*"=" + "\n")
        # print(f"Nomor buku yg akan diubah: {nomor_buku}")
        print("Apa yang ingin diubah:")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun terbit\t: {tahun}")
        print("4. Batal")
        print("5. Selesai Mengubah")
        pilihan_ubah = input("Pilih (1/2/3/4/5): ")

        match pilihan_ubah:
            case "1": judul = input("judul\t: ")
            case "2": penulis = input("penulis\t: ")
            case "3": tahun = Utilitas.validasi_tahun()
            case "4": return None
            case "5":
                Operasi.update(nomor_buku, pk, tgl_ditambahkan, judul, penulis, tahun)
                break
            case _:
                print("Pilihan tidak tersedia")
                time.sleep(1)


def delete_console():
    # nampilin semua buku buat user pilih
    nomor_buku = Utilitas.pilih_buku("hapus")
    if nomor_buku == None:
        print("Batal menghapus data")
        return None
    else:
        read_console(index=nomor_buku)
        
    while True:
        pilihan_hapus = input("Yakin menghapus data ini (y/n)? ")
        
        match pilihan_hapus:
            case "y" | "Y": 
                Operasi.delete(nomor_buku)
                break
            case "n" | "N": return print("Data batal dihapus")
            case _: 
                print("Pilihan tidak tersedia")
                time.sleep(1)