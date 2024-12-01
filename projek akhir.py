import pandas as pd
import csv
import os 
import datetime as dt

list_jenisproduk = {
   1:"Alat Tanam dan Persiapan Lahan",
   2:"Alat Pemeliharaan Tanaman",
   3:"Alat Panen dan Pascapanen",
   4:"Alat Pupuk dan Benih",
   5:"Obat dan Perawatan Tanaman",
   6:"Pencarian",
   7:"Kembali"
}
list_jenisproduk1 = {
    "1": ("Cangkul", 50000),
    "2": ("Sekop", 40000),
    "3": ("Garpu Tanah", 30000),
    "4": ("Penugal Tanam Manual", 30000),
    "5": ("Ember Plastik", 15000)
}
list_jenisproduk2 = {
    "1": ("Gembor", 45000),
    "2": ("Gunting Dahan", 60000),
    "3": ("Sprayer Manual", 70000),
    "4": ("Pemangkas Tunas Kecil", 40000),
    "5": ("Alat Pencabut Rumput", 35000)
} 
list_jenisproduk3 = {
    "1": ("Sabit", 50000),
    "2": ("Pisau Panen", 25000),
    "3": ("Keranjang Panen Plastik", 30000),
    "4": ("Timbangan Digital", 150000),
    "5": ("Kantong Plastik Panen (10 pcs)", 30000)
}
list_jenisproduk4 = {
    "1": ("Pupuk Organik", 35000),
    "2": ("Pupuk Urea", 100000),
    "3": ("Benih Sayuran (1 paket)", 20000),
    "4": ("Cocopeat", 25000),
    "5": ("Kapur Dolomit", 20000)
}
list_jenisproduk5 = {
    "1": ("Pestisida Organik", 50000),
    "2": ("Fungisida Cair", 70000),
    "3": ("Insektisida", 65000),
    "4": ("Herbisida", 80000),
    "5": ("ZPT (Zat Pengatur Tumbuh)", 90000)
}

def home():
    os.system('cls')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("$$$$$$$$$^^^^^  SELAMAT DATANG di TRIJAYA  ^^^^^$$$$$$$$")
    print('''
          1. Register
          2. Login
          3. Admin
           ''')
    home = input("Pilih fitur : ")
    if home == "1":
        register()
    elif home == "2":
        login()
    elif home == "3":
        login_admin()
    else:
        print ("Pilihan tidak tersedia")

