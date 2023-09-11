x = float(input("Panjang Sisi X: "))
y = float(input("Panjang sisi Y: "))
z = (x**2 + y**2)**0.5

luas = 1/2 * y * x
keliling = x + y + z

print(round(luas,2))
print(round(keliling,2))