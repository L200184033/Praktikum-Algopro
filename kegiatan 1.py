from tkinter import*

my_app = Tk(className="Data diri")

L1 = Label(my_app, text="Data diri", font=("Arial", 24))
L1.grid(row=0, column=0, sticky=W)
L2 = Label(my_app, text="Nama")
L2.grid(row=1, column=0, sticky=W)
L3 = Label(my_app, text="Kemas Muhamad Kevin")
L3.grid(row=1, column=1, sticky=W)
L4 = Label(my_app, text="NIM")
L4.grid(row=2, column=0, sticky=W)
L5 = Label(my_app, text="L200184033")
L5.grid(row=2, column=1, sticky=W)
L6 = Label(my_app, text="Buku favorit")
L6.grid(row=3, column=0, sticky=W)
L7 = Label(my_app, text="Tokyo Ghoul")
L7.grid(row=3, column=1, sticky=W)
L8 = Label(my_app, text="Idola di kalangan sahabat")
L8.grid(row=4, column=0, sticky=W)
L9 = Label(my_app, text="Utsman bin Affan")
L9.grid(row=4, column=1, sticky=W)
L10 = Label(my_app, text="Motto")
L10.grid(row=5, column=0, sticky=W)
L11 = Label(my_app, text="Karna ku Selow")
L11.grid(row=5, column=1, sticky=W)

def tutup():
    my_app.destroy()

B1 = Button(my_app, text="Tutup", command=tutup)
B1.grid(row=6, column=1)

my_app.mainloop()
