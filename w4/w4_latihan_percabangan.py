# nilai = int(input("Masukan Nilai: "))
# kehadiran = int(input("Masukan Nilai: "))

# if nilai >= 81 and nilai <= 100:
#     print("A")
# elif nilai >= 61 and nilai < 81:
#     print("B")
# elif nilai >= 41 and nilai < 61:
#     print("C")
# elif nilai >= 21 and nilai < 41:
#     print("D")
# elif nilai >= 0 and nilai < 21:
#     print("E")
# else:
#     print("Nilai Tidak Valid")







# nilai_akhir = int(input("Masukan Nilai Akhir: "))
# jumlah_kehadiran = int(input("Masukan Jumlah Kehadiran: "))

# nilai = ""

# if nilai_akhir >= 81 and jumlah_kehadiran >= 11:
#     nilai = "A"
# elif nilai_akhir >= 61 and jumlah_kehadiran >= 9 :
#     nilai = "B"
# elif nilai_akhir >= 41 and jumlah_kehadiran >= 7 :
#     nilai = "C"
# elif nilai_akhir >= 21 and jumlah_kehadiran >= 5:
#     nilai = "D"
# else:
#     nilai = "E"
    
# print(f'Hasil nilai huruf: {nilai}')
# print("Detail")
# print(f'Nilai akhir {nilai_akhir} dan {jumlah_kehadiran} pertemuan')






# nilai_akhir = int(input("Masukan Nilai Akhir: "))
# jumlah_kehadiran = int(input("Masukan Jumlah Kehadiran: "))

# nilai = ""

# if (nilai_akhir >= 81 and nilai_akhir <= 100) and (jumlah_kehadiran >= 11 and jumlah_kehadiran <= 14):
#     nilai = "A"
# elif (nilai_akhir >= 61 and nilai_akhir < 81) and (jumlah_kehadiran >= 9 and jumlah_kehadiran < 11):
#     nilai = "B"
# elif (nilai_akhir >= 41 and nilai_akhir < 61) and (jumlah_kehadiran >= 7 and jumlah_kehadiran < 9):
#     nilai = "C"
# elif (nilai_akhir >= 21 and nilai_akhir < 41) and (jumlah_kehadiran >= 5 and jumlah_kehadiran < 7):
#     nilai = "D"
# elif (nilai_akhir >= 0 and nilai_akhir < 21) and (jumlah_kehadiran >= 0 and jumlah_kehadiran < 5):
#     nilai = "E"
    
# print(f'Hasil nilai huruf: {nilai}')
# print("Detail")
# print(f'Nilai akhir {nilai_akhir} dan {jumlah_kehadiran} pertemuan')


nilai_akhir = float(input("Masukan Nilai Akhir: "))
jumlah_kehadiran = float(input("Masukan Jumlah Kehadiran: "))

nilai = ""

if nilai_akhir >= 81 and jumlah_kehadiran >= 11:
    nilai = "A"
elif nilai_akhir >= 61 and jumlah_kehadiran >= 9 :
    nilai = "B"
elif nilai_akhir >= 41 and jumlah_kehadiran >= 7 :
    nilai = "C"
elif nilai_akhir >= 21 and jumlah_kehadiran >= 5:
    nilai = "D"
else:
    nilai = "E"
    
print(f'Hasil nilai huruf: {nilai}')
print("Detail")
print(f'Nilai akhir {nilai_akhir} dan {jumlah_kehadiran} pertemuan')