n1 = int(input("Kérek egy számot: "))
n2 = int(input("Kérek egy másik számot: "))
def sorozat():
    otrevegzodo = 0
    for j in range(n1,n2, 1):
        if j % 2 != 0:
            print("\t",j,end="#")
        if j % 5 == 0 and j % 10 != 0:
            otrevegzodo += 1
        j+=1
    print("\t",otrevegzodo,"db 5-re végződő szám van")