def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c
    

angka1 = int(input("Masukan Angka 1: "))
angka2 = int(input("Masukan Angka 2: "))
angka3 = int(input("Masukan Angka 3: "))

print(f"Maka, max_of_threenya adalah: {max_of_three(angka1, angka2, angka3)}")