menu1_name = "Nasi Ayam Geprek"
menu1_porsi = 1
menu1_harga = 12

menu2_name = "Nasi Ayam Kremes"
menu2_porsi = 2
menu2_harga = 15
total = (menu1_porsi*menu1_harga) + (menu2_porsi*menu2_harga)

print('-'*25)
print(menu1_name)
print(f"{menu1_porsi} x {menu1_harga:.3f}")
print(f"Rp{menu1_porsi*menu1_harga:.3f}")

print(menu2_name)
print(f"{menu2_porsi} x {menu2_harga:.3f}")
print(f"Rp{menu2_porsi*menu2_harga:.3f}")
print('-'*25)
print(f"Total : Rp{total:.3f}")