# Akses list
list1 = ["2", "5", "9", "10", "7"]
print("Tampilkan element ke-3 :", list1[3]) 
print("Ambil nilai element 2-4", list1[2:5])
print("Ambil element terakhir :", list1[0:4])

print( 45*"=", "\n")

# ubah elemen list ke 4 dengan nilainya
list2 = ["2", "5", "9", "10", "7"]
print("sebelum di ubah :", list2)
list2[4] = "8"
print("setelah di ubah :", list2)

print( 45*"=", "\n")

# ubah elemen list ke 4 sampai dengan elemen terkahir
list3 = ["2", "5", "9", "10", "7"]
print("Sebelum di ubah :", list3)
list3[0:6] = ["2", "5", "9", "7", "10"]
print("Setelah di ubah :", list3, "\n")

print( 45*"=", "\n")

# Tambah list element
# Index   0(-5),   1(-4),  2(-3),   3(-2),   4(-1) 
lista  = [1, 2, 3, 4, 5]
print("List A\n", lista)
listb  = [6, 7, 8]
print("List B Sebelum di tambahkan :\n", listb, "\n")

lista  = [1 ,2 ,3 ,4 ,5]
print("List A\n", lista)
listb  = [6 ,7 ,8 ]
listb.insert(2, lista[0:2])  
print("List B Sesudah di tambahkan :\n", listb, "\n")

# Mendambahkan list B dengan nilai string
listb.append("Timey")
print("List B :\n", listb,"\n")

# Menambahkan list B dengan 3 Nilai
listb.extend([10, 12, 14])
print("Mendambahkan List B dengan 3 nilai :\n", listb,"\n")
# Menggabungkan ListA dan ListB 
listN = lista + listb
print("Gabungan list A & List B: \n", listN)


