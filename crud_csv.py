import csv #import module csv untuk manipulasi file csv

def read_data(): #fungsi untuk membaca data dari file 'barang.csv'
    with open('barang.csv', 'r') as file:
        reader = csv.DictReader(file) #membaca setiap baris sebagai dictionary
        data = list(reader)
    return data

def write_data(data): #fungsi untuk menulis data ke file csv
    with open('barang.csv', 'w', newline='') as file:
        fieldnames = ['Nama_Barang', 'Harga', 'Jumlah_Stok'] #daftar kolom yang digunakan sebagai header
        writer = csv.DictWriter(file, fieldnames=fieldnames) #untuk menulis data dalam format dictionary ke file csv

        # Menulis header
        writer.writeheader()

        # Menulis data
        for row in data:
            writer.writerow(row)

# Fungsi untuk menampilkan data
def show_data(): #menggunakan fungsi 'read_data' untuk membaca dan menampilkan data dari file csv
    data = read_data() #membaca data dari file csv yang akan disimpan divariabel 'data'
    if not data: #jika data tidak ada
        print("Data kosong.") #maka print data kosong
    else: #jika ada
        for row in data: #print setiap baris yang ada pada data
            print(row)

# Fungsi untuk menambahkan data baru
def add_data(new_data):
    data = read_data() #membaca data dari file csv yang akan disimpan divariabel 'data'
    data.append(new_data) #menambahkan data baru
    write_data(data) #memanggil fungsi untuk menulis kembali data ke file csv
    print("Data berhasil ditambahkan.")

# Fungsi untuk memperbarui data berdasarkan Nama Barang
def update_data(update_barang, new_data):
    data = read_data() #membaca data dari file csv yang akan disimpan divariabel 'data'
    for row in data: #untuk baris di dalam data
        if row['Nama_Barang'] == update_barang: #jika baris 'Nama_Barang' sama dengan update_barang
            row.update(new_data) #maka tambahkan barang di dalam baris dengan value 'new_data'
            write_data(data) #memanggil fungsi untuk menulis kembali data ke file csv
            print("Data berhasil diperbarui.")
            return
        print(f"Tidak ada data dengan Nama_Barang {update_barang}.")

# Fungsi untuk menghapus data berdasarkan Nama Barang
def delete_data(delete_barang):
    data = read_data() #membaca data dari file csv yang akan disimpan divariabel 'data'
    for i, row in enumerate(data):
        if row['Nama_Barang'] == delete_barang: #jika 'Nama_Barang' dalam baris sama dengan 'delete_barang'
            del data[i] #hapus baris data dari list berdasarkan index
            write_data(data) #memanggil fungsi untuk menulis kembali data ke file csv
            print("Data berhasil dihapus.")
            return
    print(f"Tidak ada data dengan Nama_Barang {delete_barang}.") #jika nama barang yang diinputkan tidak ada

# Main program
while True: #looping yang akan terus berjalan selama kondisi didalamnya 'True'
    print("\nMenu:")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Perbarui Data")
    print("4. Hapus Data")
    print("5. Keluar") #jika ingin keluar dari program
    pilihan = input("Pilih menu (1-5): ") #input untuk memilih salah satu menu, input disimpan didalam variabel 'pilihan'

    if pilihan == '1': #jika pilihan == 1 (Tampilkan Data)
        show_data() #maka tampilkan data dari file csv
    elif pilihan == '2': #jika pilihan == 1 (Tambah Data)
        new_data = {'Nama_Barang': input("Masukkan Nama Barang: "), 'Harga': input("Masukkan Harga: "), 'Jumlah_Stok': input("Masukkan jumlah stok: ")}
        add_data(new_data) #memanggil 'add_data(new_data)' untuk menambahkan data baru ke file csv
    elif pilihan == '3': #jika pilihan == 1 (Update Data)
        update_barang = input("Masukkan Nama Barang data yang akan diperbarui: ")
        new_data = {'Nama_Barang': input("Masukkan nama barang baru: "), 'Harga':                   
        input("Masukkan harga: "), 'Jumlah_Stok': input("Masukkan jumlah stok: ")}
        update_data(update_barang, new_data) #memanggil fungsi 'update_data', akan meng-update value dengan data baru yang diinputkan
    elif pilihan == '4': #jika pilihan == 1 (Delete Data)
        delete_barang = input("Masukkan Nama_Barang yang akan dihapus: ")
        delete_data(delete_barang) #memanggil fungsi 'delete_barang', akan menghapus data sesuai value yang diinputkan untuk dihapus
    elif pilihan == '5':
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1-5.")