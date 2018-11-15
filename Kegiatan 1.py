x = {1:"Segitiga", 2:"Persegi", 3:"Persegi Panjang", 4:"Lingkaran", 5:"Jajaran Genjang"}
y = {"Segitiga":"L = 0.5 * a * t", "Persegi":"L = s ** 2", "Persegi Panjang":"L = p * 1", "Lingkaran":"L = pi * r ** 2", "Jajaran Genjang":"L = a * t"}
for i in range(6):
    if i == 1:
        print("1", x[1], y["Segitiga"])
    elif i == 2:
        print("2", x[2], y["Persegi"])
    elif i == 3:
        print("3", x[3], y["Persegi Panjang"])
    elif i == 4:
        print("4", x[4], y["Lingkaran"])
    elif i == 5:
        print("5", x[5], y["Jajaran Genjang"])
