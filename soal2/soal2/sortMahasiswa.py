import random
from dataMahasiswa import data
from fungsiMahasiswa import show_data, presensi_dummy, acak_data

data = data.copy()
presensi_dummy(data)
acak_data(data)



def sort_by(data: list=data, index: str="nim",rev = False):
    maps = {
        "nim":0,
        "nama":1,
        "presensi":2,
    }
    indek = maps[index]
    # Kerjakan disini
    n = len(data)
    for i in range(n-1):
        for j in range(n - i-1):
            if rev == False:
                if data[j][indek] > data [j+1][indek]:
                    data [j], data [j+1] = data [j+1], data[j]
            else:
                if data[j][indek] < data [j + 1][indek]:
                    data [j], data [j+1] = data [j+1], data[j]

    # Jangan Dihapus
    show_data(data)

sort_by(data, "presensi", rev = False)
sort_by(data, "nim", rev= False)
sort_by(data, "nama", rev = False)
