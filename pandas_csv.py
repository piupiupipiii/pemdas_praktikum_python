import pandas as pd #mengimpor library pandas dengan alisan pd
#membaca file csv dari path yang sudah ditentukan
file_path = "C:\\Users\\Silvy Nur Azkia\\OneDrive\\Desktop\\Documents\\Kuliah\\tugas kuliah\\Pemrograman dasar\prak\\barang.csv"
df = pd.read_csv(file_path, thousands=',') #membaca file csv dari path yang sudah ditentukan
# Parameter thousands=',' digunakan untuk menangani pemisah ribuan pada kolom numerik.
print("Data Awal:") #print data awal yang dibaca oleh csv
print(df)