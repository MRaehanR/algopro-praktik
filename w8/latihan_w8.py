menu = [
    {
        'nama': 'Nasi Goreng',
        'harga': 15000
    },
    {
        'nama': 'Mie Goreng',
        'harga': 12000
    },
    {
        'nama': 'Ayam Geprek',
        'harga': 10000
    },
    {
        'nama': 'Es Teh',
        'harga': 2000
    }
]

pelanggan = input('Masukan Nama Pelanggan: ')


order = []
still_order = True
while still_order:
    print('='*25, 'MENU', '='*25)
    print('[1] Nasi Goreng')
    print('[2] Mie Goreng')
    print('[3] Ayam Geprek')
    print('[4] Es Teh')
    print('[0] Selesai')

    pilihan = int(input('Masukan Pilihan: '))

    if pilihan == 0:
        still_order = False

    order.append(pilihan)




