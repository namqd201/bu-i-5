a = int(input("Nhập một số nguyên có 3 chữ số: "))
b = a % 10
c = (a // 10) % 10
d = a // 100
tong = b + c + d
print(b, "+", c, "+", d, "=", tong)
