# matriks = [
#     [0, 1, 2],
#     [3, 4, 5],
#     [6, 7, 8]
# ]

# result = []
# for index, matrik in enumerate(matriks):
#     print(matriks[len(matriks)-index-1])
#     # result.append(matriks[len(matriks)-index-1])
#     for index1, matrik1 in enumerate(result):
#         # print(index1)
#         print("matrik1")
        

# result2 = []
# for index, matrik in enumerate(matriks):
#     result.append(matriks[len(matriks)-index-1])
#     for index2, matrik2 in enumerate(result):
#         # result2[index2].append(matrik[len(matrik)-index2-1])
#         print(matrik2)
# print(result)
# print(result2)

# for matrik in range(len(matriks)):
#     print(matrik, 'asdasd')
#     for matrik_dalam in range(matrik):
#         print(matrik_dalam)


# result2 = []
# for index, matrik in enumerate(matriks):
#     result.append(matriks[len(matriks)-index-1])
#     # for index_matrik_dalam, matrik_dalam in enumerate(result):
#     #     result2.append(result[len(result)-index_matrik_dalam-1])
    
# for index_matrik_dalam, result in enumerate(result):
#     result2.append(result[len(result)-index-1])
    
# print(result)
# print(result2)


# angka = [
#     [0, 1, 2],
#     [3, 4, 5],
#     [6, 7, 8]
# ]

# hasil = []
# for i in range(len(angka) - 1, -1, -1):
#     temp = []
#     for j in range(len(angka[i]) -1, -1, -1):
#         temp.append(angka[i][j])
#     hasil.append(temp)
# print(hasil)





# rows = int(input("Masukan Baris: "))
# columns = int(input("Masukan Kolom: "))

# matriks_1 = []

# print("Matriks 1")
# for row in range(rows):
#     temp = []
#     for column in range(columns):
#         temp.append(input(f'Masukan Nilai Pada baris {row} dan kolom {column}: '))
#     matriks_1.append(temp)
    

# matriks_2 = []
# print("Matriks 2")
# for row in range(rows):
#     temp = []
#     for column in range(columns):
#         temp.append(input(f'Masukan Nilai Pada baris {row} dan kolom {column}: '))
#     matriks_2.append(temp)
    
    
# matriks_3 = []
# print("Matriks 3")
# for row in range(rows):
#     temp = []
#     for column in range(columns):
#         temp.append(int(matriks_1[row][column]) + int(matriks_2[row][column]))
#     matriks_3.append(temp)


# print(matriks_1)
# print(matriks_2)
# print(matriks_3)


# huruf = input("Masukan: ")

# result = {}
# for i in range(len(huruf)):
#     result[huruf[i]] = 0

# for i in range(len(huruf)):
#     if result[huruf[i]] == result[huruf[i]]:
#         result[huruf[i]] += 1
# print(result)



text = input("Masukan: ")

result = dict({})
for i in text:
    if i in result.keys():
        result[i] += 1
    else:
        result[i] = 1

print(result)