def register():
    os.system('cls')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("$$$$$$$$$^^^^^  SELAMAT DATANG di TRIJAYA  ^^^^^$$$$$$$$")
    print("______________________  REGISTER  ______________________")
    username = input("Masukkan username anda: ").strip()
    password = input("Masukkan password anda: ").strip()
    
    file_exists = os.path.isfile('RegTRIJAYA.csv')

    with open('RegTRIJAYA.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:  
            writer.writerow(["username","password"])
        writer.writerow([username,password])
        print("________________________")
        print("Akun telah didaftarkan!!")
        print("________________________")
        print("1.Login")
        print("2.Selesai")
        otw_login = input ("pilihlah angka untuk selanjutnya (1/2) :")
        if otw_login == '2':
            print("=-=-=-=-=-=- Pendaftaran selesai! -=-=-=-=-=-=")
            input("klik enter untuk login")
        elif otw_login == '1':
            login()
        else:
            print("input tidak tersedia")

def login():
    os.system('cls')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("$$$$$$$$$^^^^^  SELAMAT DATANG di TRIJAYA  ^^^^^$$$$$$$$")
    print("________________________ LOGIN _________________________")

    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()

    if not os.path.isfile('RegTRIJAYA.csv'): 
        print("Akun tidak terdaftar. Silakan daftar terlebih dahulu!.")
        return None

    with open('RegTRIJAYA.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                print(f"Selamat datang, {username}!")
                jenis_produk(username)
                return username
        print("Login gagal! Username atau password salah.")
        return None
def login_admin():
    os.system('cls')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("$$$$$$$$$^^^^^  SELAMAT DATANG di TRIJAYA  ^^^^^$$$$$$$$")
    print("________________________ LOGIN _________________________")

    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()

    if not os.path.isfile('admin.csv'): 
        print("Akun tidak terdaftar. Silakan daftar terlebih dahulu!.")
        return None

    with open('admin.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                print(f"Selamat datang, {username}!")
                jenis_produk(username)
                return username
        print("Login gagal! Username atau password salah.")
        return None
             


def jenis_produk(username):
    os.system('cls')
    print(f"Selamat datang, silahkan pilih jenis produk : ")
    for i in list_jenisproduk:
        print(i,".",list_jenisproduk[i])
    jenis = input("Pilihlah jenis produk (1/2/3/4/5/6): ")
    if jenis == '1':
            os.system('cls')
            print('''
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            $$$$$$$$$^^^^^  Alat Persiapan Lahan  ^^^^^$$$$$$$$
            __________________ SELAMAT BERBELANJA ___________________
            ''')
            for i in list_jenisproduk1:
                nama_produk, harga_produk = list_jenisproduk1[i]
                print(f"{i}. {nama_produk} - Rp{harga_produk}")
            
            pilih_produk1 = input("Pilih produk (1-5): ").strip()
            
            if pilih_produk1 == "1":
                produk = "Gembor"
                print("\nDetail Produk: ")
                print('''
                Deskripsi Produk: Penyiram tanaman dengan desain tradisional
                Spesifikasi: Material -> Plastik tahan UV, Kapasitas -> 5 liter
                Harga: Rp 45.000''')
            elif pilih_produk1 == "2":
                produk = "Gunting Dahan"
                print("\nDetail Produk: ")
                print('''
                Deskripsi Produk: Gunting kuat untuk memotong dahan dengan mudah
                Spesifikasi: Material -> Baja karbon, Pegangan -> Anti slip
                Harga: Rp 60.000''')
            elif pilih_produk1 == "3":
                produk = "Sprayer Manual"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Alat penyemprot untuk pestisida atau pupuk cair
                Spesifikasi: Kapasitas -> 2 liter, Material -> Plastik tebal
                Harga: Rp 70.000''')
            elif pilih_produk1 == "4":
                produk = "Pemangkas Tunas Kecil"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Pemotong presisi untuk merapikan tunas kecil
                Spesifikasi: Material -> Baja stainless, Panjang -> 20 cm
                Harga: Rp 40.000''')
            elif pilih_produk1 == "5":
                produk = "Alat Pencabut Rumput"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Memudahkan mencabut rumput tanpa merusak tanaman
                Spesifikasi: Material -> Baja, Pegangan -> Kayu ergonomis
                Harga: Rp 35.000''')
            if pilih_produk1 in list_jenisproduk1:
                produk, harga = list_jenisproduk1[pilih_produk1]
                print(f"\n{produk} dengan harga Rp{harga} adalah produk yang dipilih oleh {username}")
                print('''
                A. Masukkan keranjang
                B. Beli dan bayar
                ''')
                keranjang_beli = input("Pilih menu: ").strip().upper()
                if keranjang_beli == "A":
                    keranjang(username, produk, harga)
                elif keranjang_beli == "B":
                    keranjang(username, produk, harga)
                    pembayaran(username)
                else:
                    print("Pilihan tidak tersedia. Kembali ke menu.")
                    jenis_produk(username)
            else:
                print("Pilihan tidak tersedia!")
                input("Tekan Enter untuk kembali.")
                jenis_produk(username)
                
    elif jenis == '2':
            os.system('cls')
            print('''
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            $$$$$$$$$^^^^^  Alat Pemeliharaan Tanaman  ^^^^^$$$$$$$$
            __________________ SELAMAT BERBELANJA ___________________
            ''')
            for i in list_jenisproduk2:
                nama_produk, harga_produk = list_jenisproduk2[i]
                print(f"{i}. {nama_produk} - Rp{harga_produk}")
            
            pilih_produk2 = input("Pilih produk (1-5): ").strip()
            
            if pilih_produk2 == "1":
                produk = "Gembor"
                print("\nDetail Produk: ")
                print('''
                Deskripsi Produk: Penyiram tanaman dengan desain tradisional
                Spesifikasi: Material -> Plastik tahan UV, Kapasitas -> 5 liter
                Harga: Rp 45.000''')
            elif pilih_produk2 == "2":
                produk = "Gunting Dahan"
                print("\nDetail Produk: ")
                print('''
                Deskripsi Produk: Gunting kuat untuk memotong dahan dengan mudah
                Spesifikasi: Material -> Baja karbon, Pegangan -> Anti slip
                Harga: Rp 60.000''')
            elif pilih_produk2 == "3":
                produk = "Sprayer Manual"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Alat penyemprot untuk pestisida atau pupuk cair
                Spesifikasi: Kapasitas -> 2 liter, Material -> Plastik tebal
                Harga: Rp 70.000''')
            elif pilih_produk2 == "4":
                produk = "Pemangkas Tunas Kecil"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Pemotong presisi untuk merapikan tunas kecil
                Spesifikasi: Material -> Baja stainless, Panjang -> 20 cm
                Harga: Rp 40.000''')
            elif pilih_produk2 == "5":
                produk = "Alat Pencabut Rumput"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Memudahkan mencabut rumput tanpa merusak tanaman
                Spesifikasi: Material -> Baja, Pegangan -> Kayu ergonomis
                Harga: Rp 35.000''')
            if pilih_produk2 in list_jenisproduk2:
                produk, harga = list_jenisproduk2[pilih_produk2]
                print(f"\n{produk} dengan harga Rp{harga} adalah produk yang dipilih oleh {username}")
                print('''
                A. Masukkan keranjang
                B. Beli dan bayar
                ''')
                keranjang_beli = input("Pilih menu: ").strip().upper()
                if keranjang_beli == "A":
                    keranjang(username, produk, harga)
                elif keranjang_beli == "B":
                    keranjang(username, produk, harga)
                    pembayaran(username)
                else:
                    print("Pilihan tidak tersedia. Kembali ke menu.")
                    jenis_produk(username)
            else:
                print("Pilihan tidak tersedia!")
                input("Tekan Enter untuk kembali.")
                jenis_produk(username)
    elif jenis == '3':
            os.system('cls')
            print('''
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            $$$$$$$$$^^^^^  Obat dan Perawatan Tanaman  ^^^^^$$$$$$$$
            __________________ SELAMAT BERBELANJA ___________________
            ''')
            for i in list_jenisproduk3:
                nama_produk, harga_produk = list_jenisproduk3[i]
                print(f"{i}. {nama_produk} - Rp{harga_produk}")
            
            pilih_produk3 = input("Pilih produk (1-5): ").strip()
            
            for i in list_jenisproduk3:
                print(i,".",list_jenisproduk3[i])
            pilih_produk3 = input("pilih produk: ")
            produk = ""
        
            if pilih_produk3 == "1":
                produk = "Sabit"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Alat panen tradisional dengan bilah tajam
                Spesifikasi: Material -> Baja karbon, Pegangan -> Kayu solid
                Harga: Rp 50.000''')
            elif pilih_produk3 == "2":
                produk = "Pisau Panen"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Pisau kecil untuk memotong buah atau tanaman kecil
                Spesifikasi: Material -> Baja, Pegangan -> Plastik ergonomis
                Harga: Rp 25.000''')
            elif pilih_produk3 == "3":
                produk = "Keranjang Panen Plastik"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Keranjang ringan dan tahan lama untuk hasil panen
                Spesifikasi: Material -> Plastik tebal, Kapasitas -> 20 liter
                Harga: Rp 30.000''')
            elif pilih_produk3 == "4":
                produk = "Timbangan Digital"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Timbangan presisi tinggi untuk hasil panen
                Spesifikasi: Kapasitas -> 30 kg, Layar -> Digital LED
                Harga: Rp 150.000''')
            elif pilih_produk3 == "5":
                produk = "Kantong Plastik Panen"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Paket plastik untuk membungku hasil
                Spesifikasi: Material -> plastik berkualitas, Layar -> Digital LED
                Harga: Rp 30.000''')

            if pilih_produk3 in list_jenisproduk3:
                produk, harga = list_jenisproduk3[pilih_produk3]
                print(f"\n{produk} dengan harga Rp{harga} adalah produk yang dipilih oleh {username}")
                print('''
                A. Masukkan keranjang
                B. Beli dan bayar
                ''')
                keranjang_beli = input("Pilih menu: ").strip().upper()
                if keranjang_beli == "A":
                    keranjang(username, produk, harga)
                elif keranjang_beli == "B":
                    keranjang(username, produk, harga)
                    pembayaran(username)
                else:
                    print("Pilihan tidak tersedia. Kembali ke menu.")
                    jenis_produk(username)
            else:
                print("Pilihan tidak tersedia!")
                input("Tekan Enter untuk kembali.")
                jenis_produk(username)
           
    elif jenis == "6":
         os.system('cls')
         search = input(f"Silahkan ketik barang yang anda cari :")
         if search == "Cangkul" or search == "Ember" :
                print('''
                =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                $$$$$$$$$^^^^^  Alat Pemeliharaan Tanaman ^^^^^$$$$$$$$
                __________________ SELAMAT BERBELANJA ___________________
                ''')
                for i in list_jenisproduk2:
                    print(i,".",list_jenisproduk2[i])
                pilih_produk2 = input("pilih produk: ")
                produk = ""
            
                if pilih_produk2 == "1":
                    produk = "Cangkul"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Alat tanam serbaguna dari baja yang tahan lama.
                    Spesifikasi: Material: Baja tahan karat, Pegangan: Kayu ergonomis,
                    Harga: Rp 50.000
                    ''')
                elif pilih_produk2 == "2":
                    produk = "Sekop"
                    print("\nDetail Produk: ")
                    print('''
                     Deskripsi: Alat berbahan ringan dengan pegangan ergonomis.
                     Spesifikasi: Material: Baja ringan, Pegangan: Plastik anti selip,
                     Harga: Rp 40.000
                     ''')
                elif pilih_produk2 == "3":
                    produk = "Garpu Tanah"
                    print("\nDetail Produk: ")
                    print('''
                     Deskripsi: Alat tajam dan kuat untuk melonggarkan tanah.
                     Spesifikasi: Material: Baja, Pegangan: Kayu solid, Dimensi: 25 cm,
                     Harga: "Rp 30.000"
                     ''')
                elif pilih_produk2 == "4":
                    produk = "Penugal Tanam Manual"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Alat sederhana untuk membuat lubang tanam.
                    Spesifikasi: Material: Logam tahan karat, Panjang: 30 cm,
                    Harga: Rp 30.000
                      ''')
                elif pilih_produk2 == "5":
                    produk = "Ember Plastik"
                    print("\nDetail Produk: ")
                    print('''
                     Deskripsi: Ember ringan untuk mengangkut air atau material lainnya.
                     Spesifikasi: Material: Plastik tebal, Kapasitas: 10 liter,
                     Harga: Rp 15.000
                    ''')
                else:
                    print ("pilihan tidak tersedia!")
                print(f"{produk} adalah produk yang dipilih {username}")
                print('''
                A. Masukkan keranjang
                B. Beli dan bayar
                ''')
                keranjang_beli = input("pilih menu :").strip().upper()
                if keranjang_beli == "A":
                    keranjang(username, produk)
                elif keranjang_beli == "B":
                    pembayaran()
                else:
                    print("pilihan tidak tersedia")
         os.system('cls')
         search = input(f"Silahkan ketik barang yang anda cari :")
         if search == "Sekop" or search == "Garpu Tanah" :
                print('''
                =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                $$$$$$$$$^^^^^  Alat Pemeliharaan Tanaman ^^^^^$$$$$$$$
                __________________ SELAMAT BERBELANJA ___________________
                ''')
                for i in list_jenisproduk2:
                    print(i,".",list_jenisproduk2[i])
                pilih_produk2 = input("pilih produk: ")
                produk = ""
            
                if pilih_produk2 == "1":
                    produk = "Cangkul"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Alat tanam serbaguna dari baja yang tahan lama.
                    Spesifikasi: Material: Baja tahan karat, Pegangan: Kayu ergonomis,
                    Harga: Rp 50.000
                    ''')
                elif pilih_produk2 == "2":
                    produk = "Sekop"
                    print("\nDetail Produk: ")
                    print('''
                     Deskripsi: Alat berbahan ringan dengan pegangan ergonomis.
                     Spesifikasi: Material: Baja ringan, Pegangan: Plastik anti selip,
                     Harga: Rp 40.000
                     ''')
                elif pilih_produk2 == "3":
                    produk = "Garpu Tanah"
                    print("\nDetail Produk: ")
                    print('''
                     Deskripsi: Alat tajam dan kuat untuk melonggarkan tanah.
                     Spesifikasi: Material: Baja, Pegangan: Kayu solid, Dimensi: 25 cm,
                     Harga: "Rp 30.000"
                     ''')
                elif pilih_produk2 == "4":
                    produk = "Penugal Tanam Manual"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Alat sederhana untuk membuat lubang tanam.
                    Spesifikasi: Material: Logam tahan karat, Panjang: 30 cm,
                    Harga: Rp 30.000
                      ''')
                elif pilih_produk2 == "5":
                    produk = "Ember Plastik"
                    print("\nDetail Produk: ")
                    print('''
                     Deskripsi: Ember ringan untuk mengangkut air atau material lainnya.
                     Spesifikasi: Material: Plastik tebal, Kapasitas: 10 liter,
                     Harga: Rp 15.000
                    ''')
                else:
                    print ("pilihan tidak tersedia!")
                print(f"{produk} adalah produk yang dipilih {username}")
                print('''
                A. Masukkan keranjang
                B. Beli dan bayar
                ''')
                keranjang_beli = input("pilih menu :").strip().upper()
                if keranjang_beli == "A":
                    keranjang(username, produk)
                elif keranjang_beli == "B":
                    pembayaran()
                else:
                    print("pilihan tidak tersedia")
         os.system('cls')
         search = input(f"Silahkan ketik barang yang anda cari :")
         if search == "Ember" :
                print('''
                =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                $$$$$$$$$^^^^^  Alat Pemeliharaan Tanaman ^^^^^$$$$$$$$
                __________________ SELAMAT BERBELANJA ___________________
                ''')
                for i in list_jenisproduk2:
                    print(i,".",list_jenisproduk2[i])
                pilih_produk2 = input("pilih produk: ")
                produk = ""
            
                if pilih_produk2 == "1":
                    produk = "Cangkul"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Alat tanam serbaguna dari baja yang tahan lama.
                    Spesifikasi: Material: Baja tahan karat, Pegangan: Kayu ergonomis,
                    Harga: Rp 50.000
                    ''')
                elif pilih_produk2 == "2":
                    produk = "Sekop"
                    print("\nDetail Produk: ")
                    print('''
                     Deskripsi: Alat berbahan ringan dengan pegangan ergonomis.
                     Spesifikasi: Material: Baja ringan, Pegangan: Plastik anti selip,
                     Harga: Rp 40.000
                     ''')
                elif pilih_produk2 == "3":
                    produk = "Garpu Tanah"
                    print("\nDetail Produk: ")
                    print('''
                     Deskripsi: Alat tajam dan kuat untuk melonggarkan tanah.
                     Spesifikasi: Material: Baja, Pegangan: Kayu solid, Dimensi: 25 cm,
                     Harga: "Rp 30.000"
                     ''')
                elif pilih_produk2 == "4":
                    produk = "Penugal Tanam Manual"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Alat sederhana untuk membuat lubang tanam.
                    Spesifikasi: Material: Logam tahan karat, Panjang: 30 cm,
                    Harga: Rp 30.000
                      ''')
                elif pilih_produk2 == "5":
                    produk = "Ember Plastik"
                    print("\nDetail Produk: ")
                    print('''
                     Deskripsi: Ember ringan untuk mengangkut air atau material lainnya.
                     Spesifikasi: Material: Plastik tebal, Kapasitas: 10 liter,
                     Harga: Rp 15.000
                    ''')
                else:
                    print ("pilihan tidak tersedia!")
                print(f"{produk} adalah produk yang dipilih {username}")
                print('''
                A. Masukkan keranjang
                B. Beli dan bayar
                ''')
                keranjang_beli = input("pilih menu :").strip().upper()
                if keranjang_beli == "A":
                    keranjang(username, produk)
                elif keranjang_beli == "B":
                    pembayaran()
                else:
                    print("pilihan tidak tersedia")
         elif search == "Sprayer" or search == "Pemangkas" :
                os.system('cls')
                print('''
                =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                $$$$$$$$$^^^^^  Alat Pemeliharaan Tanaman ^^^^^$$$$$$$$
                __________________ SELAMAT BERBELANJA ___________________
                ''')
                for i in list_jenisproduk2:
                    print(i,".",list_jenisproduk2[i])
                pilih_produk2 = input("pilih produk: ")
                produk = ""
            
                if pilih_produk2 == "1":
                    produk = "Pestisida Organik"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Pestisida alami untuk mengendalikan hama pada tanaman
                    Spesifikasi: Volume -> Ekstrak tumbuhan, Volume -> 500 ml
                    Harga: Rp 60.000''')
                elif pilih_produk2 == "2":
                    produk = "Fungisida Cair"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Obat cair efektif untuk mencegah jamur pada tanaman
                    Spesifikasi: Volume -> 500 ml, Kandungan -> Fungisida alami
                    Harga: Rp 40.000''')
                elif pilih_produk2 == "3":
                    produk = "Insektisida"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Produk kimia untuk mengatasi serangga pengganggu
                    Spesifikasi: Kandungan -> Insektisida sintetik, Volume -> 250 ml
                    Harga: Rp 50.000''')
                elif pilih_produk2 == "4":
                    produk = "Herbisida"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Pengendali gulma yang efektif untuk melindungi tanaman
                    Spesifikasi: Volume -> 500 ml, Kandungan -> Herbisida sistematik
                    Harga: Rp 45.000''')
                elif pilih_produk2 == "5":
                    produk = "ZPT (Zat Pengatur Tumbuh)"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Larutan untuk merangsang pertumbuhan tanaman
                    Spesifikasi: Volume -> 100 ml, Kandungan -> ZPT alami
                    Harga: Rp 35.000''')
                else:
                    print ("pilihan tidak tersedia!")
                print(f"{produk} adalah produk yang dipilih {username}")
                print('''
                A. Masukkan keranjang
                B. Beli dan bayar
                ''')
                keranjang_beli = input("pilih menu :").strip().upper()
                if keranjang_beli == "A":
                    keranjang(username, produk)
                elif keranjang_beli == "B":
                    pembayaran()
                else:
                    print("pilihan tidak tersedia")
         elif search == "Pencabut" :
                os.system('cls')
                print('''
                =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                $$$$$$$$$^^^^^  Alat Pemeliharaan Tanaman  ^^^^^$$$$$$$$
                __________________ SELAMAT BERBELANJA ___________________
                ''')
                for i in list_jenisproduk2:
                    print(i,".",list_jenisproduk2[i])
                pilih_produk2 = input("pilih produk: ")
                produk = ""
            
                if pilih_produk2 == "1":
                    produk = "Gembor"
                elif pilih_produk2 == "2":
                    produk = "Gunting Dahan"
                elif pilih_produk2 == "3":
                    produk = "Sprayer Manual"
                elif pilih_produk2 == "4":
                    produk = "Pemangkas Tunas Kecil"
                elif pilih_produk2 == "5":
                    produk = "Alat Pencabut Rumput"
                else:
                    print ("pilihan tidak tersedia!")
                print(f"{produk} adalah produk yang dipilih {username}")
                print('''
                A. Masukkan keranjang
                B. Beli dan bayar
                ''')
                keranjang_beli = input("pilih menu :").strip().upper()
                if keranjang_beli == "A":
                    keranjang(username, produk)
                elif keranjang_beli == "B":
                    pembayaran()
                else:
                    print("pilihan tidak tersedia")
         elif search == "Sabit" or search == "Pisau" :
                os.system('cls')
                print('''
                =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                $$$$$$$$$^^^^^  Alat Panen dan Pascapanen  ^^^^^$$$$$$$$
                __________________ SELAMAT BERBELANJA ___________________
                ''')
                for i in list_jenisproduk3:
                    print(i,".",list_jenisproduk3[i])
                pilih_produk3 = input("pilih produk: ")
                produk = ""
            
                if pilih_produk3 == "1":
                    produk = "Sabit"
                elif pilih_produk3 == "2":
                    produk = "Pisau Panen"
                elif pilih_produk3 == "3":
                    produk = "Keranjang Panen Plastik"
                elif pilih_produk3 == "4":
                    produk = "Timbangan Digital"
                elif pilih_produk3 == "5":
                    produk = "Kantong Plastik Panen (10 pcs)"
                else:
                    print ("pilihan tidak tersedia!")
                print(f"{produk} adalah produk yang dipilih {username}")
                print('''
                A. Masukkan keranjang
                B. Beli dan bayar
                ''')
                keranjang_beli = input("pilih menu :").strip().upper()
                if keranjang_beli == "A":
                    keranjang(username, produk)
                elif keranjang_beli == "B":
                    pembayaran()
                else:
                    print("pilihan tidak tersedia")
         elif search == "Keranjang" or search == "Timbangan" :
                os.system('cls')
                print('''
                =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                $$$$$$$$$^^^^^  Alat Panen dan Pascapanen  ^^^^^$$$$$$$$
                __________________ SELAMAT BERBELANJA ___________________
                ''')
                for i in list_jenisproduk3:
                    print(i,".",list_jenisproduk3[i])
                pilih_produk3 = input("pilih produk: ")
                produk = ""
            
                if pilih_produk3 == "1":
                    produk = "Sabit"
                elif pilih_produk3 == "2":
                    produk = "Pisau Panen"
                elif pilih_produk3 == "3":
                    produk = "Keranjang Panen Plastik"
                elif pilih_produk3 == "4":
                    produk = "Timbangan Digital"
                elif pilih_produk3 == "5":
                    produk = "Kantong Plastik Panen"
                else:
                    print ("pilihan tidak tersedia!")
                print(f"{produk} adalah produk yang dipilih {username}")
                print('''
                A. Masukkan keranjang
                B. Beli dan bayar
                ''')
                keranjang_beli = input("pilih menu :").strip().upper()
                if keranjang_beli == "A":
                    keranjang(username, produk)
                elif keranjang_beli == "B":
                    pembayaran()
                else:
                    print("pilihan tidak tersedia")
         elif search == "Plastik" :
                os.system('cls')
                print('''
                =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                $$$$$$$$$^^^^^  Alat Panen dan Pascapanen    ^^^^^$$$$$$$$
                __________________ SELAMAT BERBELANJA ___________________
                ''')
                for i in list_jenisproduk3:
                    print(i,".",list_jenisproduk3[i])
                pilih_produk3 = input("pilih produk: ")
                produk = ""
            
                if pilih_produk3 == "1":
                    produk = "Sabit"
                elif pilih_produk3 == "2":
                    produk = "Pisau Panen"
                elif pilih_produk3 == "3":
                    produk = "Keranjang Panen Plastik"
                elif pilih_produk3 == "4":
                    produk = "Timbangan Digital"
                elif pilih_produk3 == "5":
                    produk = "Kantong Plastik Panen"
                else:
                    print ("pilihan tidak tersedia!")
                print(f"{produk} adalah produk yang dipilih {username}")
                print('''
                A. Masukkan keranjang
                B. Beli dan bayar
                ''')
                keranjang_beli = input("pilih menu :").strip().upper()
                if keranjang_beli == "A":
                    keranjang(username, produk)
                elif keranjang_beli == "B":
                    pembayaran()
                else:
                    print("pilihan tidak tersedia")
         elif search == "Pupuk" or search == "Benih" :
                os.system('cls')
                print('''
                =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                $$$$$$$$$^^^^^      Pupuk dan Benih         ^^^^^$$$$$$$$
                __________________ SELAMAT BERBELANJA ___________________
                ''')
                for i in list_jenisproduk4:
                        print(i,".",list_jenisproduk4[i])
                pilih_produk4 = input("pilih produk: ")
                produk = ""
                
                if pilih_produk4 == "1":
                        produk = "Pupuk Organik"
                elif pilih_produk4 == "2":
                        produk = "Pupuk Urea"
                elif pilih_produk4 == "3":
                        produk = "Benih Sayuran"
                elif pilih_produk4 == "4":
                        produk = "Cocopeat"
                elif pilih_produk4 == "5":
                        produk = "Kapur Dolomit"
                else:
                    print ("pilihan tidak tersedia!")
                    print(f"{produk} adalah produk yang dipilih {username}")
                    print('''
                    A. Masukkan keranjang
                    B. Beli dan bayar
                    ''')
                    keranjang_beli = input("pilih menu :").strip().upper()
                    if keranjang_beli == "A":
                        keranjang(username, produk)
                    elif keranjang_beli == "B":
                        pembayaran()
                    else:
                        print("pilihan tidak tersedia")
         elif search == "Cocopeat" or search == "Kapur" :
                os.system('cls')
                print('''
                =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                $$$$$$$$$^^^^^      Pupuk dan Benih         ^^^^^$$$$$$$$
                __________________ SELAMAT BERBELANJA ___________________
                ''')
                for i in list_jenisproduk4:
                        print(i,".",list_jenisproduk4[i])
                pilih_produk4 = input("pilih produk: ")
                produk = ""
                
                if pilih_produk4 == "1":
                        produk = "Pupuk Organik"
                elif pilih_produk4 == "2":
                        produk = "Pupuk Urea"
                elif pilih_produk4 == "3":
                        produk = "Benih Sayuran"
                elif pilih_produk4 == "4":
                        produk = "Cocopeat"
                elif pilih_produk4 == "5":
                        produk = "Kapur Dolomit"
                else:
                    print ("pilihan tidak tersedia!")
                    print(f"{produk} adalah produk yang dipilih {username}")
                    print('''
                    A. Masukkan keranjang
                    B. Beli dan bayar
                    ''')
                    keranjang_beli = input("pilih menu :").strip().upper()
                    if keranjang_beli == "A":
                        keranjang(username, produk)
                    elif keranjang_beli == "B":
                        pembayaran()
                    else:
                        print("pilihan tidak tersedia")
            
         elif search == "Pestisida" or search == "Fungisida" :
                os.system('cls')
                print('''
                =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                $$$$$$$$$^^^^^  Obat dan Perawatan Tanaman  ^^^^^$$$$$$$$
                __________________ SELAMAT BERBELANJA ___________________
                ''')
                for i in list_jenisproduk5:
                    print(i,".",list_jenisproduk5[i])
                pilih_produk5 = input("pilih produk: ")
                produk = ""
            
                if pilih_produk5 == "1":
                    produk = "Pestisida Organik"
                elif pilih_produk5 == "2":
                    produk = "Fungisida Cair"
                elif pilih_produk5 == "3":
                    produk = "Insektisida"
                elif pilih_produk5 == "4":
                    produk = "Herbisida"
                elif pilih_produk5 == "5":
                    produk = "ZPT (Zat Pengatur Tumbuh)"
                else:
                    print ("pilihan tidak tersedia!")
                print(f"{produk} adalah produk yang dipilih {username}")
                print('''
                A. Masukkan keranjang
                B. Beli dan bayar
                ''')
                keranjang_beli = input("pilih menu :").strip().upper()
                if keranjang_beli == "A":
                    keranjang(username, produk)
                elif keranjang_beli == "B":
                    pembayaran()
                else:
                    print("pilihan tidak tersedia")
         elif search == "Insektisida" or search == "Herbisida" :
                os.system('cls')
                print('''
                =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                $$$$$$$$$^^^^^  Obat dan Perawatan Tanaman  ^^^^^$$$$$$$$
                __________________ SELAMAT BERBELANJA ___________________
                ''')
                for i in list_jenisproduk5:
                    print(i,".",list_jenisproduk5[i])
                pilih_produk5 = input("pilih produk: ")
                produk = ""
            
                if pilih_produk5 == "1":
                    produk = "Pestisida Organik"
                elif pilih_produk5 == "2":
                    produk = "Fungisida Cair"
                elif pilih_produk5 == "3":
                    produk = "Insektisida"
                elif pilih_produk5 == "4":
                    produk = "Herbisida"
                elif pilih_produk5 == "5":
                    produk = "ZPT (Zat Pengatur Tumbuh)"
                else:
                    print ("pilihan tidak tersedia!")
                print(f"{produk} adalah produk yang dipilih {username}")
                print('''
                A. Masukkan keranjang
                B. Beli dan bayar
                ''')
                keranjang_beli = input("pilih menu :").strip().upper()
                if keranjang_beli == "A":
                    keranjang(username, produk)
                elif keranjang_beli == "B":
                    pembayaran()
                else:
                    print("pilihan tidak tersedia")
         elif search == "ZPT":
                os.system('cls')
                print('''
                =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                $$$$$$$$$^^^^^  Obat dan Perawatan Tanaman  ^^^^^$$$$$$$$
                __________________ SELAMAT BERBELANJA ___________________
                ''')
                for i in list_jenisproduk5:
                    print(i,".",list_jenisproduk5[i])
                pilih_produk2 = input("pilih produk: ")
                produk = ""
            
                if pilih_produk5 == "1":
                    produk = "Pestisida Organik"
                elif pilih_produk5 == "2":
                    produk = "Fungisida Cair"
                elif pilih_produk5 == "3":
                    produk = "Insektisida"
                elif pilih_produk5 == "4":
                    produk = "Herbisida"
                elif pilih_produk5 == "5":
                    produk = "ZPT (Zat Pengatur Tumbuh)"
                else:
                    print ("pilihan tidak tersedia!")
                print(f"{produk} adalah produk yang dipilih {username}")
                print('''
                A. Masukkan keranjang
                B. Beli dan bayar
                ''')
                keranjang_beli = input("pilih menu :").strip().upper()
                if keranjang_beli == "A":
                    keranjang(username, produk)
                elif keranjang_beli == "B":
                    pembayaran()
                else:
                    print("pilihan tidak tersedia")
            
    elif jenis == '4':
            os.system('cls')
            print('''
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            $$$$$$$$$^^^^^  Obat dan Perawatan Tanaman  ^^^^^$$$$$$$$
            __________________ SELAMAT BERBELANJA ___________________
            ''')
            for i in list_jenisproduk4:
                nama_produk, harga_produk = list_jenisproduk4[i]
                print(f"{i}. {nama_produk} - Rp{harga_produk}")
        
            pilih_produk4 = input("Pilih produk (1-5): ").strip()
            if pilih_produk4 in list_jenisproduk4:
                produk, harga = list_jenisproduk4[pilih_produk4]
                print(f"\n{produk} dengan harga Rp{harga} adalah produk yang dipilih oleh {username}")
                print('''
                A. Masukkan keranjang
                B. Beli dan bayar
                ''')
                keranjang_beli = input("Pilih menu: ").strip().upper()
                if keranjang_beli == "A":
                    keranjang(username, produk, harga)
                elif keranjang_beli == "B":
                    keranjang(username, produk, harga)
                    pembayaran(username)
                else:
                    print("Pilihan tidak tersedia. Kembali ke menu.")
                    jenis_produk(username)
            else:
                print("Pilihan tidak tersedia!")
                input("Tekan Enter untuk kembali.")
                jenis_produk(username)
            
    elif jenis == "5":   
        os.system('cls' if os.name == 'nt' else 'clear')
    print('''
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    $$$$$$$$$^^^^^  Obat dan Perawatan Tanaman  ^^^^^$$$$$$$$
    __________________ SELAMAT BERBELANJA ___________________
    ''')
    for i in list_jenisproduk5:
        nama_produk, harga_produk = list_jenisproduk5[i]
        print(f"{i}. {nama_produk} - Rp{harga_produk}")
    
    pilih_produk5 = input("Pilih produk (1-5): ").strip()
    if pilih_produk5 in list_jenisproduk5:
        produk, harga = list_jenisproduk5[pilih_produk5]
        print(f"\n{produk} dengan harga Rp{harga} adalah produk yang dipilih oleh {username}")
        print('''
        A. Masukkan keranjang
        B. Beli dan bayar
        ''')
        keranjang_beli = input("Pilih menu: ").strip().upper()
        if keranjang_beli == "A":
            keranjang(username, produk, harga)
        elif keranjang_beli == "B":
            keranjang(username, produk, harga)
            pembayaran(username)
        else:
            print("Pilihan tidak tersedia. Kembali ke menu.")
            jenis_produk(username)
    else:
        print("Pilihan tidak tersedia!")
        input("Tekan Enter untuk kembali.")
        jenis_produk(username)

