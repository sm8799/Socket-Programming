i = 97
d = {}
while i<=122:
    c = chr(i - 97)
    d[i - 97] = c
    i += 1
s = str(input())
for i in range(25):
    out = ''
    for j in s:
        if j == ' ':
            out = out + j
        else:
            c = (ord(j) - 97 - i) % 26
            out = out + chr(c + 97)
    print(out)
