price = 1000000
good_cred = True

if good_cred :
    price= (10 * 10000)
    print ("please play  the following amount")
    print (price)
else:
    price= (20*10000)
    print("please pay this amount")
    print(price)

names=input("enter youe name : ")
if len(names)<=2 :
    print("name too short")
elif len(names)> 49 :
    print("name too long")
else:print("name is okay!")
