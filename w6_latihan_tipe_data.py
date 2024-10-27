# List
print('-'*25, 'LIST', '-'*25)

minumanku_list = ['Es Teh', 'Es Jeruk', 'Es Kopi']
print(minumanku_list)

# Menambahkan Data
minumanku_list.append('Es Cendol')
print(minumanku_list)

minumanku_list.insert(2, 'Es Kelapa')
print(minumanku_list)

# Menggabungkan List
minumanku_list2 = ['Es Degan', 'Es Kopyor']
minumanku_list.extend(minumanku_list2)
print(minumanku_list)

# Mengganti data berdasarkan index
minumanku_list[0] = 'Es Teh Tawar'
print(minumanku_list)

# Remove
minumanku_list.pop()
print(minumanku_list)

minumanku_list.pop(0)
print(minumanku_list)

minumanku_list.remove('Es Kelapa')
print(minumanku_list)

# Clear List
minumanku_list.clear()
print(minumanku_list)





# Tuple
print('-'*25, 'TUPLE', '-'*25)


minumanku_tuple = ('Es Teh', 'Es Jeruk', 'Es Kopi')
print(minumanku_tuple)

print(minumanku_tuple[0])





# Sets
print('-'*25, 'SETS', '-'*25)

minumanku_sets = {'Es Kopi', 'Es Kelapa'}
minumanku_sets.add('Es Kopyor')
minumanku_sets.add('Es Degan')
print(minumanku_sets)


angka_sets = {1,1,2,3,4,5}
print(angka_sets)

angka_sets.add(10)
print(angka_sets)

angka_sets.add(2)
print(angka_sets)



# Dictionary
print('-'*25, 'DICTIONARY', '-'*25)

nilai_dict = {
    'a': 100,
    'b': 80,
    'c': 60,
    'd': 40,
    'e': 20
}

for nilai in nilai_dict.keys():
    print(nilai)
    
for nilai in nilai_dict.values():
    print(nilai)
    
for rating, nilai in nilai_dict.items():
    print(rating, nilai)
    
# for nilai in nilai_dict.copy():
#     print(nilai)

print(nilai_dict['b'])




# LIST 2D
print('-'*25, 'LIST 2D', '-'*25)

angka_list_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(angka_list_2d[2][2])