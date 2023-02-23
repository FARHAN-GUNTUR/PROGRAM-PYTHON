#
# ! 1.
# def prima(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# angka = 1
# if prima(angka):
#     print(f"{angka} adalah bilangan prima")
# else:
#     print(f"{angka} bukan bilangan prima")

# ! 2. DARI INPUTAN USER
# def prima(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# input_user = int(input("Masukkan angka : "))
# if prima(input_user):
#     print(f"{input_user} adalah bilangan prima")
# else:
#     print(f"{input_user} bukan bilangan prima")

# ! 2. DARI INPUTAN USER DAN BISA DIULANGI SECARA TERUS MENERUS

# def prima(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# while True:
#     input_user = int(input("Masukkan angka : "))
#     if prima(input_user):
#         print(f"{input_user} adalah bilangan prima")
#     else:
#         print(f"{input_user} bukan bilangan prima")
#     isLanjut = input("Mau mencoba angka lain? (y/n) : ")
#     if isLanjut == "n":
#         break
# print("TERIMA KASIH")
