import pandas as pd
import csv
import os 

list_jenisproduk = {
   1:"Alat Tanam dan Persiapan Lahan",
   2:"Alat Pemeliharaan Tanaman",
   3:"Alat Panen dan Pascapanen",
   4:"Alat Pupuk dan Benih",
   5:"Obat dan Perawatan Tanaman",
   6:"Pencarian",
   7:"Kembali"
}
list_jenisproduk1 = pd.read_csv('list_jenisproduk1.csv')
list_jenisproduk2 = pd.read_csv('list_jenisproduk2.csv')
list_jenisproduk3 = pd.read_csv('list_jenisproduk3.csv')
list_jenisproduk4 = pd.read_csv('list_jenisproduk4.csv')
list_jenisproduk5 = pd.read_csv('list_jenisproduk5.csv')
def home():
    os.system('cls' if os.name == 'nt' else 'clear') 
    print('''
        ░██████╗███████╗██╗░░░░░░█████╗░███╗░░░███╗░█████╗░████████╗
        ██╔════╝██╔════╝██║░░░░░██╔══██╗████╗░████║██╔══██╗╚══██╔══╝
        ╚█████╗░█████╗░░██║░░░░░███████║██╔████╔██║███████║░░░██║░░░
        ░╚═══██╗██╔══╝░░██║░░░░░██╔══██║██║╚██╔╝██║██╔══██║░░░██║░░░
        ██████╔╝███████╗███████╗██║░░██║██║░╚═╝░██║██║░░██║░░░██║░░░
        ╚═════╝░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░

        ██████╗░░█████╗░████████╗░█████╗░███╗░░██╗░██████╗░  
        ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗░██║██╔════╝░  
        ██║░░██║███████║░░░██║░░░███████║██╔██╗██║██║░░██╗░  
        ██║░░██║██╔══██║░░░██║░░░██╔══██║██║╚████║██║░░╚██╗  
        ██████╔╝██║░░██║░░░██║░░░██║░░██║██║░╚███║╚██████╔╝  
        ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░  

        ██████╗░██╗
        ██╔══██╗██║
        ██║░░██║██║
        ██║░░██║██║
        ██████╔╝██║
        ╚═════╝░╚═╝

        ████████╗██████╗░██╗░░░░░██╗░█████╗░██╗░░░██╗░█████╗░
        ╚══██╔══╝██╔══██╗██║░░░░░██║██╔══██╗╚██╗░██╔╝██╔══██╗
        ░░░██║░░░██████╔╝██║░░░░░██║███████║░╚████╔╝░███████║
        ░░░██║░░░██╔══██╗██║██╗░░██║██╔══██║░░╚██╔╝░░██╔══██║
        ░░░██║░░░██║░░██║██║╚█████╔╝██║░░██║░░░██║░░░██║░░██║
        ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝
        ''')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("$$$$$$$$$^^^^^  SELAMAT DATANG di TRIJAYA  ^^^^^$$$$$$$$")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("""
          [1] Register
          [2] Login
          [3] Admin Login
          [4] Exit
    """)
    print("----------------------------------------------------------")
    
    home1 = input("Pilih fitur (1/2/3/4): ")
    if home1 == "1":
        register()
    elif home1 == "2":
        login()
    elif home1 == "3":
        login_admin()
    elif home1 == "4":
        print("Terima kasih telah menggunakan aplikasi TRIJAYA! Sampai jumpa.")
    else:
        print("Pilihan tidak tersedia, coba lagi.")
        input()
        home()  

def register():
    os.system('cls' if os.name == 'nt' else 'clear') 
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("$$$$$$$$$^^^^^  SELAMAT DATANG di TRIJAYA  ^^^^^$$$$$$$$")
    print("______________________  REGISTER  ______________________")
    print("----------------------------------------------------------")
    
    username = input("Masukkan username anda: ").strip()
    password = input("Masukkan password anda: ").strip()
    
    try:
        df = pd.read_csv('RegTRIJAYA.csv')
    except FileNotFoundError:
        print("File does not exist.")

    if not username or not password:
        print("Username dan password tidak boleh kosong. Silakan coba lagi.")
        input("klik enter untuk kembali")
        home()

    new_data = pd.DataFrame({'username': [username], 'password': [password]})
    new_data.to_csv('RegTRIJAYA.csv', mode='a', index=False, header=False)
    return home()

