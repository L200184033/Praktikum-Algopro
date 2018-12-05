##Activities 4, Kemas Muhamad Kevin
import shelve

data = shelve.open("Kemas")
print(data["newdata"][0])
print(data["newdata"][1])
print(data["newdata"][2])
print(data["newdata"][3])
