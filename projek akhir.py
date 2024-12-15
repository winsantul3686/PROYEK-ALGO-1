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

def home():
    os.system('cls') 
    print('''

        ████████╗██████╗░██╗░░░░░██╗░█████╗░██╗░░░██╗░█████╗░
        ╚══██╔══╝██╔══██╗██║░░░░░██║██╔══██╗╚██╗░██╔╝██╔══██╗
        ░░░██║░░░██████╔╝██║░░░░░██║███████║░╚████╔╝░███████║
        ░░░██║░░░██╔══██╗██║██╗░░██║██╔══██║░░╚██╔╝░░██╔══██║
        ░░░██║░░░██║░░██║██║╚█████╔╝██║░░██║░░░██║░░░██║░░██║
        ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝
        ''')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("                SELAMAT DATANG di TRIJAYA               ")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("""
        [1] Register
        [2] Login
        [3] Admin Login
        [4] Exit
    """)
    print("--------------------------------------------------------")
    
    home1 = input("Pilih fitur (1/2/3/4): ")
    if home1 == "1":
        register()
    elif home1 == "2":
        login()
    elif home1 == "3":
        login_admin()
    elif home1 == "4":
        print("Terima kasih telah menggunakan aplikasi TRIJAYA! Sampai jumpa.")
        exit ()
    else:
        print("Pilihan tidak tersedia, coba lagi.")
        input("Tekan enter untuk kembali!")
        home()  

def register():
    os.system('cls') 
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("                SELAMAT DATANG di TRIJAYA               ")
    print("______________________  REGISTER  ______________________")
    print (" ")
    
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

    if username in df['username'].values:
        print("Username sudah terdaftar. Silakan gunakan username lain.")
        input("klik enter untuk kembali")
        home()

    new_data = pd.DataFrame({'username': [username], 'password': [password]})
    new_data.to_csv('RegTRIJAYA.csv', mode='a', index=False, header=False)
    print("Registrasi berhasil! Selamat datang di TRIJAYA.")
    input("klik enter untuk kembali")
    home()

def login():
    os.system('cls')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("                SELAMAT DATANG di TRIJAYA               ")
    print("________________________ LOGIN _________________________")
    print(" ")

    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()

    try:
        df = pd.read_csv('RegTRIJAYA.csv')
    except FileNotFoundError:
        print("Data pengguna tidak ditemukan. Silakan daftar terlebih dahulu!")
        input("Tekan Enter untuk kembali...")
        home()

    matched_user = df[(df['username'] == username) & (df['password'] == password)]

    if not matched_user.empty:
        print(f"Login berhasil! Selamat datang, {username}.")
        jenis_produk(username) 
    else:
        print("Username atau password salah. Silakan coba lagi!")
        input("Tekan Enter untuk mencoba lagi...")
        home()
    

def login_admin():
    os.system('cls')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("                SELAMAT DATANG di TRIJAYA               ")
    print("______________________  ADMIN LOGIN  ___________________")
    print (" ")

    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()

    df = pd.read_csv('admin.csv')
    matched_admin = df[(df['username'] == username) & (df['password'] == password)]

    if not matched_admin.empty:
        menu_admin (username)
    else:
        print("Login gagal! Username atau password salah.")
        print("----------------------------------------------------------")
        input("Tekan Enter untuk mencoba lagi...")
        home ()
    
def menu_admin(username):
    os.system ("cls")
    print(f"Selamat datang, Admin {username}!")
    print("----------------------------------------------------------")
    print("1. Ubah Stok")
    print("2. Ubah harga")
    print("3. tambah produk")
    print("4. Hapus Produk")
    print("5. Ubah Nama")
    print("6. Kembali")
    pilih_admin = input("Masukkan pilihan: ")
    if pilih_admin == '1':
        ubah_stok(username)
    elif pilih_admin == '2':
        ubah_harga(username)
    elif pilih_admin == '3':
        tambah_produk(username)
    elif pilih_admin == '4':
        hapus_produk(username)
    elif pilih_admin == '5':
        ubah_nama(username)
    elif pilih_admin == "6":
        home ()
    else:
        print ("input salah")
        input ("tekan enter untuk kembali")
        menu_admin (username)
    