def login():
    os.system('cls' if os.name == 'nt' else 'clear') 
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("$$$$$$$$$^^^^^  SELAMAT DATANG di TRIJAYA  ^^^^^$$$$$$$$")
    print("________________________ LOGIN _________________________")
    print("----------------------------------------------------------")

    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()

    if not os.path.isfile('RegTRIJAYA.csv'):
        print("Akun tidak terdaftar. Silakan daftar terlebih dahulu!")
        input("Tekan Enter untuk kembali ke menu utama...")
        return None

    with open('RegTRIJAYA.csv', mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['username'] == username and row['password'] == password:
                print(f"Selamat datang, {username}!")
                print("----------------------------------------------------------")
                jenis_produk(username)
                return username

        print("Login gagal! Username atau password salah.")
        print("----------------------------------------------------------")
        input("Tekan Enter untuk mencoba lagi...")
        home()
        return None
                
       
def login_admin():
    os.system('cls' if os.name == 'nt' else 'clear') 
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("$$$$$$$$$^^^^^  SELAMAT DATANG di TRIJAYA  ^^^^^$$$$$$$$")
    print("______________________  ADMIN LOGIN  ______________________")
    print("----------------------------------------------------------")

    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()

    if not os.path.isfile('admin.csv'):
        print("Akun admin tidak terdaftar. Silakan daftar terlebih dahulu!")
        input("Tekan Enter untuk kembali ke menu utama...")
        return None

    df = pd.read_csv('admin.csv')
    matched_admin = df[(df['username'] == username) & (df['password'] == password)]

    if not matched_admin.empty:
        print(f"Selamat datang, Admin {username}!")
        print("----------------------------------------------------------")
        ubah_stok()
    else:
        print("Login gagal! Username atau password salah.")
        print("----------------------------------------------------------")
        input("Tekan Enter untuk mencoba lagi...")
        return None
def ubah_stok():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n=-=-=-=-=-=-=-= UBAH STOK PRODUK =-=-=-=-=-=-=-=")

    # Daftar produk dalam dictionary
    produk_dict = {
        "1": list_jenisproduk1,
        "2": list_jenisproduk2,
        "3": list_jenisproduk3,
        "4": list_jenisproduk4,
        "5": list_jenisproduk5
    }

    # Menampilkan kategori
    print("\nKategori Produk:")
    print("1. Alat Tanam")
    print("2. Alat Perawatan")
    print("3. Alat Panen")
    print("4. Pupuk dan Media Tanam")
    print("5. Obat-Obatan dan ZPT")

    # Memilih kategori
    kategori = input("\nMasukkan nomor kategori produk yang ingin diubah: ").strip()
    if kategori not in produk_dict:
        print("Kategori tidak valid!")
        return

    # Mendapatkan produk dalam kategori
    produk = produk_dict[kategori]
    print("\nProduk dalam kategori:")
    for key, value in produk.items():
        print(f"{key}. {value[0]} (Harga: {value[1]}, Stok: {value[2]})")

    # Memilih produk
    produk_id = input("\nMasukkan ID produk yang ingin diubah: ").strip()
    if produk_id not in produk:
        print("ID produk tidak valid!")
        return
    try:
        stok_baru = int(input(f"Masukkan stok baru untuk produk '{produk[produk_id][0]}': "))
        produk[produk_id] = (produk[produk_id][0], produk[produk_id][1], stok_baru)
        print(f"Stok untuk '{produk[produk_id][0]}' berhasil diperbarui menjadi {stok_baru}.")
        input("Klik enter untuk kembali")
        home()
    except ValueError:
        print("Input tidak valid! Stok harus berupa angka.")
def data_pengiriman():
    os.system('cls')
    print("======= DATA PENGIRIMAN =======")
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
    
    df = pd.read_csv('provinsi.csv')
    matched_provinsi = df[df['provinsi'].str.lower() == provinsi_pembeli.lower()]

    if not matched_provinsi.empty:
        ongkir = matched_provinsi['ongkir'].values[0] 
        print(f"Ongkir untuk wilayah {provinsi_pembeli} adalah {ongkir}!")
        return ongkir
    else:
        print(f"Provinsi {provinsi_pembeli} tidak ditemukan dalam daftar.")
        return None

def jenis_produk(username):
    os.system('cls')
    print(f"Selamat datang, silahkan pilih jenis produk : ")
    for i in list_jenisproduk:
        print(i,list_jenisproduk[i])
    jenis = input("Pilihlah jenis produk (1/2/3/4/5/6): ")
    if not jenis:
        print("Masukkan pilihan!")
        input("tekan enter untuk kembali")
        jenis_produk(username)
    elif jenis == '1':
        os.system('cls')
        print(''' 
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- 
        $$$$$$$$$^^^^^  Alat Persiapan Lahan  ^^^^^$$$$$$$$ 
        __________________ SELAMAT BERBELANJA ___________________ 
        ''')
        print(list_jenisproduk1)

        
        pilih_produk1 = input("Pilih produk (1-5): ").strip()
        produk = ""
        
        if not pilih_produk1:
            print("Masukkan pilihan!")
            input("tekan enter untuk kembali")
            jenis_produk(username)
        elif pilih_produk1 == "1":
                produk = "Cangkul"
                print("\nDetail Produk: ")
                print('''
                Deskripsi Produk: Alat tanam serbaguna dari baja yang tahan lama
                Spesifikasi: Material -> Baja tahan karat,Pegangan -> Kayu ergonomis
                Harga: Rp 50.000''')
        elif pilih_produk1 == "2":
                    produk = "Sekop"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi Produk: Alat berbahan ringan dengan pegangan ergonomis
                    Spesifikasi: Material -> Baja ringan, Pegangan -> Plastik anti selip
                    Harga: Rp 40.000''')
        elif pilih_produk1 == "3":
                    produk = "Garpu Tanah"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Alat tajam dan kuat untuk melonggarkan tanah
                    Spesifikasi: Material -> Baja, Pegangan -> Kayu solid, Dimensi: 25 cm
                    Harga: Rp 30.000''')
        elif pilih_produk1 == "4":
                    produk = "Penugal Tanam Manual"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Alat sederhana untuk membuat lubang tanam
                    Spesifikasi: Material -> Logam tahan karat, Panjang -> 30 cm
                    Harga: Rp 30.000''')
        elif pilih_produk1 == "5":
                    produk = "Ember Plastik"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Ember ringan untuk mengangkut air atau material lainnya
                    Spesifikasi: Material -> Plastik tebal, Kapasitas -> 10 liter
                    Harga: Rp 15.000''')
        if pilih_produk1 in list_jenisproduk1:  # Memastikan pilihan valid
            produk, harga, stok = list_jenisproduk1[pilih_produk1]  # Mengambil produk dan harga
            print(f"\n{produk} stok: {stok} dengan harga Rp{harga} adalah produk yang dipilih oleh {username}")
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
        # else:
        #     print("Pilihan tidak tersedia!")
        #     input("Tekan Enter untuk kembali.")
        #     jenis_produk(username)
    elif jenis == '2':
            os.system('cls')
            print('''
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    $$$$$$$$$^^^^^  Alat Pemeliharaan Tanaman  ^^^^^$$$$$$$$
    __________________ SELAMAT BERBELANJA ___________________
            ''')
            print("Daftar Produk:")
            for i, row in list_jenisproduk2.iterrows():
                print(f"{row['ID']}. {row['Nama Produk']} - Harga: Rp {row['Harga']} - Stok: {row['Stok']}")

            pilih_produk2 = input("Pilih produk (1-5): ").strip()

            # Mengecek apakah pilihan valid
            if pilih_produk2.isdigit() and int(pilih_produk2) in list_jenisproduk2['ID'].values:
                # Mengambil data produk berdasarkan ID yang dipilih
                produk = list_jenisproduk2[list_jenisproduk2['ID'] == int(pilih_produk2)].iloc[0]
                nama_produk = produk['Nama Produk']
                harga = produk['Harga']
                stok = produk['Stok']

                # Menampilkan detail produk
                print(f"\n{nama_produk} dengan harga Rp{harga} adalah produk yang dipilih oleh {username}")
                print(f"Stok: {stok}")
                print('''
                A. Masukkan keranjang
                B. Beli dan bayar
                ''')

                keranjang_beli = input("Pilih menu: ").strip().upper()

                if keranjang_beli == "A":
                    keranjang(username, nama_produk, harga)
                elif keranjang_beli == "B":
                    keranjang(username, nama_produk, harga)
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
                nama_produk, harga_produk, stok_produk = list_jenisproduk1[i]
                print(f"{i}. {nama_produk} - Rp{harga_produk} - {stok_produk}")
            
            pilih_produk3 = input("Pilih produk (1-5): ").strip()

            produk = ""    
            if not pilih_produk3:
                print("Masukkan pilihan!")
                input("tekan enter untuk kembali")
                jenis_produk(username)
            elif pilih_produk3 == "1":
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
         if search == "cangkul" or search == "ember" :
            print('''
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            $$$$$$$$$^^^^^  Alat Persiapan Lahan  ^^^^^$$$$$$$$
            __________________ SELAMAT BERBELANJA ___________________
            ''')
            for i in list_jenisproduk1:
                nama_produk, harga_produk, stok_produk = list_jenisproduk1[i]
                print(f"{i}. {nama_produk} - Rp{harga_produk} - {stok_produk}")
                
            pilih_produk1 = input("Pilih produk (1-5): ").strip()
            produk = ""
            if not pilih_produk1:
                print("Masukkan pilihan!")
                input("tekan enter untuk kembali")
                jenis_produk(username)
            elif pilih_produk1 == "1":
                produk = "Cangkul"
                print("\nDetail Produk: ")
                print('''
                Deskripsi Produk: Alat tanam serbaguna dari baja yang tahan lama
                Spesifikasi: Material -> Baja tahan karat,Pegangan -> Kayu ergonomis
                Harga: Rp 50.000''')
            elif pilih_produk1 == "2":
                produk = "Sekop"
                print("\nDetail Produk: ")
                print('''
                Deskripsi Produk: Alat berbahan ringan dengan pegangan ergonomis
                Spesifikasi: Material -> Baja ringan, Pegangan -> Plastik anti selip
                Harga: Rp 40.000''')
            elif pilih_produk1 == "3":
                produk = "Garpu Tanah"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Alat tajam dan kuat untuk melonggarkan tanah
                Spesifikasi: Material -> Baja, Pegangan -> Kayu solid, Dimensi: 25 cm
                Harga: Rp 30.000''')
            elif pilih_produk1 == "4":
                produk = "Penugal Tanam Manual"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Alat sederhana untuk membuat lubang tanam
                Spesifikasi: Material -> Logam tahan karat, Panjang -> 30 cm
                Harga: Rp 30.000''')
            elif pilih_produk1 == "5":
                produk = "Ember Plastik"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Ember ringan untuk mengangkut air atau material lainnya
                Spesifikasi: Material -> Plastik tebal, Kapasitas -> 10 liter
                Harga: Rp 15.000''')
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
         os.system('cls')
         if search == "sekop" or search == "garpu tanah" :
            print('''
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        $$$$$$$$$^^^^^  Alat Persiapan Lahan  ^^^^^$$$$$$$$
        __________________ SELAMAT BERBELANJA ___________________
        ''')
            for i in list_jenisproduk1:
                nama_produk, harga_produk, stok_produk = list_jenisproduk1[i]
                print(f"{i}. {nama_produk} - Rp{harga_produk} - {stok_produk}")
            
            pilih_produk1 = input("Pilih produk (1-5): ").strip()
            produk = ""
            if not pilih_produk1:
                print("Masukkan pilihan!")
                input("tekan enter untuk kembali")
                jenis_produk(username)
            elif pilih_produk1 == "1":
                produk = "Cangkul"
                print("\nDetail Produk: ")
                print('''
                Deskripsi Produk: Alat tanam serbaguna dari baja yang tahan lama
                Spesifikasi: Material -> Baja tahan karat,Pegangan -> Kayu ergonomis
                Harga: Rp 50.000''')
            elif pilih_produk1 == "2":
                produk = "Sekop"
                print("\nDetail Produk: ")
                print('''
                Deskripsi Produk: Alat berbahan ringan dengan pegangan ergonomis
                Spesifikasi: Material -> Baja ringan, Pegangan -> Plastik anti selip
                Harga: Rp 40.000''')
            elif pilih_produk1 == "3":
                produk = "Garpu Tanah"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Alat tajam dan kuat untuk melonggarkan tanah
                Spesifikasi: Material -> Baja, Pegangan -> Kayu solid, Dimensi: 25 cm
                Harga: Rp 30.000''')
            elif pilih_produk1 == "4":
                produk = "Penugal Tanam Manual"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Alat sederhana untuk membuat lubang tanam
                Spesifikasi: Material -> Logam tahan karat, Panjang -> 30 cm
                Harga: Rp 30.000''')
            elif pilih_produk1 == "5":
                produk = "Ember Plastik"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Ember ringan untuk mengangkut air atau material lainnya
                Spesifikasi: Material -> Plastik tebal, Kapasitas -> 10 liter
                Harga: Rp 15.000''')
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
                
         os.system('cls')
         if search == "ember" :
            print('''
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        $$$$$$$$$^^^^^  Alat Persiapan Lahan  ^^^^^$$$$$$$$
        __________________ SELAMAT BERBELANJA ___________________
        ''')
            for i in list_jenisproduk1:
                nama_produk, harga_produk, stok_produk = list_jenisproduk1[i]
                print(f"{i}. {nama_produk} - Rp{harga_produk} - {stok_produk}")
            
            pilih_produk1 = input("Pilih produk (1-5): ").strip()
            produk = ""
            if not pilih_produk1:
                print("Masukkan pilihan!")
                input("tekan enter untuk kembali")
                jenis_produk(username)
            elif pilih_produk1 == "1":
                produk = "Cangkul"
                print("\nDetail Produk: ")
                print('''
                Deskripsi Produk: Alat tanam serbaguna dari baja yang tahan lama
                Spesifikasi: Material -> Baja tahan karat,Pegangan -> Kayu ergonomis
                Harga: Rp 50.000''')
            elif pilih_produk1 == "2":
                produk = "Sekop"
                print("\nDetail Produk: ")
                print('''
                Deskripsi Produk: Alat berbahan ringan dengan pegangan ergonomis
                Spesifikasi: Material -> Baja ringan, Pegangan -> Plastik anti selip
                Harga: Rp 40.000''')
            elif pilih_produk1 == "3":
                produk = "Garpu Tanah"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Alat tajam dan kuat untuk melonggarkan tanah
                Spesifikasi: Material -> Baja, Pegangan -> Kayu solid, Dimensi: 25 cm
                Harga: Rp 30.000''')
            elif pilih_produk1 == "4":
                produk = "Penugal Tanam Manual"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Alat sederhana untuk membuat lubang tanam
                Spesifikasi: Material -> Logam tahan karat, Panjang -> 30 cm
                Harga: Rp 30.000''')
            elif pilih_produk1 == "5":
                produk = "Ember Plastik"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Ember ringan untuk mengangkut air atau material lainnya
                Spesifikasi: Material -> Plastik tebal, Kapasitas -> 10 liter
                Harga: Rp 15.000''')
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
        
         elif search == "gembor" or search == "gunting" :

                print('''
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            $$$$$$$$$^^^^^  Alat Pemeliharaan Tanaman  ^^^^^$$$$$$$$
            __________________ SELAMAT BERBELANJA ___________________
            ''')
                for i in list_jenisproduk2:
                    nama_produk, harga_produk, stok_produk = list_jenisproduk2[i]
                    print(f"{i}. {nama_produk} - Rp{harga_produk} - {stok_produk}")
                
                pilih_produk2 = input("Pilih produk (1-5): ").strip()
                produk = ""
                if not pilih_produk2:
                    print("Masukkan pilihan!")
                    input("tekan enter untuk kembali")
                    jenis_produk(username)
                elif pilih_produk2 == "1":
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
         elif search == "sprayer" or search == "pemangkas" :
                os.system('cls')
                print('''
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            $$$$$$$$$^^^^^  Alat Pemeliharaan Tanaman  ^^^^^$$$$$$$$
            __________________ SELAMAT BERBELANJA ___________________
            ''')
                for i in list_jenisproduk2:
                    nama_produk, harga_produk, stok_produk = list_jenisproduk2[i]
                    print(f"{i}. {nama_produk} - Rp{harga_produk} - {stok_produk}")
                
                pilih_produk2 = input("Pilih produk (1-5): ").strip()
                produk = ""
                if not pilih_produk2:
                    print("Masukkan pilihan!")
                    input("tekan enter untuk kembali")
                    jenis_produk(username)
                elif pilih_produk2 == "1":
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
         elif search == "pencabut" :
                os.system('cls')
                print('''
                =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                $$$$$$$$$^^^^^  Alat Pemeliharaan Tanaman  ^^^^^$$$$$$$$
                __________________ SELAMAT BERBELANJA ___________________
                ''')
                for i in list_jenisproduk2:
                    nama_produk, harga_produk, stok_produk = list_jenisproduk2[i]
                    print(f"{i}. {nama_produk} - Rp{harga_produk} - {stok_produk}")
                
                pilih_produk2 = input("Pilih produk (1-5): ").strip()
                produk = ""
                if not pilih_produk2:
                    print("Masukkan pilihan!")
                    input("tekan enter untuk kembali")
                    jenis_produk(username)
                elif pilih_produk2 == "1":
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
         elif search == "sabit" or search == "pisau" :
                os.system('cls')
                print('''
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            $$$$$$$$$^^^^^  Obat dan Perawatan Tanaman  ^^^^^$$$$$$$$
            __________________ SELAMAT BERBELANJA ___________________
            ''')
                for i in list_jenisproduk3:
                    nama_produk, harga_produk, stok_produk = list_jenisproduk3[i]
                    print(f"{i}. {nama_produk} - Rp{harga_produk} - {stok_produk}")
                
                pilih_produk3 = input("Pilih produk (1-5): ").strip()
                
                produk = ""
                if not pilih_produk3:
                    print("Masukkan pilihan!")
                    input("tekan enter untuk kembali")
                    jenis_produk(username)
            
                elif pilih_produk3 == "1":
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
           
         elif search == "keranjang" or search == "timbangan" :
                os.system('cls')
                print('''
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            $$$$$$$$$^^^^^  Obat dan Perawatan Tanaman  ^^^^^$$$$$$$$
            __________________ SELAMAT BERBELANJA ___________________
            ''')
                for i in list_jenisproduk3:
                    nama_produk, harga_produk, stok_produk = list_jenisproduk3[i]
                    print(f"{i}. {nama_produk} - Rp{harga_produk} - {stok_produk}")
                    
                pilih_produk3 = input("Pilih produk (1-5): ").strip()
                
                produk = ""
                if not pilih_produk3:
                    print("Masukkan pilihan!")
                    input("tekan enter untuk kembali")
                    jenis_produk(username)

            
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
         elif search == "plastik" :
                os.system('cls')
                print('''
                =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                $$$$$$$$$^^^^^  Alat Panen dan Pascapanen    ^^^^^$$$$$$$$
                __________________ SELAMAT BERBELANJA ___________________
                ''')
                for i in list_jenisproduk3:
                    nama_produk, harga_produk, stok_produk = list_jenisproduk3[i]
                    print(f"{i}. {nama_produk} - Rp{harga_produk} - {stok_produk}")
                
                pilih_produk3 = input("Pilih produk (1-5): ").strip()

                produk = ""
                if not pilih_produk3:
                    print("Masukkan pilihan!")
                    input("tekan enter untuk kembali")
                    jenis_produk(username)
            
                elif pilih_produk3 == "1":
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
         elif search == "pupuk" or search == "benih" :
                os.system('cls')
                print('''
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            $$$$$$$$$^^^^^  Obat dan Perawatan Tanaman  ^^^^^$$$$$$$$
            __________________ SELAMAT BERBELANJA ___________________
            ''')
                for i in list_jenisproduk4:
                    nama_produk, harga_produk, stok_produk = list_jenisproduk4[i]
                    print(f"{i}. {nama_produk} - Rp{harga_produk} - {stok_produk}")
                
                pilih_produk4 = input("Pilih produk (1-5): ").strip()

                produk = ""
                if not pilih_produk4:
                    print("Masukkan pilihan!")
                    input("tekan enter untuk kembali")
                    jenis_produk(username)
            
                elif pilih_produk4 == "1":
                    produk = "Pupuk Organik"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Pupuk alami untuk meningkatkan kesuburan tanah
                    Spesifikasi: Berat: 1 kg, Bahan: Kompos organik
                    Harga: Rp 35.000''')
                elif pilih_produk4 == "2":
                    produk = "Pupuk Urea"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Pupuk kimia untuk mempercepat pertumbuhan tanaman
                    Spesifikasi: Berat: 2 kg, Kandungan: Nitrogen tinggi
                    Harga: Rp 100.000''')
                elif pilih_produk4 == "3":
                    produk = "Benih Sayuran (1 paket)"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Paket benih berkualitas untuk berbagai sayuran
                    Spesifikasi: Isi: 50 gram, Jenis: Aneka sayuran
                    Harga: Rp 20.000''')
                elif pilih_produk4 == "4":
                    produk = "Cocopeat"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Media tanam serbaguna dari serbuk kelapa
                    Spesifikasi: Berat: 1 kg, Material: Serbuk kelapa
                    Harga: Rp 25.000''')
                elif pilih_produk4 == "5":
                    produk = "Kapur Dolomit"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Bahan alami untuk menetralkan pH tanah
                    Spesifikasi: Berat: 1 kg, Material: Kapur murni
                    Harga: Rp 20.000''')

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
         elif search == "cocopeat" or search == "kapur" :
                os.system('cls')
                print('''
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            $$$$$$$$$^^^^^  Obat dan Perawatan Tanaman  ^^^^^$$$$$$$$
            __________________ SELAMAT BERBELANJA ___________________
            ''')
                for i in list_jenisproduk4:
                    nama_produk, harga_produk, stok_produk = list_jenisproduk4[i]
                    print(f"{i}. {nama_produk} - Rp{harga_produk} - {stok_produk}")
                    
                pilih_produk4 = input("Pilih produk (1-5): ").strip()
                
                produk = ""
                if not pilih_produk4:
                    print("Masukkan pilihan!")
                    input("tekan enter untuk kembali")
                    jenis_produk(username)
            
                elif pilih_produk4 == "1":
                    produk = "Pupuk Organik"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Pupuk alami untuk meningkatkan kesuburan tanah
                    Spesifikasi: Berat: 1 kg, Bahan: Kompos organik
                    Harga: Rp 35.000''')
                elif pilih_produk4 == "2":
                    produk = "Pupuk Urea"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Pupuk kimia untuk mempercepat pertumbuhan tanaman
                    Spesifikasi: Berat: 2 kg, Kandungan: Nitrogen tinggi
                    Harga: Rp 100.000''')
                elif pilih_produk4 == "3":
                    produk = "Benih Sayuran (1 paket)"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Paket benih berkualitas untuk berbagai sayuran
                    Spesifikasi: Isi: 50 gram, Jenis: Aneka sayuran
                    Harga: Rp 20.000''')
                elif pilih_produk4 == "4":
                    produk = "Cocopeat"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Media tanam serbaguna dari serbuk kelapa
                    Spesifikasi: Berat: 1 kg, Material: Serbuk kelapa
                    Harga: Rp 25.000''')
                elif pilih_produk4 == "5":
                    produk = "Kapur Dolomit"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Bahan alami untuk menetralkan pH tanah
                    Spesifikasi: Berat: 1 kg, Material: Kapur murni
                    Harga: Rp 20.000''')

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
            
         elif search == "pestisida" or search == "fungisida" :
                os.system('cls')
                print('''
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        $$$$$$$$$^^^^^  Obat dan Perawatan Tanaman  ^^^^^$$$$$$$$
        __________________ SELAMAT BERBELANJA ___________________
        ''')
                for i in list_jenisproduk5:
                    nama_produk, harga_produk, stok_produk = list_jenisproduk5[i]
                    print(f"{i}. {nama_produk} - Rp{harga_produk} - {stok_produk}")
                
                pilih_produk5 = input("Pilih produk (1-5): ").strip()
                
                produk = ""
                if not pilih_produk5:
                    print("Masukkan pilihan!")
                    input("tekan enter untuk kembali")
                    jenis_produk(username)
            
                elif pilih_produk5 == "1":
                    produk = "Pestisida Organik"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Pestisida alami untuk mengendalikan hama pada tanaman
                    Spesifikasi: Kandungan: Ekstrak tumbuhan, Volume: 500 ml
                    Harga: Rp 60.000''')
                elif pilih_produk5 == "2":
                    produk = "Fungisida Cair"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Obat cair efektif untuk mencegah jamur pada tanaman
                    Spesifikasi: Volume: 500 ml, Kandungan: Fungisida alami
                    Harga: Rp 40.000''')
                elif pilih_produk5 == "3":
                    produk = "Insektisida"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Produk kimia untuk mengatasi serangga pengganggu
                    Spesifikasi: Kandungan: Insektisida sintetik, Volume: 250 ml
                    Harga: Rp 50.000''')
                elif pilih_produk5 == "4":
                    produk = "Herbisida"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Pengendali gulma yang efektif untuk melindungi tanaman
                    Spesifikasi: Volume: 500 ml, Kandungan: Herbisida sistemik
                    Harga: Rp 45.000''')
                elif pilih_produk5 == "5":
                    produk = "ZPT (Zat Pengatur Tumbuh)"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Larutan untuk merangsang pertumbuhan tanaman
                    Spesifikasi: Volume: 100 ml, Kandungan: ZPT alami
                    Harga: Rp 35.000''')

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
         elif search == "insektisida" or search == "herbisida" :
                os.system('cls')
                print('''
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            $$$$$$$$$^^^^^  Obat dan Perawatan Tanaman  ^^^^^$$$$$$$$
            __________________ SELAMAT BERBELANJA ___________________
            ''')
                for i in list_jenisproduk5:
                    nama_produk, harga_produk, stok_produk = list_jenisproduk5[i]
                    print(f"{i}. {nama_produk} - Rp{harga_produk} - {stok_produk}")
                
                pilih_produk5 = input("Pilih produk (1-5): ").strip()
                
                produk = ""
                if not pilih_produk5:
                    print("Masukkan pilihan!")
                    input("tekan enter untuk kembali")
                    jenis_produk(username)
            
                elif pilih_produk5 == "1":
                    produk = "Pestisida Organik"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Pestisida alami untuk mengendalikan hama pada tanaman
                    Spesifikasi: Kandungan: Ekstrak tumbuhan, Volume: 500 ml
                    Harga: Rp 60.000''')
                elif pilih_produk5 == "2":
                    produk = "Fungisida Cair"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Obat cair efektif untuk mencegah jamur pada tanaman
                    Spesifikasi: Volume: 500 ml, Kandungan: Fungisida alami
                    Harga: Rp 40.000''')
                elif pilih_produk5 == "3":
                    produk = "Insektisida"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Produk kimia untuk mengatasi serangga pengganggu
                    Spesifikasi: Kandungan: Insektisida sintetik, Volume: 250 ml
                    Harga: Rp 50.000''')
                elif pilih_produk5 == "4":
                    produk = "Herbisida"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Pengendali gulma yang efektif untuk melindungi tanaman
                    Spesifikasi: Volume: 500 ml, Kandungan: Herbisida sistemik
                    Harga: Rp 45.000''')
                elif pilih_produk5 == "5":
                    produk = "ZPT (Zat Pengatur Tumbuh)"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Larutan untuk merangsang pertumbuhan tanaman
                    Spesifikasi: Volume: 100 ml, Kandungan: ZPT alami
                    Harga: Rp 35.000''')

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
         elif search == "zpt":
                os.system('cls')
                print('''
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            $$$$$$$$$^^^^^  Obat dan Perawatan Tanaman  ^^^^^$$$$$$$$
            __________________ SELAMAT BERBELANJA ___________________
            ''')
                for i in list_jenisproduk5:
                    nama_produk, harga_produk, stok_produk = list_jenisproduk5[i]
                    print(f"{i}. {nama_produk} - Rp{harga_produk} - {stok_produk}")
                    
                pilih_produk5 = input("Pilih produk (1-5): ").strip()
                
                produk = ""
                if not pilih_produk5:
                    print("Masukkan pilihan!")
                    input("tekan enter untuk kembali")
                    jenis_produk(username)
            
                elif pilih_produk5 == "1":
                    produk = "Pestisida Organik"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Pestisida alami untuk mengendalikan hama pada tanaman
                    Spesifikasi: Kandungan: Ekstrak tumbuhan, Volume: 500 ml
                    Harga: Rp 60.000''')
                elif pilih_produk5 == "2":
                    produk = "Fungisida Cair"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Obat cair efektif untuk mencegah jamur pada tanaman
                    Spesifikasi: Volume: 500 ml, Kandungan: Fungisida alami
                    Harga: Rp 40.000''')
                elif pilih_produk5 == "3":
                    produk = "Insektisida"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Produk kimia untuk mengatasi serangga pengganggu
                    Spesifikasi: Kandungan: Insektisida sintetik, Volume: 250 ml
                    Harga: Rp 50.000''')
                elif pilih_produk5 == "4":
                    produk = "Herbisida"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Pengendali gulma yang efektif untuk melindungi tanaman
                    Spesifikasi: Volume: 500 ml, Kandungan: Herbisida sistemik
                    Harga: Rp 45.000''')
                elif pilih_produk5 == "5":
                    produk = "ZPT (Zat Pengatur Tumbuh)"
                    print("\nDetail Produk: ")
                    print('''
                    Deskripsi: Larutan untuk merangsang pertumbuhan tanaman
                    Spesifikasi: Volume: 100 ml, Kandungan: ZPT alami
                    Harga: Rp 35.000''')

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
            
    elif jenis == '4':
            os.system('cls')
            print('''
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            $$$$$$$$$^^^^^  Obat dan Perawatan Tanaman  ^^^^^$$$$$$$$
            __________________ SELAMAT BERBELANJA ___________________
            ''')
            for i in list_jenisproduk4:
                nama_produk, harga_produk, stok_produk = list_jenisproduk4[i]
                print(f"{i}. {nama_produk} - Rp{harga_produk} - {stok_produk}")
            
            pilih_produk4 = input("Pilih produk (1-5): ").strip()
            
            produk = ""
            if not pilih_produk4:
                    print("Masukkan pilihan!")
                    input("tekan enter untuk kembali")
                    jenis_produk(username)
        
            elif pilih_produk4 == "1":
                produk = "Pupuk Organik"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Pupuk alami untuk meningkatkan kesuburan tanah
                Spesifikasi: Berat: 1 kg, Bahan: Kompos organik
                Harga: Rp 35.000''')
            elif pilih_produk4 == "2":
                produk = "Pupuk Urea"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Pupuk kimia untuk mempercepat pertumbuhan tanaman
                Spesifikasi: Berat: 2 kg, Kandungan: Nitrogen tinggi
                Harga: Rp 100.000''')
            elif pilih_produk4 == "3":
                produk = "Benih Sayuran (1 paket)"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Paket benih berkualitas untuk berbagai sayuran
                Spesifikasi: Isi: 50 gram, Jenis: Aneka sayuran
                Harga: Rp 20.000''')
            elif pilih_produk4 == "4":
                produk = "Cocopeat"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Media tanam serbaguna dari serbuk kelapa
                Spesifikasi: Berat: 1 kg, Material: Serbuk kelapa
                Harga: Rp 25.000''')
            elif pilih_produk4 == "5":
                produk = "Kapur Dolomit"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Bahan alami untuk menetralkan pH tanah
                Spesifikasi: Berat: 1 kg, Material: Kapur murni
                Harga: Rp 20.000''')

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
            os.system('cls')
            print('''
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            $$$$$$$$$^^^^^  Obat dan Perawatan Tanaman  ^^^^^$$$$$$$$
            __________________ SELAMAT BERBELANJA ___________________
            ''')
            for i in list_jenisproduk5:
                nama_produk, harga_produk, stok_produk = list_jenisproduk5[i]
                print(f"{i}. {nama_produk} - Rp{harga_produk} - {stok_produk}")
            
            pilih_produk5 = input("Pilih produk (1-5): ").strip()
            
            produk = ""
            if not pilih_produk5:
                    print("Masukkan pilihan!")
                    input("tekan enter untuk kembali")
                    jenis_produk(username)
        
            elif pilih_produk5 == "1":
                produk = "Pestisida Organik"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Pestisida alami untuk mengendalikan hama pada tanaman
                Spesifikasi: Kandungan: Ekstrak tumbuhan, Volume: 500 ml
                Harga: Rp 60.000''')
            elif pilih_produk5 == "2":
                produk = "Fungisida Cair"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Obat cair efektif untuk mencegah jamur pada tanaman
                Spesifikasi: Volume: 500 ml, Kandungan: Fungisida alami
                Harga: Rp 40.000''')
            elif pilih_produk5 == "3":
                produk = "Insektisida"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Produk kimia untuk mengatasi serangga pengganggu
                Spesifikasi: Kandungan: Insektisida sintetik, Volume: 250 ml
                Harga: Rp 50.000''')
            elif pilih_produk5 == "4":
                produk = "Herbisida"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Pengendali gulma yang efektif untuk melindungi tanaman
                Spesifikasi: Volume: 500 ml, Kandungan: Herbisida sistemik
                Harga: Rp 45.000''')
            elif pilih_produk5 == "5":
                produk = "ZPT (Zat Pengatur Tumbuh)"
                print("\nDetail Produk: ")
                print('''
                Deskripsi: Larutan untuk merangsang pertumbuhan tanaman
                Spesifikasi: Volume: 100 ml, Kandungan: ZPT alami
                Harga: Rp 35.000''')

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
    elif jenis == '7':
        home()
           

