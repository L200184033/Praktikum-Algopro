##Activities 3, Kemas Muhamad Kevin
import shelve

data = open("L200184033", "r")
NIM = data.readline()
TL = data.readline()
Nama = data.readline()
Kota = data.readline()
data.close()

data = shelve.open("Kemas")
data["newdata"] = [NIM, TL, Nama, Kota]
data.close()
