def input_user():
    sisi = int(input("Panjang Sisi Kubus : "))
    return sisi


def luas_kubus(sisi):
    hasil = 6*(sisi**2)
    return hasil


def display(value, key):
    print(f"Panjang Sisi Kubus = {value}\nLuas = {key}")


SISI = input_user()
luas = luas_kubus(SISI)
display(SISI, luas)

# ? INPUTAN YANG BISA DIULANGI
# while True:
# SISI = input_user()
# luas = luas_kubus(SISI)
# display(SISI, luas)
#     lanjut = input("Mau Melanjutkan? (y/n): ")
#     if lanjut == "n":
#         break
# print("TERIMA KASIH")
