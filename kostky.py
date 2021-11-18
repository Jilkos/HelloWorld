import random
a=random.randint(1,6)
b=random.randint(1,6)
c=random.randint(1,6)
print("Hráč A hodil hodnotu", a)
print("Hráč B hodil hodnotu", b)
print("Hráč C hodil hodnotu", c)
if ((a>b) and (a>c)):
    print("Vyhrál hráč A")
elif((b>a) and (b>c)):
    print("Vyhrál hráč B")
elif((c>a) and (c>b)):
    print("Vyhrál hráč C")
elif ((a==b) and (a!=c) and (b!=c))  or ((a==c) and (a!=b) and (c!=b)) or ((b==c) and (b!=a) and (c!=a)):
    if (a==b):
        print("Vyhrál hráč A a hráč B")
    elif(b==c):
        print("Vyhrál hráč B a hráč C")
    else:
        print("Vyhrál hráč A a hráč C")
else:
    print("Hráči A, B a hráč C mají stejnou hodnotu, tudíž vyhrávají všichni")


