## Program Akun
## Dibuat oleh Kemas L200184033
import random
angka = random.randint(0,1000)

Nama = 'Kemas Muhamad Kevin'
TanggalLahir = '9 Februari 2000'
NamaSingkat = Nama[0] + '. ' + Nama[6] + '. ' + Nama[14:19]
Username = Nama[0] + TanggalLahir[0] + TanggalLahir[11:15]
Password = Nama[0:4] + str(angka)
