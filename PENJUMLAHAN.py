#
# TODO: MENGGUNAKAN CARA BIASA
# ! 1.
# number = 1, 2, 3, 4, 5
# amount = sum(number)
# average = amount / len(number)
# print(amount)
# print(average)
# ! 2.INPUTAN DARI USER
# input_user = [int(i) for i in input("Masukkan Bilangan : ").split(" ")]
# amount = sum(input_user)
# average = amount / len(input_user)
# print("Jumlah =", amount)
# print("dan Rata-Rata =", average)

# ! 2.INPUTAN DARI USER DAN DAPAT DIULANGI
# while True:
#     input_user = [int(i) for i in input("Masukkan Bilangan : ").split(" ")]
#     amount = sum(input_user)
#     average = amount / len(input_user)
#     print("Jumlah =", amount)
#     print("dan Rata-Rata =", average)
#     lanjut = input("Mau Melanjutkan? (y/n) : ")
#     if lanjut == "n":
#         break
# print("TERIMA KASIH")

# TODO: MENGGUNAKAN FUNGSI
def get_numbers():
    numbers = list(map(int, input("Masukkan Angka : ").split()))
    return numbers


def jumlah(*angka):
    total = 0
    for i in angka:
        total += i
    return total


def rata_rata(angka):
    amount = jumlah(*angka) / len(angka)
    return amount


def display(result, average):
    print(f"Jumlah = {result}")
    print(f"Rata-Rata = {average}")


while True:
    NUMBER = get_numbers()
    numbers = jumlah(*NUMBER)
    result = rata_rata(NUMBER)
    display(numbers, result)
    isLanjut = input("Coba Bilangan lain? (y/n) : ")
    if isLanjut == "n":
        break
print("TERIMA KASIH")
