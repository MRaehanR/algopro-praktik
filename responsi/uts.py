rekap_daerah = {
    "Sleman utara": {
        "id": 1,
        "deskripsi": "Mencakup 7 kelurahan",
        "hasil_suara": [1, 2, 1, 1, 2, 3, 1],
    },
    "Sleman selatan": {
        "id": 2,
        "deskripsi": "Mencakup 8 kelurahan",
        "hasil_suara": [1, 3, 3, 3, 2, 3, 2, 3],
    },
    "Sleman barat": {
        "id": 3,
        "deskripsi": "Mencakup 9 kelurahan",
        "hasil_suara": [1, 2, 2, 2, 2, 3, 3, 1, 2],
    },
}

kandidat = [
    {
        "id": 1,
        "nama": "Agus",
        "partai": "Harapan kita",
        "slogan": "Maju terus pantang mundur",
    },
    {
        "id": 2,
        "nama": "Budi",
        "partai": "Demokrasi bersama",
        "slogan": "Terus berinovasi untuk rakyat",
    },
    {
        "id": 3,
        "nama": "Cita",
        "partai": "Terang bulan",
        "slogan": "Terus terang, terang terus",
    },
]

def hitung_suara_terbanyak(rekap_daerah, kandidat):
    """
    lanjutkan codingan anda disini,
    fungsi ini akan mengembalikan dictionary nama daerah dengan value
    berisi nama kandidat yang mendapatkan suara terbanyak di daerah tersebut
    suara terbanyak dapat diperoleh dengan perulangan
    """

    results = {}

    for daerah in rekap_daerah:
        rekap_suara =  dict({})
        for suara in rekap_daerah[daerah]['hasil_suara']:
            if suara in rekap_suara.keys():
                rekap_suara[suara] += 1
            else:
                rekap_suara[suara] = 1
        max = 0
        for suara in rekap_suara:
            if rekap_suara[suara] > max:
                max = rekap_suara[suara]
                results[daerah] = suara

    for nama_kab in results:
        for kandidat_item in kandidat:
            if kandidat_item['id'] == results[nama_kab]:
                results[nama_kab] = kandidat_item['nama']


            
    return results

def tambah_daerah(nama_kab, deskripsi, hasil_suara):
    """
    lanjutkan codingan anda disini,
    fungsi ini akan membalikkan nilai dictionary rekap_daerah dengan nilai daerah baru
    id akan terisi otomatis sesuai penomoran sebelumnya
    jika nama_kab sudah ada maka return "Nama kabupaten sudah ada"
    """

    id = list(rekap_daerah.values())[-1]['id']+1

    if nama_kab in rekap_daerah:
        return "Nama Kabupaten Sudah Ada!"
    
    else:
        rekap_daerah[nama_kab] = dict(
            {
                "id": id,
                "deskripsi": deskripsi,
                "hasil_suara": hasil_suara,
            },
        )
    return rekap_daerah

print(hitung_suara_terbanyak(rekap_daerah, kandidat))
# output: {'Sleman utara': 'Agus', 'Sleman selatan': 'Cita', 'Sleman barat': 'Budi', 'Sleman timur': 'Agus'}

print(tambah_daerah("Sleman timur", "Mencakup 6 kelurahan", [1, 2, 1, 1, 1, 2]))
"""
output: {'Sleman utara': {'id': 1, 'deskripsi': 'Mencakup 7 kelurahan', 'hasil_suara': [1, 2, 1, 1, 2, 3, 1]}, 'Sleman selatan': {'id': 2, 'deskripsi': 'Mencakup 8 kelurahan', 'hasil_suara': [1, 3, 3, 3, 2, 3, 2, 3]},
'Sleman barat': {'id': 3, 'deskripsi': 'Mencakup 9 kelurahan', 'hasil_suara': [1, 2, 2, 2, 2, 3, 3, 1, 2]}, 
'Sleman timur': {'id': 4, 'deskripsi': 'Mencakup 6 kelurahan', 'hasil_suara': [1, 2, 1, 1, 1, 2] }
"""