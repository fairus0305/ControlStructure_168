a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))
c = float(input("Masukkan angka ketiga: "))

if a > b and a > c: 
    largest = a
    print ('yang paling besar = ', largest)
elif b > a and b > c:
    largest = b
    print ('yang paling besar = ', largest)
elif c > a and c > b:
    largest = c
    print ('yang paling besar = ', largest)
else:
    print ('gada yang paling besar')
