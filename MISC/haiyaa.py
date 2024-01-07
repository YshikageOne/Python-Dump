data = [5, 3, 7]

def displaydata(x):
    print("data[2] :" , x[2])
    print("data[-1] :" , x[-1])
    print("len(data) :", len(data))
    print("data[0:2] :", x[0:2])
    print("data+[2,10,5] :", x+[2,10,5])
    print("tuple(data) :", tuple(x))

def changedata(x):
   x[0] = -x[0]
   x.insert(3,10)
   x.insert(2,22)
   x.remove(x[1])
   x.sort()
   print(x)




displaydata(data)
changedata(data)