# rows = int(input("Masukan Rows: "))
# columns = int(input("Masukan columns: "))



# for row in range(rows):
#     # print(f'row = {row}')
#     for column in range(columns):
#         # print(f'column = {column}')
#         if column % 2 == 0:
#             print('x', end='')
#         else:
#             print('o', end='')
#     print('')
    
    


# for row in range(rows):
#     for column in range(columns):
#         if  row % 2 == 0 :
#             print('x', end='')
#         else:
#             print('o', end='')
#     print('')


rows = 3
columns = 3
    
for row in range(rows):
    for column in range(columns):
        if column % 2 == 0:
            print('x', end='')
        else:
            print('o', end='')
    print('')
    
print('-'*40)

for row in range(rows):
    for column in range(columns):
        if column % 2 == 0 and row % 2 == 0 or column % 2 == 1 and row % 2 == 1:
            print('x', end='')
        else:
            print('o', end='')
    print('')
    
    
print('-'*40)
    
for row in range(rows):
    for column in range(columns):
        if column == row:
            print('*', end='')
        elif column % 2 == 0 and row % 2 == 0 or column % 2 == 1 and row % 2 == 1:
            print('x', end='')
        else:
            print('o', end='')
    print('')