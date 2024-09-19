# Latihan Projek Bikin Program Perpustakaan
# Pastiin terminalnya udah di folder ini sebelum run

# Program utama / interface utama yg muncul ke pengguna

import os
import time
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name

    while True:
        match sistem_operasi:                   # pengecekan, mana yg cocok
            case "posix": os.system("clear")    # linux, mac
            case "nt":  os.system("cls")        # windows

        print("SELAMAT DATANG DI PROGRAM")
        print(f"{"DATABASE PERPUSTAKAAN":^25}")
        print(25 * "=") 

        # Mengecek ada/tidak ada database
        CRUD.init_console()     # ini masuk ke CRUD\__init__.py

        print("\n1. Lihat Daftar Buku")
        print("2. Tambahkan Daftar Buku")
        print("3. Ubah Data Buku")
        print("4. Hapus Data Buku")
        print("5. Keluar")

        pilihan = input("Pilih (1/2/3/4/5): ")

        match pilihan:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()
            case "5": break
            case _: 
                print("Masukan angka 1-5")
                time.sleep(1)
                continue

        print(f"{'- - - - -':^39}")
        is_done = input("Apakah ingin memakai fitur lain (y/n)? ")
        match is_done:
            case "n" | "N": break
            case "y" | "Y": continue
            case _:
                print("Input salah")
                break

    print("Program ditutup. Terima kasih.")