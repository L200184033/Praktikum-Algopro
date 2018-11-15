x = input("Masukkan Password : ")
if x == "Kemas":
    print("Anda Berhasil Login")
else:
    x = input("Maaf, Anda Salah Memeasukkan Password. Masukkan Password : ")
    if x == "Kemas":
        print("Anda Berhasil Login")
    else:
        x = input("Maaf, Anda Salah Memeasukkan Password. Masukkan Password : ")
        if x == "Kemas":
            print("Anda Berhasil Login")
        else:
            print("Anda Telah Mencoba 3 Kali, Akses Anda Ditolak")
