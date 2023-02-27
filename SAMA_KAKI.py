#
# TODO: MEMBUAT SEGITIGA SAMA KAKI
# ! CARA 1
# ? TIDAK DISARANKAN
result = ""
for i in range(1, 11):
    for j in range(10-i):
        result += " "
    for k in range(i*2-1):
        result += "*"
    result += "\n"
print(result)


# ! CARA 2
for i in range(1, 11):
    spasi = ""
    for j in range(10-i):
        spasi += " "
    bintang = ""
    for k in range(i * 2 - 1):
        bintang += "*"
    print(spasi+bintang)


# ! CARA 3
for i in range(1, 11):
    print(" " * (10-i) + "*" * (i*2-1))
