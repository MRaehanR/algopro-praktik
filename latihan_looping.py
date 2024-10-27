def sum_numbers_to_ten():
    sum = 0
    for i in range(1, 11):
        sum += i
    print(sum)
    
sum_numbers_to_ten()


print('-'*25)


def sum_numbers_with_specific_num():
    num = 7
    sum = 0
    for i in range(1, num+1):
        sum += i
    print(sum)
    
sum_numbers_with_specific_num()


print('-'*25)



def triangle_stars():
    result = ''
    for i in range(4):
        for j in range(i):
            result += '*'
            print(result)

triangle_stars()

print('-'*25)

def triangle_ordered_number():
    for i in range(1, 7):
        result = ''
        for j in range(1, i):
            result += str(j)
        print(result)
    
triangle_ordered_number()

print('-'*25)

def triangle_row_repeat_number():
    for i in range(1, 5):
        result = ''
        for j in range(i):
            result += str(i)
        print(result)
        
triangle_row_repeat_number()
    
print('-'*25)

def reverse_pyramid_stars():
    for i in range(5):
        result = ''
        for j in range(5-i):
            result += '*'
        for j in range(5):
            result += ' '
        print(result)
        
reverse_pyramid_stars()

print('-'*25)



def diagonal():
    rows = 6
    columns = 6
    for row in range(rows):
        for column in range(columns):
            if column == row:
                print('*', end='')
            elif column % 2 == 0 and row % 2 == 0 or column % 2 == 1 and row % 2 == 1:
                print('x', end='')
            else:
                print('o', end='')
        print('')
        
diagonal()

print('-'*25)


# List
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

import re

def calculator():
    print("Selamat datang di Kalkulator Python!")
    print("Ketik 'keluar' untuk mengakhiri program.")
    
    while True:
        # Menerima input dari pengguna
        user_input = input("Masukkan operasi matematika: ")
        
        # Cek apakah pengguna ingin keluar
        if user_input.lower() == 'keluar':
            print("Terima kasih telah menggunakan Kalkulator Python!")
            break
        
        try:
            # Membersihkan input dari karakter yang tidak diinginkan
            cleaned_input = re.sub(r'[^0-9+\-*/().\s]', '', user_input)
            
            # Mengevaluasi ekspresi matematika
            result = eval(cleaned_input)
            
            # Menampilkan hasil
            print(f"Hasil: {result}")
        
        except (SyntaxError, NameError, ZeroDivisionError) as e:
            print(f"Error: {str(e)}")
            print("Pastikan Anda memasukkan operasi matematika yang valid.")
        
        except Exception as e:
            print(f"Terjadi kesalahan yang tidak diketahui: {str(e)}")

# Menjalankan kalkulator
calculator()



