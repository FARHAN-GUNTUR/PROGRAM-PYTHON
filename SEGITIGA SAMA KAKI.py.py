hasil = ""
row = 8
for i in range(1, row):
    for j in range(row-i):
        hasil += ' '
    for k in range(i * 2 - 1):
        hasil += '*'
    hasil += "\n"
print(hasil)
