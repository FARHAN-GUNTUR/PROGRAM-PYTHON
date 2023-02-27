#
# TODO: MEMBUAT SEGITIGA SIKU-SIKU
# ! CARA 1
spasi = ""
for i in range(1, 10):
    for j in range(0, i):
        spasi += "*"
    spasi += "\n"
print(spasi)

# ! CARA 2
for i in range(1, 11):
    spasi = ""
    for j in range(0, i):
        spasi += "*"
    print(spasi)


# ! CARA 3
for i in range(1, 11):
    print("*" * i)
