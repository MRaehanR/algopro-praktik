# data = [1, 2, 3, 4, 5, 6, 7, 9, 10]

# for i in data:
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)




# Soal
# kata = "Bu Enney Itje"

# result = ''
# for char in kata:
#     if char == 'n' or char == 'e' or char == 'E':
#         continue
#     else:
#         result += char


# print(result)



# for i in range(100):
#     print(f"Hello World! ke-{i+1}")


# result = ''
# for i in range(4):
#     print(i)
#     for j in range(i):
#         result += '*'
#         print(result)


# for i in range(4):
#     print('*'*(i+1))


# print('r'*10)


import random

number = random.randint(1, 5)
chance = 5

while chance > 0:
    print(f'Sisa Kesempatan: {chance}')
    input_number = int(input(f'Masukan Angka: '))
    if input_number > number:
        print('Angka Input Lebih Dari Jawaban')
    elif input_number < number:
        print('Angka Input Kurang Dari Jawaban')
    else:
        print('Tebakan Anda Benar!')
        break
    chance -= 1


# while chance+1 > 0:
#     if chance == 1:
#         print("Kesempatan anda Habis!")
#         break
#     print(f'Sisa Kesempatan: {chance}')
#     input_number = int(input(f'Masukan Angka: '))
#     if input_number > number:
#         print('Angka Input Lebih Dari Guess Number')
#     elif input_number < number:
#         print('Angka Input Kurang Dari Guess Number')
#     else:
#         print('Tebakan Anda Benar!')
#         break
#     chance -= 1

# for chance in range(5, 0, -1):
#     print(f'Sisa Kesempatan: {chance}')
#     input_number = int(input(f'Masukan Angka: '))
#     if input_number > number:
#         print('Angka Input Lebih Dari Guess Number')
#     elif input_number < number:
#         print('Angka Input Kurang Dari Guess Number')
#     else:
#         print('Tebakan Anda Benar!')
#         break
