hasil = ""
row = 10
for i in range(1, row):
    for j in range(row-i):
        hasil += ' '
    for k in range(i * 2 - 1):
        hasil += '*'
    hasil += "\n"
print(hasil)
for i in range(row, 1, -1):
    for j in range(row, i, -1):
        hasil += ' '
    for k in range(i * 2 - 1):
        hasil += '*'
    hasil += "\n"
print(hasil)
# for i in range(1, row):
#     hasil += ' ' * (row - i)
#     hasil += '*' * (i * 2 - 1) + "\n"
# for i in range(row, 0, -1):
#     hasil += ' ' * (row - i)
#     hasil += '*' * (i * 2 - 1) + "\n"
# print(hasil)
