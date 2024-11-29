data_mhs = [
    ["Nama", "NPM", "Prodi", "Nilai"],
    ["Ghea Hilary Angelina", "038", "IF", 100],
    ["Nabil Syahreza Febry Usman", "044", "IF", 100],
    ["Muhammad Raehan Robban", "056", "IF", 100],
    ["Agus", "056", "IF", 80],
]

# with open('w8_hello_world.txt', 'r') as file:
#     print(file.read())


# with open('w8_data_mahasiswa.csv', 'w') as file:
#     for row in data_mhs:
#         for index, item in enumerate(row):
#             file.write(str(item))
#             if index != len(row)-1: file.write(',')
#         file.write('\n')


# with open('w8_data_mahasiswa.csv', 'w') as file:
#     for row in data_mhs:
#         for i in range(len(row)):
#             if i > 0:
#                 file.write(',')
#             file.write(str(row[i]))
#         file.write('\n')



# temp = []
# with open('w8_data_mahasiswa.csv', 'r') as file:
#     for line in file:
#         temp.append(line.strip().split(','))
# print(temp)


# temp = []
# with open('w8_data_mahasiswa.csv', 'r') as file:
#     for line in file:
#         temp.append(line.replace('\n', '').split(','))
# print(temp)





import csv

# with open('w8_data_mahasiswa.csv', 'w') as file:
#     csv_writer = csv.writer(file)
#     # csv_writer.writerows(data_mhs)
#     for line in data_mhs:
#         csv_writer.writerow(line)


# with open('w8_data_mahasiswa.csv', 'w') as file:
#     csv_writer = csv.writer(file)
#     for index, item in enumerate(data_mhs):
#         if index == 0 or item[3] > 90: 
#             csv_writer.writerow(item)


temp = []
with open('w8_data_mahasiswa.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for line in reader:
        temp.append(line)

print(temp)