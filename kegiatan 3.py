from tkinter import*

my_app = Tk(className='kalkulator sederhana')

L1 = Label(my_app, text='Bangun Geometri', font=('Arial', 24))
L1.grid(row=0, column=0)

L2 = Label(my_app, text='Deskripsi tentang bola, antara lain nama, dimensi, contoh benda, dan lain-lain.')
L2.grid(row=1, column=0)

L3 = Label(my_app, text='Jari-Jari : ')
L3.grid(row=2, column=0)
str1 = StringVar()
E1 = Entry(my_app, textvariable=str1)
E1.grid(row=2, column=1)

L5 = Label(my_app, text='Hasil = ')
L5.grid(row=3, column=0)
L6 = Label(my_app, text='0')
L6.grid(row=3, column=1)

def area():
    s = float(str1.get())
    result = 4*3.14*(s*s)
    L6.config (text=result)
    

B1 = Button(my_app, text='Hitung luas', command=area)
B1.grid(row=3,column=0)

my_app.mainloop()