def hapus_produk(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n=-=-=-=-=-=-=-= HAPUS PRODUK =-=-=-=-=-=-=-=")

    kategori_dict = {
        "1": "list_jenisproduk1.csv",
        "2": "list_jenisproduk2.csv",
        "3": "list_jenisproduk3.csv",
        "4": "list_jenisproduk4.csv",
        "5": "list_jenisproduk5.csv"
    }

    print("\nKategori Produk:")
    print("1. Alat Tanam")
    print("2. Alat Perawatan")
    print("3. Alat Panen")
    print("4. Pupuk dan Media Tanam")
    print("5. Obat-Obatan dan ZPT")

    kategori = input("\nMasukkan nomor kategori produk yang ingin dihapus: ").strip()

    if kategori not in kategori_dict:
        print("Kategori tidak valid!")
        input("Tekan Enter untuk kembali.")
        menu_admin (username)

    file_path = kategori_dict[kategori]

    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan!")
        input("Tekan Enter untuk kembali.")
        hapus_produk(username)
   
    if df.empty:
        print("Daftar produk kosong! Tidak ada yang bisa dihapus.")
        input("Tekan Enter untuk kembali.")
        hapus_produk (username)

    print("\nDaftar Produk:")
    print("+-----+---------------------------+--------------+----------+")
    print("| ID  | Nama Produk               | Harga (Rp)   | Stok     |")
    print("+-----+---------------------------+--------------+----------+")
    for _, row in df.iterrows():
        print(f"| {row['ID']:<3} | {row['Nama_Produk']:<25} | Rp{row['Harga']:>10,} | {row['Stok']:>8} |")
    print("+-----+---------------------------+--------------+----------+")

    try:
        id_produk = int(input("Masukkan ID produk yang ingin dihapus: ").strip())
        if id_produk not in df["ID"].values:
            print(f"ID produk {id_produk} tidak ditemukan!")
            input("Tekan Enter untuk kembali.")
            hapus_produk (username)

        konfirmasi = input("Apakah Anda yakin ingin menghapus produk ini? (y/n): ").strip().lower()
        if konfirmasi == 'n':
            print("Penghapusan dibatalkan.")
            input("Tekan Enter untuk kembali.")
            menu_admin (username)

        elif konfirmasi != "y":
            print ("Pilihan tidak tersedia")
            input ("Tekan Enter untuk kembali.")
            hapus_produk (username)

        df = df[df["ID"] != id_produk]

        df.reset_index(drop=True, inplace=True)
        df["ID"] = df.index + 1

        df.to_csv(file_path, index=False)
        print(f"\nProduk dengan ID {id_produk} berhasil dihapus.")
        input("Tekan Enter untuk kembali.")
        menu_admin (username)
    except ValueError:
        print("Input tidak valid! ID produk harus berupa angka.")
        input("Tekan Enter untuk kembali.")
        hapus_produk (username)

def tambah_produk(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n=-=-=-=-=-=-=-= TAMBAH PRODUK BARU =-=-=-=-=-=-=-=")

    kategori_dict = {
        "1": "list_jenisproduk1.csv",
        "2": "list_jenisproduk2.csv",
        "3": "list_jenisproduk3.csv",
        "4": "list_jenisproduk4.csv",
        "5": "list_jenisproduk5.csv"
    }

    print("\nKategori Produk:")
    print("1. Alat Tanam")
    print("2. Alat Perawatan")
    print("3. Alat Panen")
    print("4. Pupuk dan Media Tanam")
    print("5. Obat-Obatan dan ZPT")

    kategori = input("\nMasukkan nomor kategori produk yang ingin ditambahkan: ").strip()

    if kategori not in kategori_dict:
        print("Kategori tidak valid!")
        input("Tekan Enter untuk kembali.")
        menu_admin (username)

    file_path = kategori_dict[kategori]

    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan!")
        input("Tekan Enter untuk kembali.")
        return

    try:
        print("\nMasukkan detail produk baru:")
        nama_produk = input("Nama Produk: ").strip()
        if not nama_produk:
            print("Nama produk tidak boleh kosong!")
            tambah_produk (username)

        harga_produk = int(input("Harga Produk (Rp): "))
        stok_produk = int(input("Stok Produk: "))
        des_produk = input ("Masukkan Deskripsi Produk: ")
        spek_produk = input ("Masukkan Spek Produk: ")

        if not df.empty:
            id_produk = df["ID"].max() + 1
        else:
            id_produk = 1

        df.loc[len(df)] = [id_produk, nama_produk, harga_produk, stok_produk, des_produk, spek_produk]

        df.to_csv(file_path, index=False)
        print(f"\nProduk '{nama_produk}' berhasil ditambahkan dengan ID {id_produk}.")
        input("Tekan Enter untuk kembali.")
        menu_admin (username)
    except ValueError:
        print("Input tidak valid! Harga dan stok harus berupa angka.")
        input("Tekan Enter untuk kembali.")
        tambah_produk (username)

def ubah_nama(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n=-=-=-=-=-=-=-= UBAH HARGA PRODUK =-=-=-=-=-=-=-=")

    kategori_dict = {
        "1": "list_jenisproduk1.csv",
        "2": "list_jenisproduk2.csv",
        "3": "list_jenisproduk3.csv",
        "4": "list_jenisproduk4.csv",
        "5": "list_jenisproduk5.csv"
    }

    print("\nKategori Produk:")
    print("1. Alat Tanam")
    print("2. Alat Perawatan")
    print("3. Alat Panen")
    print("4. Pupuk dan Media Tanam")
    print("5. Obat-Obatan dan ZPT")

    kategori = input("\nMasukkan nomor kategori produk yang ingin diubah: ").strip()

    if kategori not in kategori_dict:
        print("Kategori tidak valid!")
        input("Tekan Enter untuk kembali.")
        menu_admin (username)

    file_path = kategori_dict[kategori]

    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan!")
        input("Tekan Enter untuk kembali.")
        return 

    print("\nProduk dalam kategori:")
    print("+-----+---------------------------+--------------+----------+")
    print("| ID  | Nama Produk               | Harga (Rp)   | Stok     |")
    print("+-----+---------------------------+--------------+----------+")
    for _, row in df.iterrows():
        print(f"| {row['ID']:<3} | {row['Nama_Produk']:<25} | Rp{row['Harga']:>10,} | {row['Stok']:>8} |")
    print("+-----+---------------------------+--------------+----------+")

    produk_id = input("\nMasukkan ID produk yang ingin diubah: ").strip()

    if not produk_id.isdigit() or int(produk_id) not in df["ID"].values:
        print("ID produk tidak valid!")
        input("Tekan Enter untuk kembali.")
        ubah_nama (username)

    try:
        nama_baru = (input(f"Masukkan nama baru untuk produk '{df[df['ID'] == int(produk_id)]['Nama_Produk'].values[0]}': "))
    except ValueError:
        print("Input tidak valid! Stok harus berupa angka.")
        input("Tekan Enter untuk kembali.")
        ubah_nama (username)

    df.loc[df["ID"] == int(produk_id), "Nama_Produk"] = nama_baru

    df.to_csv(file_path, index=False)
    print(f"Nama untuk produk dengan ID {produk_id} berhasil diperbarui menjadi {nama_baru}.")
    input("Tekan Enter untuk kembali.")
    menu_admin (username)

def ubah_harga(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n=-=-=-=-=-=-=-= UBAH HARGA PRODUK =-=-=-=-=-=-=-=")

    kategori_dict = {
        "1": "list_jenisproduk1.csv",
        "2": "list_jenisproduk2.csv",
        "3": "list_jenisproduk3.csv",
        "4": "list_jenisproduk4.csv",
        "5": "list_jenisproduk5.csv"
    }

    print("\nKategori Produk:")
    print("1. Alat Tanam")
    print("2. Alat Perawatan")
    print("3. Alat Panen")
    print("4. Pupuk dan Media Tanam")
    print("5. Obat-Obatan dan ZPT")

    kategori = input("\nMasukkan nomor kategori produk yang ingin diubah: ").strip()

    if kategori not in kategori_dict:
        print("Kategori tidak valid!")
        input("Tekan Enter untuk kembali.")
        menu_admin (username)

    file_path = kategori_dict[kategori]

    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan!")
        input("Tekan Enter untuk kembali.")
        return 

    print("\nProduk dalam kategori:")
    print("+-----+---------------------------+--------------+----------+")
    print("| ID  | Nama Produk               | Harga (Rp)   | Stok     |")
    print("+-----+---------------------------+--------------+----------+")
    for _, row in df.iterrows():
        print(f"| {row['ID']:<3} | {row['Nama_Produk']:<25} | Rp{row['Harga']:>10,} | {row['Stok']:>8} |")
    print("+-----+---------------------------+--------------+----------+")

    produk_id = input("\nMasukkan ID produk yang ingin diubah: ").strip()

    if not produk_id.isdigit() or int(produk_id) not in df["ID"].values:
        print("ID produk tidak valid!")
        input("Tekan Enter untuk kembali.")
        ubah_harga (username)

    try:
        harga_baru = int(input(f"Masukkan harga baru untuk produk '{df[df['ID'] == int(produk_id)]['Harga'].values[0]}': "))
    except ValueError:
        print("Input tidak valid! Stok harus berupa angka.")
        input("Tekan Enter untuk kembali.")
        ubah_harga (username)

    df.loc[df["ID"] == int(produk_id), "Harga"] = harga_baru

    df.to_csv(file_path, index=False)
    print(f"Harga untuk produk dengan ID {produk_id} berhasil diperbarui menjadi {harga_baru}.")
    input("Tekan Enter untuk kembali.")
    menu_admin (username) 

def ubah_stok(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n=-=-=-=-=-=-=-= UBAH STOK PRODUK =-=-=-=-=-=-=-=")

    kategori_dict = {
        "1": "list_jenisproduk1.csv",
        "2": "list_jenisproduk2.csv",
        "3": "list_jenisproduk3.csv",
        "4": "list_jenisproduk4.csv",
        "5": "list_jenisproduk5.csv"
    }

    print("\nKategori Produk:")
    print("1. Alat Tanam")
    print("2. Alat Perawatan")
    print("3. Alat Panen")
    print("4. Pupuk dan Media Tanam")
    print("5. Obat-Obatan dan ZPT")

    kategori = input("\nMasukkan nomor kategori produk yang ingin diubah: ").strip()

    if kategori not in kategori_dict:
        print("Kategori tidak valid!")
        input("Tekan Enter untuk kembali.")
        menu_admin (username)

    file_path = kategori_dict[kategori]
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan!")
        input("Tekan Enter untuk kembali.")
        return 

    print("\nProduk dalam kategori:")
    print("+-----+---------------------------+--------------+----------+")
    print("| ID  | Nama Produk               | Harga (Rp)   | Stok     |")
    print("+-----+---------------------------+--------------+----------+")
    for _, row in df.iterrows():
        print(f"| {row['ID']:<3} | {row['Nama_Produk']:<25} | Rp{row['Harga']:>10,} | {row['Stok']:>8} |")
    print("+-----+---------------------------+--------------+----------+")

    produk_id = input("\nMasukkan ID produk yang ingin diubah: ").strip()

    if not produk_id.isdigit() or int(produk_id) not in df["ID"].values:
        print("ID produk tidak valid!")
        input("Tekan Enter untuk kembali.")
        ubah_stok (username)

    try:
        stok_baru = int(input(f"Masukkan stok baru untuk produk '{df[df['ID'] == int(produk_id)]['Nama_Produk'].values[0]}': "))
    except ValueError:
        print("Input tidak valid! Stok harus berupa angka.")
        input("Tekan Enter untuk kembali.")
        ubah_stok (username)

    df.loc[df["ID"] == int(produk_id), "Stok"] = stok_baru

    df.to_csv(file_path, index=False)
    print(f"Stok untuk produk dengan ID {produk_id} berhasil diperbarui menjadi {stok_baru}.")
    input("Tekan Enter untuk kembali.")
    menu_admin (username)

def data_pengiriman():
    os.system('cls')
    print("======= DATA PENGIRIMAN =======")
    nama_pembeli = input ("Masukkan Nama: ")
    if not nama_pembeli:
        input ("nama harus di isi!")
        data_pengiriman ()

    alamat_pembeli = input ("Masukkan Alamat: ")
    if not alamat_pembeli:
        input ("Alamat harus di isi!")
        data_pengiriman ()

    provinsi_pembeli = input ("Masukkan Provinsi: ")
    if not provinsi_pembeli:
        input ("Provinsi harus di isi cth: Bali")
        data_pengiriman ()
    
    no_pembeli = input ("Masukkan Nomor HP: ")
    if not no_pembeli:
        input ("nomor harus di isi!") 
        data_pengiriman ()

    try:
        df = pd.read_csv('provinsi.csv')
    except FileNotFoundError:
        print("Error: File provinsi.csv tidak ditemukan.")
        input("Klik Enter untuk keluar.")
        return
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        input("Klik Enter untuk keluar.")
        return

    try:
        sama_provinsi = df[df['provinsi'].str.lower() == provinsi_pembeli.lower()]
        if sama_provinsi.empty:
            print(f"Provinsi {provinsi_pembeli} tidak ditemukan dalam daftar.")
            input("Klik Enter untuk mengisi data kembali.")
            return data_pengiriman()
        # else:
        #     ongkir = sama_provinsi['ongkir'].values[0]
        #     print(f"Ongkir untuk wilayah {provinsi_pembeli} adalah {ongkir}.")
    except KeyError as e:
        print(f"Kolom tidak ditemukan dalam file: {e}")
        input("Klik Enter untuk keluar.")
        data_pengiriman ()

    print ('''
    PILIH OPSI KURIR:
    1. JNE
    2. SiCepat Express
    3. JNT
    4. Trijaya Express
           ''')
    kurir = input ("Pilih Opsi Kurir: ")
    if kurir == "1":
        os.system('cls')
        print ("Pengriman Menggunakan JNE, dengan nama", nama_pembeli ,)
        # print ("Provinsi: ", provinsi_pembeli)
        # print ("Alamat: ", alamat_pembeli)
        # print ("Nomor HP: ", no_pembeli)

    elif kurir == "2":
        os.system ('cls')
        print ("Pengriman Menggunakan SiCepat Express, dengan nama", nama_pembeli ,)
        # print ("Provinsi: ", provinsi_pembeli)
        # print ("Alamat: ", alamat_pembeli)
        # print ("Nomor HP: ", no_pembeli)
    
    elif kurir == "3":
        os.system ("cls")
        print ("Pengriman Menggunakan JNT, dengan nama", nama_pembeli ,)
        # print ("Provinsi: ", provinsi_pembeli)
        # print ("Alamat: ", alamat_pembeli)
        # print ("Nomor HP: ", no_pembeli)
    
    elif kurir == "4":
        os.system('cls')
        print ("Pengriman Menggunakan Trijaya Express, dengan nama", nama_pembeli ,)
        # print ("Provinsi: ", provinsi_pembeli)
        # print ("Alamat: ", alamat_pembeli)
        # print ("Nomor HP: ", no_pembeli)

    elif not os.path.isfile('provinsi.csv'): 
        print("Wilayah Tidak Tersedia!.")
        return None
    
    print ("Provinsi: ", provinsi_pembeli)
    print ("Alamat: ", alamat_pembeli)
    print ("Nomor HP: ", no_pembeli)

    # df = pd.read_csv('provinsi.csv')
    sama_provinsi = df[df['provinsi'].str.lower() == provinsi_pembeli.lower()]

    if not sama_provinsi.empty:
        ongkir = sama_provinsi['ongkir'].values[0] 
        print(f"Ongkir untuk wilayah {provinsi_pembeli} adalah {ongkir}!")
        return ongkir
    # else:
    #     print(f"Provinsi {provinsi_pembeli} tidak ditemukan dalam daftar.")
    #     input("klik enter untuk mengisi data kembali")

def jenis_produk(username):
    os.system('cls')
    print(f"Selamat datang, silahkan pilih jenis produk : ")
    print("+-----+--------------------------------------+")
    print("| No  | Nama Produk                          |")
    print("+-----+--------------------------------------+")
    for i in list_jenisproduk:
        print(f"| {i:<3} | {list_jenisproduk[i]:<36} |")
    print("+-----+--------------------------------------+")
    print(" ")

    jenis = input("Pilihlah jenis produk (1/2/3/4/5/6/7): ")

    if not jenis:
        print("Masukkan pilihan!")
        input("Tekan enter untuk kembali")
        jenis_produk(username)

    elif jenis == '1':
        os.system('cls')
        file_path = "list_jenisproduk1.csv"
        df = pd.read_csv(file_path)
        print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|")
        print("|                 SELAMAT DATANG di TRIJAYA                 |")
        print("|_______________________ Alat tanam ________________________|")
        print("|___________________ dan Persiapan lahan ___________________|")
        print("+-----+---------------------------+--------------+----------+")
        print("| No  | Nama Produk               | Harga (Rp)   | Stok     |")
        print("+-----+---------------------------+--------------+----------+")
        for index, row in df.iterrows():
            id_produk = row["ID"]
            nama_produk = row["Nama_Produk"]
            harga_produk = row["Harga"]
            stok_produk = row["Stok"]
            print(f"| {id_produk:<3} | {nama_produk:<25} | Rp{harga_produk:>10,} | {stok_produk:>8} |")
        print("+-----+---------------------------+--------------+----------+")

        pilih_produk1 = input("Pilih produk (masukkan nomor ID): ").strip()

        if not pilih_produk1.isdigit() or int(pilih_produk1) not in df["ID"].values:
            print("Pilihan tidak tersedia!")
            input("Tekan Enter untuk kembali.")
            jenis_produk(username)
            return

        produk_row = df[df["ID"] == int(pilih_produk1)].iloc[0]
        produk = produk_row["Nama_Produk"]
        harga = produk_row["Harga"]
        stok = produk_row["Stok"]
        deskripsi = produk_row["Deskripsi"]
        spek = produk_row["Spesifikasi"]
        print(f"\nDetail Produk: {produk}")
        print(f"{deskripsi} | {spek}")
        print(f"Harga: Rp {harga:,}")
        print(f"Stok: {stok}")
        print('''
        A. Masukkan keranjang
        B. Beli dan bayar
        ''')
        keranjang_beli = input("Pilih menu: ").strip().upper()
        if keranjang_beli == "A":
            keranjang(username, produk, harga, stok)
        elif keranjang_beli == "B":
            keranjang(username, produk, harga, stok)
            input("lanjut pembayaran...")
            pembayaran(username)
        else:
            print("Pilihan tidak tersedia. Kembali ke menu.")
            jenis_produk(username)

    elif jenis == '2':
        os.system('cls')
        file_path = "list_jenisproduk2.csv"  
        df = pd.read_csv(file_path)
        print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|")
        print("|                 SELAMAT DATANG di TRIJAYA                 |")
        print("|________________ Alat Pemeliharaan Tanaman ________________|")
        print("+-----+---------------------------+--------------+----------+")
        print("| No  | Nama Produk               | Harga (Rp)   | Stok     |")
        print("+-----+---------------------------+--------------+----------+")
        for index, row in df.iterrows():
            id_produk = row["ID"]
            nama_produk = row["Nama_Produk"]
            harga_produk = row["Harga"]
            stok_produk = row["Stok"]
            print(f"| {id_produk:<3} | {nama_produk:<25} | Rp{harga_produk:>10,} | {stok_produk:>8} |")
        print("+-----+---------------------------+--------------+----------+")

        pilih_produk2 = input("Pilih produk (masukkan nomor ID): ").strip()

        if not pilih_produk2.isdigit() or int(pilih_produk2) not in df["ID"].values:
            print("Pilihan tidak tersedia!")
            input("Tekan Enter untuk kembali.")
            jenis_produk(username)
            return

        produk_row = df[df["ID"] == int(pilih_produk2)].iloc[0]
        produk = produk_row["Nama_Produk"]
        harga = produk_row["Harga"]
        stok = produk_row["Stok"]
        deskripsi = produk_row["Deskripsi"]
        spek = produk_row["Spesifikasi"]
        print(f"\nDetail Produk: {produk}")
        print(f"{deskripsi} | {spek}")
        print(f"Harga: Rp {harga:,}")
        print(f"Stok: {stok}")
        print('''
        A. Masukkan keranjang
        B. Beli dan bayar
        ''')
        keranjang_beli = input("Pilih menu: ").strip().upper()
        if keranjang_beli == "A":
            keranjang(username, produk, harga, stok)
        elif keranjang_beli == "B":
            keranjang(username, produk, harga, stok)
            pembayaran(username)
        else:
            print("Pilihan tidak tersedia. Kembali ke menu.")
            jenis_produk(username)

    elif jenis == '3':
        os.system('cls')
        file_path = "list_jenisproduk3.csv"  
        df = pd.read_csv(file_path)
        print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|")
        print("|                 SELAMAT DATANG di TRIJAYA                 |")
        print("|________________ Alat Panen dan Pascapanen ________________|")
        print("+-----+---------------------------+--------------+----------+")
        print("| No  | Nama Produk               | Harga (Rp)   | Stok     |")
        print("+-----+---------------------------+--------------+----------+")
        for index, row in df.iterrows():
            id_produk = row["ID"]
            nama_produk = row["Nama_Produk"]
            harga_produk = row["Harga"]
            stok_produk = row["Stok"]
            print(f"| {id_produk:<3} | {nama_produk:<25} | Rp{harga_produk:>10,} | {stok_produk:>8} |")
        print("+-----+---------------------------+--------------+----------+")

        pilih_produk3 = input("Pilih produk (masukkan nomor ID): ").strip()

        if not pilih_produk3.isdigit() or int(pilih_produk3) not in df["ID"].values:
            print("Pilihan tidak tersedia!")
            input("Tekan Enter untuk kembali.")
            jenis_produk(username)
            return

        produk_row = df[df["ID"] == int(pilih_produk3)].iloc[0]
        produk = produk_row["Nama_Produk"]
        harga = produk_row["Harga"]
        stok = produk_row["Stok"]
        deskripsi = produk_row["Deskripsi"]
        spek = produk_row["Spesifikasi"]
        print(f"\nDetail Produk: {produk}")
        print(f"{deskripsi} | {spek}")
        print(f"Harga: Rp {harga:,}")
        print(f"Stok: {stok}")
        print('''
        A. Masukkan keranjang
        B. Beli dan bayar
        ''')
        keranjang_beli = input("Pilih menu: ").strip().upper()
        if keranjang_beli == "A":
            keranjang(username, produk, harga, stok)
        elif keranjang_beli == "B":
            keranjang(username, produk, harga, stok)
            pembayaran(username)
        else:
            print("Pilihan tidak tersedia. Kembali ke menu.")
            jenis_produk(username)

    elif jenis == '4':
        os.system('cls')
        file_path = "list_jenisproduk4.csv"  
        df = pd.read_csv(file_path)
        print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|")
        print("|                 SELAMAT DATANG di TRIJAYA                 |")
        print("|_____________________ Pupuk Dan Benih _____________________|")
        print("+-----+---------------------------+--------------+----------+")
        print("| No  | Nama Produk               | Harga (Rp)   | Stok     |")
        print("+-----+---------------------------+--------------+----------+")
        for index, row in df.iterrows():
            id_produk = row["ID"]
            nama_produk = row["Nama_Produk"]
            harga_produk = row["Harga"]
            stok_produk = row["Stok"]
            print(f"| {id_produk:<3} | {nama_produk:<25} | Rp{harga_produk:>10,} | {stok_produk:>8} |")
        print("+-----+---------------------------+--------------+----------+")

        pilih_produk4 = input("Pilih produk (masukkan nomor ID): ").strip()

        if not pilih_produk4.isdigit() or int(pilih_produk4) not in df["ID"].values:
            print("Pilihan tidak tersedia!")
            input("Tekan Enter untuk kembali.")
            jenis_produk(username)
            return

        produk_row = df[df["ID"] == int(pilih_produk4)].iloc[0]
        produk = produk_row["Nama_Produk"]
        harga = produk_row["Harga"]
        stok = produk_row["Stok"]
        deskripsi = produk_row["Deskripsi"]
        spek = produk_row["Spesifikasi"]
        print(f"\nDetail Produk: {produk}")
        print(f"{deskripsi} | {spek}")
        print(f"Harga: Rp {harga:,}")
        print(f"Stok: {stok}")
        print('''
        A. Masukkan keranjang
        B. Beli dan bayar
        ''')
        keranjang_beli = input("Pilih menu: ").strip().upper()
        if keranjang_beli == "A":
            keranjang(username, produk, harga, stok)
        elif keranjang_beli == "B":
            keranjang(username, produk, harga, stok)
            pembayaran(username)
        else:
            print("Pilihan tidak tersedia. Kembali ke menu.")
            jenis_produk(username)

    elif jenis == '5':
        os.system('cls')
        file_path = "list_jenisproduk5.csv" 
        df = pd.read_csv(file_path)
        print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|")
        print("|                 SELAMAT DATANG di TRIJAYA                 |")
        print("|________________ Obat dan Perawatan Tanaman _______________|")
        print("+-----+---------------------------+--------------+----------+")
        print("| No  | Nama Produk               | Harga (Rp)   | Stok     |")
        print("+-----+---------------------------+--------------+----------+")
        for index, row in df.iterrows():
            id_produk = row["ID"]
            nama_produk = row["Nama_Produk"]
            harga_produk = row["Harga"]
            stok_produk = row["Stok"]
            print(f"| {id_produk:<3} | {nama_produk:<25} | Rp{harga_produk:>10,} | {stok_produk:>8} |")
        print("+-----+---------------------------+--------------+----------+")

        pilih_produk5 = input("Pilih produk (masukkan nomor ID): ").strip()

        if not pilih_produk5.isdigit() or int(pilih_produk5) not in df["ID"].values:
            print("Pilihan tidak tersedia!")
            input("Tekan Enter untuk kembali.")
            jenis_produk(username)
            return

        produk_row = df[df["ID"] == int(pilih_produk5)].iloc[0]
        produk = produk_row["Nama_Produk"]
        harga = produk_row["Harga"]
        stok = produk_row["Stok"]
        deskripsi = produk_row["Deskripsi"]
        spek = produk_row["Spesifikasi"]
        print(f"\nDetail Produk: {produk}")
        print(f"{deskripsi} | {spek}")
        print(f"Harga: Rp {harga:,}")
        print(f"Stok: {stok}")
        print('''
        A. Masukkan keranjang
        B. Beli dan bayar
        ''')
        keranjang_beli = input("Pilih menu: ").strip().upper()
        if keranjang_beli == "A":
            keranjang(username, produk, harga, stok)
        elif keranjang_beli == "B":
            keranjang(username, produk, harga, stok)
            pembayaran(username)
        else:
            print("Pilihan tidak tersedia. Kembali ke menu.")
            jenis_produk(username)

    elif jenis == '6':
        os.system('cls')

        search = input(f"Silahkan ketik barang yang anda cari :")
        os.system('cls')
        file_path = "list_jenisproduk1.csv" 
        df = pd.read_csv(file_path)
        if search == "sekop" or search == "garpu tanah" or search == "cangkul" or search == "ember plastik" :
    
            print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|")
            print("|                 SELAMAT DATANG di TRIJAYA                 |")
            print("|_______________________ Alat tanam ________________________|")
            print("|___________________ dan Persiapan lahan ___________________|")
            print("+-----+---------------------------+--------------+----------+")
            print("| No  | Nama Produk               | Harga (Rp)   | Stok     |")
            print("+-----+---------------------------+--------------+----------+")
            for index, row in df.iterrows():
                id_produk = row["ID"]
                nama_produk = row["Nama_Produk"]
                harga_produk = row["Harga"]
                stok_produk = row["Stok"]
                print(f"| {id_produk:<3} | {nama_produk:<25} | Rp{harga_produk:>10,} | {stok_produk:>8} |")
            print("+-----+---------------------------+--------------+----------+")

            pilih_produk1 = input("Pilih produk (masukkan nomor ID): ").strip()

            if not pilih_produk1.isdigit() or int(pilih_produk1) not in df["ID"].values:
                print("Pilihan tidak tersedia!")
                input("Tekan Enter untuk kembali.")
                jenis_produk(username)
                return

            produk_row = df[df["ID"] == int(pilih_produk1)].iloc[0]
            produk = produk_row["Nama_Produk"]
            harga = produk_row["Harga"]
            stok = produk_row["Stok"]
            deskripsi = produk_row["Deskripsi"]
            spek = produk_row["Spesifikasi"]
            print(f"\nDetail Produk: {produk}")
            print(f"{deskripsi} | {spek}")
            print(f"Harga: Rp {harga:,}")
            print(f"Stok: {stok}")
            print('''
            A. Masukkan keranjang
            B. Beli dan bayar
            ''')
            keranjang_beli = input("Pilih menu: ").strip().upper()
            if keranjang_beli == "A":
                keranjang(username, produk, harga, stok)
            elif keranjang_beli == "B":
                keranjang(username, produk, harga, stok)
                pembayaran(username)
            else:
                print("Pilihan tidak tersedia. Kembali ke menu.")
                jenis_produk(username)
        
        elif search == "gembor" or search == "gunting" or search == "sprayer" or search == "pemangkas" or search == "pencabut" :
            os.system('cls')
            file_path = "list_jenisproduk2.csv"  
            df = pd.read_csv(file_path)
            print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|")
            print("|                 SELAMAT DATANG di TRIJAYA                 |")
            print("|________________ Alat Pemeliharaan Tanaman ________________|")
            print("+-----+---------------------------+--------------+----------+")
            print("| No  | Nama Produk               | Harga (Rp)   | Stok     |")
            print("+-----+---------------------------+--------------+----------+")
            for index, row in df.iterrows():
                id_produk = row["ID"]
                nama_produk = row["Nama_Produk"]
                harga_produk = row["Harga"]
                stok_produk = row["Stok"]
                print(f"| {id_produk:<3} | {nama_produk:<25} | Rp{harga_produk:>10,} | {stok_produk:>8} |")
            print("+-----+---------------------------+--------------+----------+")

            pilih_produk2 = input("Pilih produk (masukkan nomor ID): ").strip()

            if not pilih_produk2.isdigit() or int(pilih_produk2) not in df["ID"].values:
                print("Pilihan tidak tersedia!")
                input("Tekan Enter untuk kembali.")
                jenis_produk(username)
                return

            produk_row = df[df["ID"] == int(pilih_produk2)].iloc[0]
            produk = produk_row["Nama_Produk"]
            harga = produk_row["Harga"]
            stok = produk_row["Stok"]
            deskripsi = produk_row["Deskripsi"]
            spek = produk_row["Spesifikasi"]
            print(f"\nDetail Produk: {produk}")
            print(f"{deskripsi} | {spek}")
            print(f"Harga: Rp {harga:,}")
            print(f"Stok: {stok}")
            print('''
            A. Masukkan keranjang
            B. Beli dan bayar
            ''')
            keranjang_beli = input("Pilih menu: ").strip().upper()
            if keranjang_beli == "A":
                keranjang(username, produk, harga, stok)
            elif keranjang_beli == "B":
                keranjang(username, produk, harga, stok)
                pembayaran(username)
            else:
                print("Pilihan tidak tersedia. Kembali ke menu.")
                jenis_produk(username)

        elif search == "sabit" or search == "pisau" or search == "keranjang" or search == "plastik" or search == "timbangan" :
            os.system('cls')
            file_path = "list_jenisproduk3.csv"
            df = pd.read_csv(file_path)
            print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|")
            print("|                 SELAMAT DATANG di TRIJAYA                 |")
            print("|________________ Alat Panen dan Pascapanen ________________|")
            print("+-----+---------------------------+--------------+----------+")
            print("| No  | Nama Produk               | Harga (Rp)   | Stok     |")
            print("+-----+---------------------------+--------------+----------+")
            for index, row in df.iterrows():
                id_produk = row["ID"]
                nama_produk = row["Nama_Produk"]
                harga_produk = row["Harga"]
                stok_produk = row["Stok"]
                print(f"| {id_produk:<3} | {nama_produk:<25} | Rp{harga_produk:>10,} | {stok_produk:>8} |")
            print("+-----+---------------------------+--------------+----------+")

            pilih_produk3 = input("Pilih produk (masukkan nomor ID): ").strip()

            if not pilih_produk3.isdigit() or int(pilih_produk3) not in df["ID"].values:
                print("Pilihan tidak tersedia!")
                input("Tekan Enter untuk kembali.")
                jenis_produk(username)
                return

            produk_row = df[df["ID"] == int(pilih_produk3)].iloc[0]
            produk = produk_row["Nama_Produk"]
            harga = produk_row["Harga"]
            stok = produk_row["Stok"]
            deskripsi = produk_row["Deskripsi"]
            spek = produk_row["Spesifikasi"]
            print(f"\nDetail Produk: {produk}")
            print(f"{deskripsi} | {spek}")
            print(f"Harga: Rp {harga:,}")
            print(f"Stok: {stok}")
            print('''
            A. Masukkan keranjang
            B. Beli dan bayar
            ''')
            keranjang_beli = input("Pilih menu: ").strip().upper()
            if keranjang_beli == "A":
                keranjang(username, produk, harga, stok)
            elif keranjang_beli == "B":
                keranjang(username, produk, harga, stok)
                pembayaran(username)
            else:
                print("Pilihan tidak tersedia. Kembali ke menu.")
                jenis_produk(username)

        elif search == "pupuk" or search == "benih" or search == "cocopeat" or search == "kapur" :
            os.system('cls')
            file_path = "list_jenisproduk4.csv"  
            df = pd.read_csv(file_path)
            print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|")
            print("|                 SELAMAT DATANG di TRIJAYA                 |")
            print("|_____________________ Pupuk Dan Benih _____________________|")
            print("+-----+---------------------------+--------------+----------+")
            print("| No  | Nama Produk               | Harga (Rp)   | Stok     |")
            print("+-----+---------------------------+--------------+----------+")
            for index, row in df.iterrows():
                id_produk = row["ID"]
                nama_produk = row["Nama_Produk"]
                harga_produk = row["Harga"]
                stok_produk = row["Stok"]
                print(f"| {id_produk:<3} | {nama_produk:<25} | Rp{harga_produk:>10,} | {stok_produk:>8} |") 
            print("+-----+---------------------------+--------------+----------+")

            pilih_produk4 = input("Pilih produk (masukkan nomor ID): ").strip()

            if not pilih_produk4.isdigit() or int(pilih_produk4) not in df["ID"].values:
                print("Pilihan tidak tersedia!")
                input("Tekan Enter untuk kembali.")
                jenis_produk(username)
                return

            produk_row = df[df["ID"] == int(pilih_produk4)].iloc[0]
            produk = produk_row["Nama_Produk"]
            harga = produk_row["Harga"]
            stok = produk_row["Stok"]
            deskripsi = produk_row["Deskripsi"]
            spek = produk_row["Spesifikasi"]
            print(f"\nDetail Produk: {produk}")
            print(f"{deskripsi} | {spek}")
            print(f"Harga: Rp {harga:,}")
            print(f"Stok: {stok}")
            print('''
            A. Masukkan keranjang
            B. Beli dan bayar
            ''')
            keranjang_beli = input("Pilih menu: ").strip().upper()
            if keranjang_beli == "A":
                keranjang(username, produk, harga, stok)
            elif keranjang_beli == "B":
                keranjang(username, produk, harga, stok)
                pembayaran(username)
            else:
                print("Pilihan tidak tersedia. Kembali ke menu.")
                jenis_produk(username)

        elif search == "pestisida" or search == "fungisida" or search == "insektisida" or search == "herbisida" or search == "zpt" :
            os.system('cls')
            file_path = "list_jenisproduk5.csv" 
            df = pd.read_csv(file_path)
            print("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|")
            print("|                 SELAMAT DATANG di TRIJAYA                 |")
            print("|________________ Obat dan Perawatan Tanaman _______________|")
            print("+-----+---------------------------+--------------+----------+")
            print("| No  | Nama Produk               | Harga (Rp)   | Stok     |")
            print("+-----+---------------------------+--------------+----------+")
            for index, row in df.iterrows():
                id_produk = row["ID"]
                nama_produk = row["Nama_Produk"]
                harga_produk = row["Harga"]
                stok_produk = row["Stok"]
                print(f"| {id_produk:<3} | {nama_produk:<25} | Rp{harga_produk:>10,} | {stok_produk:>8} |")
            print("+-----+---------------------------+--------------+----------+")

            pilih_produk5 = input("Pilih produk (masukkan nomor ID): ").strip()

            if not pilih_produk5.isdigit() or int(pilih_produk5) not in df["ID"].values:
                print("Pilihan tidak tersedia!")
                input("Tekan Enter untuk kembali.")
                jenis_produk(username)
                return

            produk_row = df[df["ID"] == int(pilih_produk5)].iloc[0]
            produk = produk_row["Nama_Produk"]
            harga = produk_row["Harga"]
            stok = produk_row["Stok"]
            deskripsi = produk_row["Deskripsi"]
            spek = produk_row["Spesifikasi"]
            print(f"\nDetail Produk: {produk}")
            print(f"{deskripsi} | {spek}")
            print(f"Harga: Rp {harga:,}")
            print(f"Stok: {stok}")
            print('''
            A. Masukkan keranjang
            B. Beli dan bayar
            ''')
            keranjang_beli = input("Pilih menu: ").strip().upper()
            if keranjang_beli == "A":
                keranjang(username, produk, harga, stok)
            elif keranjang_beli == "B":
                keranjang(username, produk, harga, stok)
                pembayaran(username)
            else:
                print("Pilihan tidak tersedia. Kembali ke menu.")
                jenis_produk(username)
        else: 
            print ("Produk tidak ada!")
            input ("tekan enter untuk kembali")
            jenis_produk (username)
    
    elif jenis == "7":
        home ()

    else:
        print("Masukkan pilihan!")
        input("Tekan enter untuk kembali")
        jenis_produk(username)

def keranjang(username, produk, harga, stok):
    jumlah_input = input(f"Masukkan jumlah {produk}: ")

    if jumlah_input.strip() == "":
        print("Anda belum memasukkan stok")
        keranjang(username, produk, harga, stok)
    
    try:
        jumlah = int(jumlah_input)
    except ValueError:
        print("Input harus berupa angka")
        input ("Tekan enter untuk kembali!")
        keranjang(username, produk, harga, stok)

    if jumlah < 1:
        print("Input salah (harus lebih dari 0)")
        keranjang(username, produk, harga, stok)

    elif jumlah > stok:
        print(f"Stok {produk} tidak mencukupi. Stok tersedia: {stok}")
        keranjang(username, produk, harga, stok)

    else:
        print(f"{jumlah} {produk} berhasil ditambahkan ke keranjang.")

    
    total_harga = harga * jumlah
    stok_tersisa = stok - jumlah

    keranjang_file = 'KeranjangTRIJAYA.csv'
    data_keranjang = []

    file_exists = os.path.isfile(keranjang_file)

    if file_exists:
        with open(keranjang_file, mode='r') as file:
            reader = csv.reader(file)
            data_keranjang = list(reader)

    header = ["username", "produk", "harga", "jumlah", "total", "stok"]

    produk_ada = False
    for i in range(len(data_keranjang)):
        if len(data_keranjang[i]) == 6:
            user, prod, hrg, jml, tot, stok = data_keranjang[i]
            if user == username and prod == produk:
                data_keranjang[i][3] = str(int(jml) + jumlah)  
                data_keranjang[i][4] = str(harga * int(data_keranjang[i][3]))
                data_keranjang[i][5] = str(int(stok) - jumlah)
                produk_ada = True
                break
    
    if not produk_ada:
        data_keranjang.append([username, produk, str(harga), str(jumlah), str(total_harga), str(stok_tersisa)])
    
    with open(keranjang_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        if not file_exists or data_keranjang[0] != header:
            writer.writerow(header)
        writer.writerows(data_keranjang)
    
    print(f"{produk} berhasil ditambahkan ke keranjang!\n")
    print('''\
        A. Tambahkan produk lagi
        B. Lanjutkan ke pembayaran
        ''')
    keranjang_beli = input("Pilih menu: ").strip().upper()

    if keranjang_beli == "A":
        jenis_produk(username) 
    elif keranjang_beli == "B":
        ongkir = data_pengiriman() 
        pembayaran(username, ongkir)
    else:
        print("Pilihan tidak tersedia. Kembali ke menu utama.")
        jenis_produk(username)

def pembayaran(username, ongkir):
    print("\nMemproses pembayaran...\n")
    total_belanja = 0
    keranjang_user = {}

    print(f"Keranjang {username}:")
    print("+---------------------+---------------+----------------+-------------------+")
    print("| Produk              | Harga (Rp)    | Jumlah         | Total (Rp)        |")
    print("+---------------------+---------------+----------------+-------------------+")

    try:
        with open('KeranjangTRIJAYA.csv', mode='r') as file:
            reader = csv.reader(file)
            header = next(reader, None)

            if header != ["username", "produk", "harga", "jumlah", "total", "stok"]:
                print("File CSV tidak valid.")
                return

            for row in reader:
                if len(row) < 6:
                    continue

                user, produk, harga, jumlah, total, stok = row
                try:
                    user = str(user)
                    produk = str(produk)
                    harga = int(harga)
                    jumlah = int(jumlah)
                    total = int(total)
                    stok = int(stok)
                except ValueError:
                    
                    continue

                if user == username:
                    if produk in keranjang_user:
                        keranjang_user[produk]['jumlah'] += jumlah
                        keranjang_user[produk]['total'] += total
                    else:
                        keranjang_user[produk] = {
                            'harga': harga,
                            'jumlah': jumlah,
                            'total': total,
                        }

        for produk, data in keranjang_user.items():
            print(f"| {produk:<19} | {data['harga']:>13,} | {data['jumlah']:>14} | {data['total']:>17,} |")
            total_belanja += data['total']


        total_belanja += int(ongkir)

    except FileNotFoundError:
        print("Keranjang kosong. Silakan tambahkan produk terlebih dahulu.")
        return

    print("+---------------------+---------------+----------------+-------------------+")
    print(f"Total Belanja: Rp{total_belanja:>15,}")
    print('''
    Pilih Metode Pembayaran:
    1. Bank Account
    ''')
    metode = input("Pilih metode pembayaran: ").strip()
    if metode == '1':
        bank_account(username, total_belanja)
    else:
        print("Metode pembayaran tidak valid.")
        pembayaran(username, ongkir)
        
def kosongkan_keranjang(username):
    data_baru = [] 
    
    try:
        with open('keranjangTRIJAYA.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            
            if header:
                data_baru.append(header)
            
            for row in reader:
                if len(row) != len(header):
                    print(f"Baris tidak valid: {row}. Lewati.")
                    continue

                if row[0] != username:
                    data_baru.append(row)

        with open('keranjangTRIJAYA.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data_baru)
    except FileNotFoundError:
        print("File keranjang tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengosongkan keranjang: {e}")

def bank_account(username,total_belanja):
    os.system ("cls")
    print('''
    Pilih Pembayaran Bank:
    1. BCA
    2. Mandiri
    3. BRI
    4. BNI
    ''')
    bank = input("Pilih bank: ").strip()
    if bank in ['1', '2', '3', '4']:
        rekening = input("Masukkan nomor rekening Anda: ")
        if not rekening :
            print ("Rekening belum dimasukkan")
            input ("Tekan enter untuk mengisi kembali!")
            bank_account (username, total_belanja)
        print(f"Total yang harus dibayarkan: Rp{total_belanja}")
        print(f"Lakukan pembayaran ke rekening TRIJAYA: 2424101010.")
        jumlah_uang = int(input("Masukkan jumlah uang :"))
        sisa_saldo = jumlah_uang-total_belanja
        if jumlah_uang < total_belanja:
            print("Uang tidak cukup")
            bank_account(username, total_belanja)
        elif jumlah_uang > total_belanja:
            print(f"Kembalian Anda : {sisa_saldo}")
            print("Pembayaran berhasil!")
        elif jumlah_uang == total_belanja:
            print("Pembayaran berhasil!")
        print('''
            A. Kembali ke menu utama
            B. Keluar
        ''')
        pilihan = input("Pilih menu: ").strip().upper()
        if pilihan == "A":
            kosongkan_keranjang(username)
            home() 
        elif pilihan == "B":
            print("Terima kasih telah berbelanja di TRIJAYA!")
            kosongkan_keranjang (username)
            exit()
        else:
            print("Pilihan tidak valid. Mengakhiri program.")
            kosongkan_keranjang (username)
            exit()
    else:
        print("Pilihan bank tidak valid.")
        input ("Tekan enter untuk pilih kembali!")
        bank_account(username, total_belanja)
        
home()
