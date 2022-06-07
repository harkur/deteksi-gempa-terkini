import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """

    Tanggal: 07 Juni 2022
    Waktu:   13:03:13 WIB
    Magnitudo: 4.6
    Kedalaman: 10 km
    Lokasi: LS=8.17 BT= - 117.31 BT
    Pusat Gempa: Pusat gempa berada di laut 37 km Barat Laut Sumbawa
    dirasakan: Dirasakan (Skala MMI): II - III Sumbawa
    :return:
    """
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None

    if content.status_code == 200:
         soup = BeautifulSoup(content.text, 'html.parser')
         result = soup.find('span', {'class': 'waktu'})
         result = result.text.split(', ')
         waktu = result[1]
         tanggal = result[0]


    hasil = dict()
    hasil['tanggal'] = tanggal #'07 Juni 2022'
    hasil['waktu'] = waktu #'13:03:13 WIB'
    hasil['magnitudo'] = '4.6'
    hasil['lokasi'] = {'ls': 8.17, 'bt': - 117.31}
    hasil['pusat'] = 'Pusat gempa berada di laut 37 km Barat Laut Sumbawa'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II - III Sumbawa'
    print(hasil)

    return hasil


def tampilkan_data(result):
    if result is None:
        print("Tidak Bisa Menemukan Data Gempa Terkini")
        return

    print('\nGempa Terakhir Berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi LS={result['lokasi']['ls']},BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")


if __name__ == '__main__':
    print('Ini Adalah package gempaterkini')
