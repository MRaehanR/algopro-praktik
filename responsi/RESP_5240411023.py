rekap_nilai = {
    "Algoritma":{
        "dosen":"Ir. Putra Alam",
        "nik":"334229100",
        "nilai":[73, 45, 89, 77, 73, 30]
    },
    "Struktur Data":{
        "dosen":"Hamdan Syakirin, S.Kom., M.Kom.",
        "nik":"334229101",
        "nilai":[91, 80, 32, 91, 45, 22, 100]
    },
    "Seni Rupa":{
        "dosen":"Dr. Ponirin Indra Ketujuh",
        "nik":"334229105",
        "nilai":[19, 45, 100, 24, 87]
    }
}

def tambah_matkul(data, matkul, dosen, nik, nilai):

    if matkul in data:
        print(f"Mata kuliah '{matkul}' dengan dosen '{data[matkul]['dosen']}' sudah ada.")
        return
    
    
    for matkuliah in data.values():
        if matkuliah["nik"] == nik:
            print("NIK sudah digunakan oleh mata kuliah lain.")
            return

    data[matkul] = {
        "dosen": dosen,
        "nik": nik,
        "nilai": nilai
    }

    print("Data setelah penambahan mata kuliah baru:")
    for matkuliah, informasi in data.items():
        print(f"Mata Kuliah: {matkuliah}")
        print(f"Dosen: {informasi['dosen']}")
        print(f"NIK: {informasi['nik']}")
        print(f"Nilai: {informasi['nilai']}\n")
   #Lakukan perulangan untuk mengambil data dari dictionary
   #Lakukan seleksi bahwa jika nama matkul atau nik sudah ada maka invalid
   #Berikan pesan(print) pemberitahuan bahwa data sudah ada
        return #untuk menghentikan fungsi 


   #Jika data belum ada maka tambahkan disini
   #selesai menambahkan maka buat supaya semua data ditampilkan dengan rapi
   #Pastikan data sudah terupdate dengan tambahan yang baru
def tampil_nilai_tertinggi(data):
    for matkuliah, informasi in data.items():
        nilai_tertinggi = max(informasi["nilai"])
        print(f"Nilai tertinggi untuk {matkuliah}: {nilai_tertinggi}")

   #Lanjutkan Coding disini
   #Gunakan perulangan untuk mengambil nilai tertinggi masing-masing matkul
   #Tampilkan masing-masing nilai tinggi tiap matkul itu

tambah_matkul(rekap_nilai, "Teknik Lingkungan", "Ir. Maskito Wawan", "334229107", [90, 99, 19, 22]) 
tambah_matkul(rekap_nilai, "Algoritma", "Raden Mas Ajeng, S.Kom., M.Kom.", "334229100", [90, 99, 19, 22])
tampil_nilai_tertinggi(rekap_nilai)
#output:
# Data setelah penambahan mata kuliah baru:
# Mata Kuliah: Algoritma
# Dosen: Ir. Putra Alam
# NIK: 334229100
# Nilai: [73, 45, 89, 77, 73, 30]

# Mata Kuliah: Struktur Data
# Dosen: Hamdan Syakirin, S.Kom., M.Kom.
# NIK: 334229101
# Nilai: [91, 80, 32, 91, 45, 22, 100]

# Mata Kuliah: Seni Rupa
# Dosen: Dr. Ponirin Indra Ketujuh
# NIK: 334229105
# Nilai: [19, 45, 100, 24, 87]

# Mata Kuliah: Teknik Lingkungan
# Dosen: Ir. Maskito Wawan
# NIK: 334229107
# Nilai: [90, 99, 19, 22]

# tambah_matkul(rekap_nilai, "Algoritma", "Raden Mas Ajeng, S.Kom., M.Kom.", "334229100",[90,99,19,22]))
#output: Mata kuliah 'Algoritma' dengan dosen 'Ir. Putra Alam' sudah ada (Mungkin nik salah).

# tampil_nilai_tertinggi(rekap_nilai)
#output:Nilai tertinggi untuk Algoritma: 89
        # Nilai tertinggi untuk Struktur Data: 100
        # Nilai tertinggi untuk Seni Rupa: 100
        # Nilai tertinggi untuk Teknik Lingkungan: 99

    


