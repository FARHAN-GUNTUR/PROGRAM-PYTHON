star = 10
for i in range(star, 0, -1):
    space = ""
    for j in range(0, i):
        space += " "
    asterisk = ""
    for k in range(star-i+1):
        asterisk += "*"
    print(space+asterisk)
for i in range(1, star, +1):
    space = ""
    for j in range(0, i+1):
        space += " "
    asterisk = ""
    for k in range(star, i, -1):
        asterisk += "*"
    print(space+asterisk)
# star = 10
for i in range(star, 0, -1):
    print(" " * (i) + "*" * (star-i+1))
for i in range(1, star+1):
    print(" " * (i) + "*" * (star-i+1))