def keranjang(username, produk, harga):
    try:
        # User input for quantity
        jumlah = int(input(f"Masukkan jumlah {produk}: "))
        total_harga = harga * jumlah

        # Define the cart file path
        keranjang_file = 'keranjangTRIJAYA.csv'

        # Read the cart (keranjang) CSV file or create a new one if not exists
        if os.path.isfile(keranjang_file):
            data_keranjang = pd.read_csv(keranjang_file)
        else:
            header = ["username", "produk", "harga", "jumlah", "total", "stok"]
            data_keranjang = pd.DataFrame(columns=header)

        # Check if product already in the cart for the user
        produk_ada = data_keranjang[(data_keranjang["username"] == username) & (data_keranjang["produk"] == produk)]
        
        if not produk_ada.empty:
            # If product already in the cart, update its quantity and total
            data_keranjang.loc[produk_ada.index, "jumlah"] += jumlah
            data_keranjang.loc[produk_ada.index, "total"] = data_keranjang.loc[produk_ada.index, "harga"] * data_keranjang.loc[produk_ada.index, "jumlah"]
        else:
            # If product not in cart, add a new row to the cart
            new_row = {
                "username": username,
                "produk": produk,
                "harga": harga,
                "jumlah": jumlah,
                "total": total_harga,
                "stok": 0  # This can be updated later
            }
            data_keranjang = data_keranjang.append(new_row, ignore_index=True)

        # Define the product file path (you can specify your product CSV here)
        produk_file = 'list_jenisproduk2.csv'

        # Read the product CSV file
        produk_data = pd.read_csv(produk_file)

        # Check if the product exists in the product CSV
        produk_info = produk_data[produk_data['Nama Produk'] == produk]
        if not produk_info.empty:
            stok_terbaru = produk_info['Stok'].values[0] - jumlah
            if stok_terbaru < 0:
                print("Stok tidak cukup!")
                return
            # Update the stock in the product file
            produk_data.loc[produk_data['Nama Produk'] == produk, 'Stok'] = stok_terbaru
            produk_data.to_csv(produk_file, index=False)
        else:
            print("Produk tidak ditemukan!")
            return

        # Save the updated cart data to CSV
        data_keranjang.to_csv(keranjang_file, index=False)

        print(f"{produk} berhasil ditambahkan ke keranjang!\n")
        print('''  
            A. Tambahkan produk lagi
            B. Lanjutkan ke pembayaran
        ''')
        keranjang_beli = input("Pilih menu: ").strip().upper()

        if keranjang_beli == "A":
            jenis_produk(username)
        elif keranjang_beli == "B":
            ongkir = data_pengiriman()  # Make sure this function is defined
            pembayaran(username, ongkir)  # Make sure this function is defined
        else:
            print("Pilihan tidak tersedia. Kembali ke menu utama.")
            jenis_produk(username)

    except ValueError:
        print("Input jumlah produk tidak valid! Harap masukkan angka.")
        keranjang(username, produk, harga)

