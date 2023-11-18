# <strong> Praktikum Python </strong>
>Tugas praktikum 5 Bahasa Pemrograman | Universitas Pelita Bangsa

| Nama                    |  *NIM*           | *Kelas*      |
|:-----------------------:|-----------------:|-------------:|
|*Gladis Toti Anggraini*  | *312310566*      |  *TI.23.A5*  |

# Tugas Latihan

## Membuat list dengan 5 elemen
![Alt text](image-1.png) ![alt text](image-1.png?raw=true)

### #Akses List
* list1 = ["2", "5", "9", "10", "7"]: Membuat sebuah list dengan nama list1 yang berisi lima elemen, yaitu string "2", "5", "9", "10", dan "7".

* print("Tampilkan element ke-3 :", list1[3]): Menampilkan elemen ke-3 dari list. Dalam Python, indeks dimulai dari 0, jadi list1[3] merujuk ke elemen ke-4 dari list (indeks 0: "2", indeks 1: "5", indeks 2: "9", indeks 3: "10", dan indeks 4: "7"). Hasilnya adalah "10".

* print("Ambil nilai element 2-4", list1[2:5]): Menampilkan elemen dari indeks 2 hingga indeks 4 (indeks 2, 3, dan 4). Ini disebut slicing di Python. Jadi, list1[2:5] akan menghasilkan sublist ["9", "10", "7"].

* print("Ambil element terakhir :", list1[0:4]): Menampilkan elemen dari indeks 0 hingga indeks 3 (indeks 0, 1, 2, dan 3). Jadi, list1[0:4] akan menghasilkan sublist ["2", "5", "9", "10"].

### #Ubah Elemen List Ke 4 dengan Nilainya

* list2 = ["2", "5", "9", "10", "7"]: Membuat list dengan nama list2 yang berisi lima elemen string: "2", "5", "9", "10", dan "7".

* print("sebelum di ubah :", list2): Menampilkan isi dari list sebelum dilakukan perubahan. Hasilnya akan mencetak elemen-elemen awal dari list2.

* list2[4] = "8": Mengubah nilai elemen pada indeks ke-4 dari list list2. Indeks dimulai dari 0, sehingga list2[4] merujuk ke elemen ke-5 dari list (indeks 0: "2", indeks 1: "5", indeks 2: "9", indeks 3: "10", dan indeks 4: "7"). Dalam kode ini, nilai "7" pada indeks ke-4 diganti dengan nilai "8".

* print("setelah di ubah :", list2): Menampilkan isi dari list setelah dilakukan perubahan. Hasilnya akan mencetak list list2 yang sudah mengalami perubahan nilai pada indeks ke-4.

Sebagai hasilnya, program ini menggantikan nilai "7" pada indeks ke-4 dengan nilai "8", dan kemudian menampilkan list setelah perubahan.

### #Ubah Elemen List Ke 4 sampai dengan Nilai Terakhir

* list3 = ["2", "5", "9", "10", "7"]: Membuat list dengan nama list3 yang berisi lima elemen string: "2", "5", "9", "10", dan "7".

* print("Sebelum di ubah :", list3): Menampilkan isi dari list list3 sebelum dilakukan perubahan. Hasilnya akan mencetak elemen-elemen awal dari list3.

* list3[0:6] = ["2", "5", "9", "7", "10"]: Mengganti sebagian elemen dalam list3 mulai dari indeks 0 hingga indeks 5 (indeks 0, 1, 2, 3, 4, dan 5) dengan list baru ["2", "5", "9", "7", "10"]. Operasi ini menggunakan teknik slicing untuk mengganti sebagian elemen list dengan list lainnya.

* print("Setelah di ubah :", list3, "\n"): Menampilkan isi dari list list3 setelah dilakukan perubahan. Hasilnya akan mencetak list list3 yang sudah mengalami perubahan pada sebagian elemennya.

<br>Elemen pada indeks 0 diganti dengan "2".
<br>Elemen pada indeks 1 diganti dengan "5".
<br>Elemen pada indeks 2 diganti dengan "9".
<br>Elemen pada indeks 3 diganti dengan "7".
<br>Elemen pada indeks 4 diganti dengan "10".
<br>Elemen pada indeks 5 diganti dengan "10" 
<br>(indeks 5 diikutkan dalam slicing, meskipun biasanya di Python indeks akhir tidak diikutkan).


![Alt text](image-2.png)

### #Tambah List Elemen
* Buat list pertama (A)
<br>lista  = [1, 2, 3, 4, 5]
<br>print("List A\n", lista)
<br>listb  = [6, 7, 8]
<br>print("List B Sebelum di tambahkan :\n", listb, "\n")
<br>Pada bagian ini, dua list, yaitu lista dan listb diinisialisasi. lista berisi angka 1 sampai 5, sedangkan listb berisi angka 6 sampai 8.

