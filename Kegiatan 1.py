Data = {"NIM":"L200184033", "Nama":"Kemas Muhamad Kevin", "Tempat/Tanggal_Lahir":"Palembang / 9 February 2000", "Jenis_Kelamin":"Laki - laki", "Golongan_Darah":"O", "Alamat":"Besole, Bayan, Purworejo", "Agama":"Islam", "Status_Perkawinan":"Belum Kawin", "Pekerjaan":"Mahasiswa", "Kewarganegaraan":"Indonesia"}
NIM = Data["NIM"]
Nama = Data["Nama"]
TTL = Data["Tempat/Tanggal_Lahir"]
JK = Data["Jenis_Kelamin"]
GD = Data["Golongan_Darah"]
Alamat = Data["Alamat"]
Agama = Data["Agama"]
SP = Data["Status_Perkawinan"]
Pekerjaan = Data["Pekerjaan"]
Kewarganegaraan = Data["Kewarganegaraan"]

print("Pilihan Yang Tersedia:")
print("f menampilkan bantuan ini")
print("z menampilkan NIM")
print("x menampilkan Nama")
print("c menampilkan Tempat/Tanggal Lahir")
print("v menampilkan Jenis Kelamin")
print("b menampilkan Golongan Darah")
print("n menampilkan Alamat")
print("m menampilkan Agama")
print("a menampilkan Status Perkawinan")
print("s menampilkan Pekerjaan")
print("d menampilkan Kewarganegaraan")
print("g untuk keluar")
print(" ")

f ='''Pilihan Yang Tersedia:
f menampilkan bantuan ini
z menampilkan NIM
x menampilkan Nama
c menampilkan Tempat/Tanggal Lahir
v menampilkan Jenis Kelamin
b menampilkan Golongan Darah
n menampilkan Alamat
m menampilkan Agama
a menampilkan Status Perkawinan
s menampilkan Pekerjaan
d menampilkan Kewarganegaraan
g untuk keluar'''

g = "Terima Kasih"
w = input("Masukkan huruf: ")
while w != "g":
    if w == "f":
        print(f)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "z":
        print(NIM)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "x":
        print(Nama)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "c":
        print(TTL)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "v":
        print(JK)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "b":
        print(GD)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "n":
        print(Alamat)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "m":
        print(Agama)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "a":
        print(SP)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "s":
        print(Pekerjaan)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "d":
        print(Kewarganegaraan)
        print(" ")
        w = input("Masukkan huruf: ")
    else:
        print("perintah tidak dikenal")
        print(" ")
        w = input("Masukkan huruf: ")
print(g)

