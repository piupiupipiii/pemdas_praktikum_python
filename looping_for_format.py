a = input("masukkan nama : ")

print ("Masukkan Nama Kamu : {}". format(a))

# Input angka untuk looping
b = int(input("masukkan banyak looping : "))

print ("Masukkan banyak looping : {}". format(b))

# Buat range dari 0 sampai jumlah looping - 1
#   Contoh: jumlah looping adalah 5, maka rangenya 0 s/d 4
# Lalu looping range tersebut,
# dan masukan setiap angka dalam range ke variable i
for i in range(b):
    # Print angka dalam range
    # diikuti dengan nama yang sudah diinput di awal
    print('No {}. {}'. format (i, a))