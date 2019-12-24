def vol(r):
    volume = (4/3)*3.14*(r**3)
    return volume
n = int(input("Enter radius :"))
c = vol(n)
print("The volume of the sphere : {}".format(c))