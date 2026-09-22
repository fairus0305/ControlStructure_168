n = int(input("Masukkan nilai n: "))

a = 0
b = 1
i = 0

print("Deret Fibonacci:")

while i < n:
    print(a)
    a, b = b, a + b
    i += 1