# Fungsi untuk menambahkan produk ke keranjang
def keranjang(username, produk, harga):
    jumlah = int(input(f"Masukkan jumlah {produk}: "))
    total_harga = harga * jumlah

    keranjang_file = 'KeranjangTRIJAYA.csv'
    data_keranjang = []

    # Cek apakah file sudah ada
    file_exists = os.path.isfile(keranjang_file)

    # Baca file jika sudah ada
    if file_exists:
        with open(keranjang_file, mode='r') as file:
            reader = csv.reader(file)
            data_keranjang = list(reader)
    
    # Header file CSV
    header = ["username", "produk", "harga", "jumlah", "total"]
    
    # Cek apakah produk sudah ada di keranjang
    produk_ada = False
    for i in range(len(data_keranjang)):
        if len(data_keranjang[i]) == 5:
            user, prod, hrg, jml, tot = data_keranjang[i]
            if user == username and prod == produk:
                # Jika produk sudah ada, perbarui jumlah dan total
                data_keranjang[i][3] = str(int(jml) + jumlah)  # Update jumlah
                data_keranjang[i][4] = str(int(hrg) * int(data_keranjang[i][3]))  # Update total
                produk_ada = True
                break
    
    if not produk_ada:
        # Tambahkan produk baru jika belum ada
        data_keranjang.append([username, produk, str(harga), str(jumlah), str(total_harga)])
    
    # Tulis ulang data ke file
    with open(keranjang_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        if not file_exists or data_keranjang[0] != header:
            writer.writerow(header)
        writer.writerows(data_keranjang)
    
    print(f"{produk} berhasil ditambahkan ke keranjang!\n")
    print('''
        A. Tambahkan produk lagi
        B. Lanjutkan ke pembayaran
        ''')
    keranjang_beli = input("Pilih menu: ").strip().upper()

    if keranjang_beli == "A":
        jenis_produk(username)
    elif keranjang_beli == "B":
        pembayaran(username)
    else:
        print("Pilihan tidak tersedia. Kembali ke menu utama.")
        jenis_produk(username)

# Fungsi pembayaran
def pembayaran(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Memproses pembayaran untuk {username}...\n")
    
    # Membaca keranjang pengguna
    total_belanja = 0
    keranjang_user = {}

    print(f"Keranjang {username}:")
    print(f"{'Produk':<15} {'Harga':<10} {'Jumlah':<8} {'Total':<10}")
    print("-" * 50)

    try:
        with open('KeranjangTRIJAYA.csv', mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Baca header
            
            for row in reader:
                if len(row) < 5:
                    continue  # Lewati baris tidak valid
                
                user, produk, harga, jumlah, total = row
                if user == username:
                    # Jika produk sudah ada, perbarui jumlah dan total
                    if produk in keranjang_user:
                        keranjang_user[produk]['jumlah'] += int(jumlah)
                        keranjang_user[produk]['total'] += int(total)
                    else:
                        keranjang_user[produk] = {
                            'harga': int(harga),
                            'jumlah': int(jumlah),
                            'total': int(total),
                        }

        # Tampilkan keranjang pengguna
        for produk, data in keranjang_user.items():
            print(f"{produk:<15} {data['harga']:<10} {data['jumlah']:<8} {data['total']:<10}")
            total_belanja += data['total']
    except FileNotFoundError:
        print("Keranjang kosong. Silakan tambahkan produk terlebih dahulu.")
        return
    except ValueError:
        print("Terjadi kesalahan pada format data keranjang.")
        return

    print("-" * 50)
    print(f"Total Belanja: Rp{total_belanja}")
    print('''
    Pilih Metode Pembayaran:
    1. Bank Account
    2. Cash on Delivery
    ''')
    metode = input("Pilih metode pembayaran: ").strip()
    if metode == '1':
        bank_account(total_belanja)
    elif metode == '2':
        print(f"Total Belanja: Rp{total_belanja}")
        print("Pembayaran akan dilakukan saat barang diterima (COD).")
        kosongkan_keranjang(username)
    else:
        print("Metode pembayaran tidak valid.")
        pembayaran(username)

# Fungsi pembayaran melalui bank
def bank_account(total_belanja):
    print('''
    Pilih Bank:
    1. BCA
    2. Mandiri
    3. BRI
    4. BNI
    ''')
    bank = input("Pilih bank: ").strip()
    if bank in ['1', '2', '3', '4']:
        rekening = input("Masukkan nomor rekening Anda: ")
        print(f"Total yang harus dibayarkan: Rp{total_belanja}")
        print(f"Lakukan pembayaran ke rekening TRIJAYA: 2424101010.")
        print("Pembayaran berhasil!")
        print('''
            A. Kembali ke menu utama
            B. Keluar
        ''')
        pilihan = input("Pilih menu: ").strip().upper()
        if pilihan == "A":
            home()  # Ganti dengan fungsi menu utama
        elif pilihan == "B":
            print("Terima kasih telah berbelanja di TRIJAYA!")
            exit()
        else:
            print("Pilihan tidak valid. Mengakhiri program.")
            exit()
    else:
        print("Pilihan bank tidak valid.")
        bank_account(total_belanja)
    
# Fungsi untuk mengosongkan keranjang
def kosongkan_keranjang(username):
    data_baru = []
    try:
        with open('KeranjangTRIJAYA.csv', mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if row[0] != username:  # Simpan data pengguna lain
                    data_baru.append(row)
    except FileNotFoundError:
        print("File keranjang tidak ditemukan.")
        return
    
    # Tulis ulang data yang bukan milik pengguna
    with open('KeranjangTRIJAYA.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data_baru)
    print("Keranjang Anda telah dikosongkan.")
    jenis_produk(username)
    kosongkan_keranjang(username)


# def voucher():
#     voucher = ()
#     if voucher == "TR1J4Y4" :
#         print ("VOUCHER BERHASIL, KAMU MENDAPATKAN VOUCHER SEBESAR 5%")
#         harga_total = harga - harga * 0.05
#         print (harga_total)
#     elif voucher == "W1NS4C0M3L":
#         print ("VOUCHER BERHASIL, KAMU MENDAPATKAN VOUCHER SEBESAR 5%")
#         harga_total = harga - harga * 0.05
#         print (harga_total)
#     elif voucher == "":
#         pass

def data_pengiriman():
    os.system('cls')
    
    nama_pembeli = input ("Masukkan Nama: ")
    provinsi_pembeli = input ("Masukkan Provinsi: ")
    alamat_pembeli = input ("Masukkan Alamat: ")
    no_pembeli = input ("Masukkan Nomor HP: ")

    print ('''
    PILIH OPSI KURIR:
    1. JNE
    2. SiCepat Express
    3. JNT
    4. Trijaya Express
           ''')
    kurir = input ("Pilih Opsi Kurir: ")
    if kurir == "1":
        print ("Pengriman Menggunakan JNE, dengan nama", nama_pembeli ,)
        print ("Provinsi: ", provinsi_pembeli)
        print ("Alamat: ", alamat_pembeli)
        print ("Nomor HP: ", no_pembeli)

    elif kurir == "2":
        print ("Pengriman Menggunakan SiCepat Express, dengan nama", nama_pembeli ,)
        print ("Provinsi: ", provinsi_pembeli)
        print ("Alamat: ", alamat_pembeli)
        print ("Nomor HP: ", no_pembeli)
    
    elif kurir == "3":
        print ("Pengriman Menggunakan JNT, dengan nama", nama_pembeli ,)
        print ("Provinsi: ", provinsi_pembeli)
        print ("Alamat: ", alamat_pembeli)
        print ("Nomor HP: ", no_pembeli)
    
    elif kurir == "4":
        print ("Pengriman Menggunakan Trijaya Express, dengan nama", nama_pembeli ,)
        print ("Provinsi: ", provinsi_pembeli)
        print ("Alamat: ", alamat_pembeli)
        print ("Nomor HP: ", no_pembeli)

    elif not os.path.isfile('provinsi.csv'): 
        print("Wilayah Tidak Tersedia!.")
        return None
    
    with open('provinsi.csv', mode='r') as file:
        reader = csv.DictReader(file)
        provinsi_found = False  # Flag untuk mengecek apakah provinsi ditemukan
        for row in reader:
            if row['provinsi'].lower() == provinsi_pembeli.lower():  # Membandingkan dengan provinsi dari input
                provinsi_found = True
                ongkir = row['ongkir']
                print(f"Ongkir untuk wilayah {provinsi_pembeli} adalah {ongkir}!")
                
        
        if not provinsi_found:
            print(f"Provinsi {provinsi_pembeli} tidak ditemukan dalam daftar.")
            return None

# def deskripsi_produk():
#     pass


def main():
    home()
    
main()

     
                 
