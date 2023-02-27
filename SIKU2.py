#
# TODO: MEMBUAT SEGITIGA SIKU-SIKU KE-2
# ! CARA 1
bintang = ""
for i in range(10, 0, -1):
    for j in range(1, i):
        bintang += " "
    for k in range(11, i, -1):
        bintang += "*"
    bintang += "\n"
print(bintang)


# ! CARA 2
# ? TIDAK DISARANKAN
for i in range(10, 0, -1):
    spasi = ""
    for j in range(1, i):
        spasi += " "
    bintang = ""
    for k in range(11, i, -1):
        bintang += "*"
    print(spasi + bintang)


# ! CARA 3
for i in range(10, 0, -1):
    print(" " * (i-1) + "*" * (11-i))
