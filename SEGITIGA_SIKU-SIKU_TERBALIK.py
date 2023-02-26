#
# ! CARA 1
star = 10
for i in range(0,star):
    space = ""
    for j in range(0, i):
        space += " "
    asterisk = ""
    for k in range(star, i, -1):
        asterisk += "*"
    print(space+asterisk)
# ! CARA 2
stars = 10
for i in range(stars):
    print(" " * i + "*" * (stars - i))
