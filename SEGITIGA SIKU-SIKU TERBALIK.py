star = 10
for i in range(0,star, +1):
    space = ""
    for j in range(0, i):
        space += " "
    asterisk = ""
    for k in range(star, i, -1):
        asterisk += "*"
    print(space+asterisk)