def pembayaran(username, ongkir):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Memproses pembayaran untuk {username}...\n")
    
    total_belanja = 0
    keranjang_user = {}

    print(f"Keranjang {username}:")
    print(f"{'Produk':<15} {'Harga':<10} {'Jumlah':<8} {'Total':<10}")
    print("-" * 50)

    try:
        with open('KeranjangTRIJAYA.csv', mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip the header
            
            for row in reader:
                if len(row) < 5:
                    print(f"Warning: Baris dengan data tidak lengkap ditemukan, akan dilewati: {row}")
                    continue  # Skip rows with missing data
                
                user, produk, harga, jumlah, total = row
                
                # Check if all required fields are present and numeric
                try:
                    if user == username:
                        harga = int(harga)  # Convert harga to integer
                        jumlah = int(jumlah)  # Convert jumlah to integer
                        total = int(total)  # Convert total to integer
                        
                        if produk in keranjang_user:
                            keranjang_user[produk]['jumlah'] += jumlah
                            keranjang_user[produk]['total'] += total
                        else:
                            keranjang_user[produk] = {
                                'harga': harga,
                                'jumlah': jumlah,
                                'total': total,
                            }
                except ValueError:
                    print(f"Error: Format data tidak valid untuk produk {produk}. Data dilewati.")
                    continue  # Skip rows with invalid numeric data

        # Print cart details and calculate total
        for produk, data in keranjang_user.items():
            print(f"{produk:<15} {data['harga']:<10} {data['jumlah']:<8} {data['total']:<10}")
            total_belanja += data['total']  # Add product total to total_belanja

        # Add ongkir (shipping fee) to the final total
        total_belanja += ongkir

    except FileNotFoundError:
        print("Keranjang kosong. Silakan tambahkan produk terlebih dahulu.")
        return
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return

    print("-" * 50)
    print(f"Total Belanja: Rp{total_belanja}")
    print('''  
    Pilih Metode Pembayaran:
    1. Bank Account
    ''')
    metode = input("Pilih metode pembayaran: ").strip()
    if metode == '1':
        bank_account(total_belanja)
    else:
        print("Metode pembayaran tidak valid.")
        pembayaran(username, ongkir)

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
        input("Masukkan nomor rekening Anda: ")
        print(f"Total yang harus dibayarkan: Rp{total_belanja}")
        print(f"Lakukan pembayaran ke rekening TRIJAYA: 2424101010.")
        input("Masukkan jumlah uang :")
        print("Pembayaran berhasil!")
        print('''
            A. Kembali ke menu utama
            B. Keluar
        ''')
        pilihan = input("Pilih menu: ").strip().upper()
        if pilihan == "A":
            kosongkan_keranjang()
            home() 
        elif pilihan == "B":
            print("Terima kasih telah berbelanja di TRIJAYA!")

            exit()
        else:
            print("Pilihan tidak valid. Mengakhiri program.")
            exit()
    else:
        print("Pilihan bank tidak valid.")
        bank_account(total_belanja)

def kosongkan_keranjang(username):
    data_baru = []
    try:
        with open('KeranjangTRIJAYA.csv', mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if row[0] != username:  
                    data_baru.append(row)
    except FileNotFoundError:
        print("File keranjang tidak ditemukan.")
        return
       
    with open('KeranjangTRIJAYA.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data_baru)
    print("Keranjang Anda telah dikosongkan.")
    jenis_produk(username)
    kosongkan_keranjang(username)


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
        
    
    with open('provinsi.csv', mode='r') as file:
        reader = csv.DictReader(file)
        provinsi_found = False  
        for row in reader:
            if row['provinsi'].lower() == provinsi_pembeli.lower():  
                provinsi_found = True
                ongkir = row['ongkir']
                print(f"Ongkir untuk wilayah {provinsi_pembeli} adalah {ongkir}!")
                return ongkir
                
    
        if not provinsi_found:
            print(f"Provinsi {provinsi_pembeli} tidak ditemukan dalam daftar.")
            return None
        
def main():
    home()
    
main()

     
                 