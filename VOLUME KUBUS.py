# def volume(sisi):
#     hasil = sisi**3
#     return hasil


# volume_kubus = volume(5)
# print("Volume Kubus = ", volume_kubus)

# ! MEMASUKKAN INPUTAN DARI USER


# def volume(sisi):
#     hasil = sisi**3
#     return hasil


# input_user = int(input("Panjang Sisi Kubus : "))
# volume_kubus = volume(input_user)
# print(f"Panjang Sisi Kubus = {input_user}\nVolume = {volume_kubus}")


# ! MEMASUKKAN INPUTAN DARI USER DAN DAPAT DIULANGI
# ? CARA 1
# def volume(sisi):
#     hasil = sisi**3
#     return hasil


# def display(inputan, hasil_volume):
#     print(f"Panjang Sisi Kubus = {inputan}\nVolume = {hasil_volume}")


# while True:
#     input_user = int(input("Panjang Sisi Kubus : "))
#     volume_kubus = volume(input_user)
#     display(input_user, volume_kubus)
#     print("="*25)
#     lanjut = input("Mau Mencoba Lagi? (y/n) : ")
#     if lanjut == "n":
#         break
# print("TERIMA KASIH")


# ? CARA 2
def input_user():
    sisi = int(input("Panjang Sisi Kubus : "))
    return sisi


def volume(sisi):
    hasil = sisi**3
    return hasil


def display(inputan, hasil_volume):
    print(f"Panjang Sisi Kubus = {inputan}\nVolume = {hasil_volume}")


while True:
    SISI = input_user()
    volume_kubus = volume(SISI)
    display(SISI, volume_kubus)
    print("="*25)
    lanjut = input("Mau Mencoba Lagi? (y/n) : ")
    if lanjut == "n":
        break
print("TERIMA KASIH")