* Penambahan sublist lista[0:2] ke dalam listb pada indeks 2
<br>lista  = [1 ,2 ,3 ,4 ,5]
<br>print("List A\n", lista)
<br>listb  = [6 ,7 ,8 ]
<br>listb.insert(2, lista[0:2])  
<br>print("List B Sesudah di tambahkan :\n", listb, "\n")
<br>Pada bagian ini, dua elemen pertama dari lista (yaitu lista[0:2] atau [1, 2]) dimasukkan ke dalam listb pada indeks 2 menggunakan metode insert.

* Penambahan nilai string "Timey" ke dalam listb
<br>listb.append("Timey")
<br>print("List B :\n", listb,"\n")
<br>Pada bagian ini, string "Timey" ditambahkan ke dalam listb menggunakan metode append.

* Menambahkan list B dengan 3 Nilai
<br>listb.extend([10, 12, 14])
<br>print("Mendambahkan List B dengan 3 nilai :\n", listb,"\n")
<br>Pada bagian ini, tiga nilai (10, 12, 14) ditambahkan ke dalam listb menggunakan metode extend.

* Menggabungkan ListA dan ListB 
<br>listN = lista + listb
<br>print("Gabungan list A & List B: \n", listN)
<br>Pada bagian ini, lista dan listb digabungkan menjadi list baru listN menggunakan operator +.




# Tugas Praktikum 
![Alt text](image-3.png)

* Inisialisasi List:
<br>nama = []
<br>nim = []
<br>nilaiTugas = []
<br>nilaiUTS = []
<br>nilaiUAS = []
<br>nilaiAkhir = []

<br>Membuat beberapa list kosong (nama, nim, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir) yang akan digunakan untuk menyimpan data mahasiswa.

* Input Data Mahasiswa:
<br>while True:
   <br>nama.append(input("Masukan nama : "))
    <br>nim.append(input("Masukan NIM  : "))
    <br>Tugas = int(input("Nilai Tugas  : ")); 
    <br>nilaiTugas.append(Tugas)
    <br>UTS   = int(input("Nilai UTS    : ")); 
    <br>nilaiUTS.append(UTS)
    <br>UAS   = int(input("Nilai UAS    : ")); 
    <br>nilaiUAS.append(UAS)

    <br>nilaiAkhir.append(Tugas * 30/100 + UTS * 35/100 + UAS * 35/100)

    <br>_tanya = input("Tambah data ? [y/t]: ")
    if(_tanya == "t"):
        break

<br>Program menggunakan perulangan while untuk terus meminta input data mahasiswa sampai pengguna memilih untuk tidak menambahkan data lagi (_tanya == "t"). Setiap input data disimpan dalam list yang sesuai, dan nilai akhir dihitung berdasarkan bobot tugas, UTS, dan UAS yang diberikan.

* Output Tabel Data Mahasiswa:
<br>print("+----+-----------------------+--------+--------+-------+-------+---------+")
<br>print("| {0:^2} | {1:^18} | {2:^9} | {3:^6} | {4:^5} | {5:^5} | {6:^7} |".format("No", "Nama", "NIM", "Tugas", "UTS", "UAS", "Akhir"))
<br>print("-----+-----------------------+--------+--------+-------+-------+---------+")
<br>no = 0
<br>for nama, nim, Tugas, UTS, UAS, nilaiAkhir in zip(nama, nim, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir):
<br>no += 1    
<br>print("| {0:>2} | {1:<18} | {2:>8} | {3:>6} | {4:>5} | {5:>5} | {6:>7} |".format(no, nama, nim, Tugas, UTS, UAS, nilaiAkhir))
<br>print("+----+-----------------------+--------+--------+-------+-------+---------+")

<br>Program mencetak tabel dengan format yang rapi untuk menampilkan data mahasiswa, termasuk nomor urut, nama, NIM, nilai tugas, nilai UTS, nilai UAS, dan nilai akhir. Ini menggunakan fungsi format untuk memformat output tabel.
<br>Sebagai hasilnya, program ini memberikan antarmuka sederhana untuk memasukkan data mahasiswa, menghitung nilai akhir, dan menampilkan data dalam bentuk tabel.

![Alt text](image-6.png)

## Flowchart
![Alt text](image-5.png)

1. Program dimulai dengan menginisialisasi list data_mahasiswa untuk menyimpan data mahasiswa.
2. Didefinisikan fungsi hitung_nilai_akhir untuk menghitung nilai akhir berdasarkan proporsi yang diberikan.
3. Program menggunakan perulangan while True untuk terus meminta input data.
4. Pengguna diminta untuk memasukkan nama, nilai tugas, nilai UTS, dan nilai UAS.
5. Nilai akhir dihitung menggunakan fungsi hitung_nilai_akhir dan data dimasukkan ke dalam list.
6. Program menanyakan apakah pengguna ingin menambahkan data lagi, dan perulangan berlanjut jika jawabannya 'y', jika tidak maka 't'.
7. Setelah selesai memasukkan data, program menampilkan daftar data mahasiswa dalam format tabel sederhana.

