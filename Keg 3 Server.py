import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50005))
s.listen(5)
print"Server sudah siap"
perintah = "
r=0
while perintah !='keluar':
    komm, addr = s.accept()
    while perintah !='keluar':
        data = komm.recv(1024).lower().split("=")
        perintah = data[0]
        if perintah == 'keluar':
            s.close()
            break
        print 'Pesan:', perintah
        if len(data) == 1:
            if perintah == 'jari-jari':
                r = int(data[1])
                respon = "jari-jari dicatat"
                komm.send(respon)
            else:
                komm.send('pesan tidak diketahui')
        elif perintah == 'hitung':
            L = float(3*22/7*r*r)
            respon = "Luas bola dengan jari-jari {} adalah {}".format(r,L)
            komm.send(respon)
        else:
            komm.send('pesan tidak diketahui')
