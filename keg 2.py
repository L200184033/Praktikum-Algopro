##Activities 2, Kemas Muhamad Kevin
berkas = open("L200184033","w")
berkas.write("L200184033 \n")
berkas.write("09-02-2000 \n")
berkas.write("Kemas Muhamad Kevin \n")
berkas.write("Purworejo \n")
berkas.close()

import shelve
a = open("L200184033","r")
NIM = a.readline()
TL = a.readline()
Nama = a.readline()
Kota = a.readline()
a.close()

a = shelve.open("Kemas")
a['b'] = [Nama, Kota, TL, NIM]
a.close()

a = shelve.open("Kemas")
 
print (a['b'][0])
print (a['b'][1])
print (a['b'][2])
print (a['b'][3])
