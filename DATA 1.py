# def print_values(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")


# while True:
#     input_data = input(
#         "Enter values in key=value format, separated by comma: ")
#     data = dict(item.split("=") for item in input_data.split(","))
#     for index, i in enumerate(data):
#         print_values(**data)
#     lanjut = input("Mau Lanjut Bro? (y/n) : ")
#     if lanjut == "y":
#         continue
#     else:
#         break
# data_mahasiswa = []
# while True:
#     nama = input("Siapa Nama Anda? : ")
#     umur = int(input("Berapa Usia Anda? : "))
#     asal = input("Kota Asal? : ")
#! data = {
#!     'nama': nama,
#!     'umur': umur,
#!     'asal': asal,
#! }
#! data_mahasiswa.append(data)
#     data_mahasiswa.append({'nama': nama, 'umur': umur, 'asal': asal})
#     for index, mahasiswa in enumerate(data_mahasiswa):
#         print(
#             f"{index+1}.Nama = {mahasiswa['nama']}\nUsia = {mahasiswa['umur']}\nAsal = {mahasiswa['asal']}")
#     lanjut = input("Mau Memasukkan Data Yang Lain? (y/n): ")
#     if lanjut == "n":
#         break
# print("Terima Kasih")

# data_mahasiswa = []
# while True:
#     data = {
#         'nama': input("Siapa Nama Kamu? : "),
#         'umur': int(input("Berapa Umurmu? : ")),
#         'alamat': input("Alamat Saat Ini? : ")
#     }
#     data_mahasiswa.append(data)
#     for index, mahasiswa in enumerate(data_mahasiswa):
#         print(
#             f"{index+1}.Nama = {mahasiswa['nama']}\nUmur = {mahasiswa['umur']}\nAlamat = {mahasiswa['alamat']}")

#     lanjut = input("Mau Melanjutkan bro? (y/n) : ")

#     if lanjut == "n":
#         break
data_mahasiswa = []
while True:
    nama = input("Siapa Nama Kamu? : ")
    umur = int(input("Berapa Umurmu? : "))
    alamat = input("Alamat Saat Ini? : ")
    data_mahasiswa.append({'nama': nama, 'umur': umur, 'alamat': alamat})
    for index, mahasiswa in enumerate(data_mahasiswa):
        print(
            f"{index+1}.Nama = {mahasiswa['nama']}\nUmur = {mahasiswa['umur']}\nAlamat = {mahasiswa['alamat']}")

    lanjut = input("Mau Melanjutkan bro? (y/n) : ")

    if lanjut == "n":
        break
