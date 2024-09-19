# Kebutuhan awal setup database

from . import Operasi

DB_NAME = "data.txt"
TEMPLATE_DATA = {
    "pk": "XXXXXX",     # primary key, ada di setiap table database & key-nya unik (ga ada yg sama)
    "tgl_ditambahkan": "dd-mm-yyyy",
    "judul": 255*" ",
    "penulis": 255*" ",
    "tahun": "yyyy",
}
# Templatenya ga kapake buat database berupa file.txt
# Soalnya pas masuk file.txt juga jadinya string
# Pas dipanggil pake open juga jadinya list,
# bukan dictionary kayak template di atas
# Mungkin template kepakenya kalo pake database asli ya?

def init_console():
    try:
        with open(DB_NAME, "r") as file:
            daftar_buku = file.readlines()
            if daftar_buku == []:
                print("Isi Database kosong, silahkan isi data baru:")
                Operasi.bikin_data("w")
            else:
                return None 

    except:
        print("\n" + 102*"=")
        print("Database tidak tersedia. Silahkan membuat database baru")
        Operasi.bikin_data("w")