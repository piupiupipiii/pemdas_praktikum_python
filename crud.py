import mysql.connector
#berisi detail konfigurasi untuk terhubung ke database MySQL. Ini mencakup host, user, password,dan nama database.
db_config = {'host': 'localhost', 'user': 'root', 'password': '', 'database': 'hotel'}

#fungsi untuk menghubungkan ke databsase MySQL menggunakan db_config
def create_connection():
 try:
    connection = mysql.connector.connect(**db_config)
    #jika terhubung maka akan menunjukkan notifikasi 'terhubung ke database mysql'
    if connection.is_connected():
        print('Terhubung ke database MySQL')
    return connection
 
 #jika gagal, maka akan mengembalikan none
 except mysql.connector.Error as e:
    print(f"Error koneksi ke MySQL: {e}")
    return None
 
#fungsi untuk mengambil query SQL dan values opsional yang akan dimasukkan ke dalam query.
def execute_query(query, values=None):
    #fungsi yang dipanggil untuk membuat koneksi ke database MySQL
    connection = create_connection()
    #jika koneksi berhasil, program berlanjut
    if connection:
        cursor = connection.cursor()
        cursor.execute(query, values)

    #jika query dimulai dengan "SELECT"
    if query.lower().startswith("select"):
        #hasil query tersebut diambil menggunakan 'cursor.fetchall()'
        result = cursor.fetchall()
        #kemudian cursor di tutup
        cursor.close()
        #dan koneksi ditutup
        connection.close()
        #lalu hasilnya dikembalikan
        return result
    else:
        connection.commit()
        cursor.close()
        connection.close()

#bagian looping untuk memilih menu yang akan terus berjalan sampai ada perintah break
while True:
    print("Pilih Menu : \n"
        "1. Select\n" "2. Insert\n" "3. Update\n" "4. Delete\n" "5. Exit\n")
    menu = int(input("Masukkan pilihan menu : "))

    #jika menu yang dipilih yaitu SELCET
    if menu == 1:
        #query SELECT mengamnil semua data dari tabel "rooms"
        select_query = "SELECT * FROM rooms"
        result = execute_query(select_query)
        #print hasilnya
        print(result)

    #jika memilih menu INSERT
    elif menu == 2:
        #meminta input baru dari 'id_rooms', 'type', 'lantai', dan 'harga'
        values = (
        input("Masukkan ID Kamar: "),
        input("Masukkan Jenis Kamar: "),
        input("Masukkan Lantai: "),
        input("Masukkan Harga: ")
        )
        #menjalankan query INSERT untuk menambahkan data baru ke tabel "rooms"
        insert_query = "INSERT INTO rooms (id_rooms, type, lantai, harga) VALUES (%s, %s, %s,%s)"
        execute_query(insert_query, values)

    #jika memilih menu UPDATE
    elif menu == 3:
        #meminta input baru dari 'id_rooms', 'type', 'lantai', dan 'harga'
        values = (
        input("Masukkan ID Kamar yang Akan Diupdate: "),
        input("Masukkan ID Kamar Baru: "),
        input("Masukkan Jenis Kamar Baru: "),
        input("Masukkan Lantai Baru: "),
        input("Masukkan Harga Baru: ")
        )
        # menjalankan query UPDATE untuk mengupdate data baru ke tabel "rooms"
        update_query = "UPDATE rooms SET id_rooms=%s, type=%s, lantai=%s, harga=%s WHERE id_rooms=%s"
        execute_query(update_query, values)

    #jika memilih menu DELETE
    elif menu == 4:
        #meminta inputan dari 'id_rooms' yang akan dihapus
        id_rooms = input("Masukkan ID Kamar yang Akan Dihapus: ")
        # menjalankan query DELETE untuk menghapus data dari tabel "rooms"
        delete_query = "DELETE FROM rooms WHERE id_rooms=%s"
        execute_query(delete_query, (id_rooms,))
        
    #jika memilih menu Exit
    elif menu == 5:
    #maka program keluar dari loop 'While True' dan program selesai
        break