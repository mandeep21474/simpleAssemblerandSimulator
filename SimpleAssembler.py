
"""
Co project A80
Lovleen Kumar Verma 2021471
Mandeep Singh Virdi 2021474
Arnav Gupta         2021453
"""
from sys import stdin
import sys
b = []
a = sys.stdin.readlines()
c = [i.rstrip() for i in a]
for k in c:
    if k != '':
        b.append(k)
Dict1 = {'add': '10000', 'sub': '10001', 'mov': ['10010', '10011'], 'ld': '10100', 'st': '10101', 'mul': '10110',
         'div': '10111', 'rs': '11000', 'ls': '11001', 'xor': '11010', 'or': '11011', 'and': '11100', 'not': '11101',
         'cmp': '11110', 'jmp': '11111', 'jlt': '01100', 'jgt': '01101', 'je': '01111', 'hlt': '01010'}

Dict2 = {'R0': '000', 'R1': '001', 'R2': '010', 'R3': '011', 'R4': '100', 'R5': '101', 'R6': '110'}

Dict_Type = {'add': 'A', 'sub': 'A', 'mov': ['B', 'C'], 'ld': 'D', 'st': 'D', 'mul': 'A',
             'div': 'C', 'rs': 'B', 'ls': 'B', 'xor': 'A', 'or': 'A', 'and': 'A', 'not': 'C',
             'cmp': 'C', 'jmp': 'E', 'jlt': 'E', 'jgt': 'E', 'je': 'E', 'hlt': 'F'}


def DB(x):
    l = []
    if x < 0:
        L = [str(i) for i in l]
        n = "".join(L)
        if len(n) < 8:
            n = [str(i) for i in n]
            d = 8 - len(n)
            for i in range(0, d):
                n.insert(i, "0")
            n = "".join(n)
        return n
    while x >= 2:
        d = x % 2
        l.append(d)
        x = x // 2
    l.append(x)
    l.reverse()
    L = [str(i) for i in l]
    n = "".join(L)
    if (len(n) < 8):
        n = [str(i) for i in n]
        d = 8 - len(n)
        for i in range(0, d):
            n.insert(i, "0")
        n = "".join(n)

    return n
Dict_fin = {}
lb = []
L = []
i = 0
c = 0
z = b[i]
z = z.split()
count = 0
count1 = 0
Count = 0
Count1 = 0
while z[0] == 'var':
    if len(z) > 2:
        sys.stdout.write(f"{count}Typos in instruction name or register name")
        c = 1
        break
    L.append(z[1])
    i = i + 1
    if i == len(b):
        sys.stdout.write("Missing hlt instruction")
        c = 1
        break
    z = b[i]
    z = z.split()
    count = i
    if (count > 256):
        sys.stdout.write(f"More Number of memory allocation than given")
        break
if c == 0:
    Count1 = 1
    Count = Count + 1
    for j in range(i, len(b)):
        y = b[j]
        y = y.split()
        if ":" in y[0]:
            z = y[0].split(':')
            if z[0] not in Dict_fin:
                Dict_fin[z[0]] = Count1
        Count1 = Count1 + 1
        Count = Count + 1
if c == 0:
    count1 = 1
    count = count + 1
    str1 = []
    for j in range(i, len(b)):
        if (count > 256):
            sys.stdout.write(f"More Number of memory allocation than given")
            str1.clear()
            break
        s = ""
        y = b[j]
        if j == len(b) - 1:
            p = y.split()
            if len(p) > 1:
                if p[1] == 'hlt':
                    str1.append('0101000000000000')
        if y == 'hlt' and j == len(b) - 1:
            str1.append('0101000000000000')
        if y != 'hlt' and j == len(b) - 1:
            p = y.split()
            if len(p) == 1:
                sys.stdout.write(f"Missing hlt instruction")
                str1.clear()
                break
            else:
                break
        if y == 'hlt' and j != len(b) - 1:
            sys.stdout.write(f"{count} hlt not declared at end")
            str1.clear()
            break
        else:
            y = y.split()
            if ":" in y[0]:
                if y[0].count(":") != 1:
                    sys.stdout.write(f" {count} Typos in instruction name or register name")
                    str1.clear()
                    break
                if y[0][-1] == ':':
                    z = y[0].split(':')
                    lb.append(z[0])
                    if z[0] in L:
                        sys.stdout.write(f"{count} Variables used in label")
                        str1.clear()
                        break
                    y.pop(0)
                    if y[0] == 'hlt':
                        sys.stdout.write(f"0101000000000000")
                        str1.clear()
                        break
            if Dict_Type.get(y[0], '-1') != '-1':
                type = Dict_Type[y[0]]
                if type == ['B', 'C']:
                    if y[2][0] == '$':
                        type = 'B'
                    else:
                        type = 'C'
            else:
                if y[0] == 'var':
                    sys.stdout.write(f"{count} Variables not declared at the beginning")
                    str1.clear()
                    break
                elif y[0] == 'hlt':
                    sys.stdout.write(f"{count} hlt not declared at end")
                    str1.clear()
                    break
                else:
                    sys.stdout.write(f" {count} Typos in instruction name or register name")
                    str1.clear()
                    break
            if type == 'A':
                if len(y) != 4:
                    sys.stdout.write(f" {count} Typos in instruction name or register name")
                    str1.clear()
                    break
                if Dict1.get(y[0], '-1') != '-1':
                    s = s + Dict1[y[0]]
                else:
                    sys.stdout.write(f"{count} Typos in instruction name or register name")
                    str1.clear()
                    break

                s = s + "00"
                if Dict2.get(y[1], '-1') != '-1':
                    s = s + Dict2[y[1]]
                else:
                    sys.stdout.write(f"{count} Typos in instruction name or register name")
                    str1.clear()
                    break
                if Dict2.get(y[2], '-1') != '-1':
                    s = s + Dict2[y[2]]
                else:
                    sys.stdout.write(f"{count} Typos in instruction name or register name")
                    str1.clear()
                    break
                if Dict2.get(y[3], '-1') != '-1':
                    s = s + Dict2[y[3]]
                else:
                    sys.stdout.write(f"{count} Typos in instruction name or register name")
                    str1.clear()
                    break
                str1.append(s)
                count = count + 1
                count1 = count1 +1
            elif type == 'C':
                if len(y) != 3:
                    sys.stdout.write(f"{count} Typos in instruction name or register name")
                    str1.clear()
                    break
                if Dict1.get(y[0], '-1') != '-1':
                    if y[0] == 'mov':
                        s = s + Dict1[y[0]][1]
                    else:
                        s = s + Dict1[y[0]]
                else:
                    sys.stdout.write(f"{count} Typos in instruction name or register name")
                    str1.clear()
                    break

                s = s + "00000"
                if Dict2.get(y[1], '-1') != '-1':
                    s = s + Dict2[y[1]]
                elif y[1] == 'FLAGS':
                    s = s + '111'
                else:
                    sys.stdout.write(f"{count} Typos in instruction name or register name")
                    str1.clear()
                    break
                if Dict2.get(y[2], '-1') != '-1':
                    s = s + Dict2[y[2]]
                else:
                    sys.stdout.write(f"{count} Typos in instruction name or register name")
                    str1.clear()
                    break
                str1.append(s)
                count = count + 1
                count1 = count1 + 1
            elif type == 'D':
                if len(y) != 3:
                    sys.stdout.write(f"{count} Typos in instruction name or register name")
                    str1.clear()
                    break
                if Dict1.get(y[0], '-1') != '-1':
                    s = s + Dict1[y[0]]
                else:
                    sys.stdout.write(f"{count} Typos in instruction name or register name")
                    str1.clear()
                    break
                if Dict2.get(y[1], '-1') != '-1':
                    s = s + Dict2[y[1]]
                else:
                    sys.stdout.write(f"{count} Typos in instruction name or register name")
                    str1.clear()
                    break
                if y[2] not in L:
                    sys.stdout.write(f"{count} Use of undefined variables")
                    str1.clear()
                    break
                else:
                    q = DB(count1 + L.index(y[2])+1)
                    s = s + q
                    str1.append(s)
                count1 = count1 + 1
                count = count + 1
            elif type == 'E':
                if len(y) != 2:
                    sys.stdout.write(f"{count} Typos in instruction name or register name")
                    str1.clear()
                    break
                if Dict1.get(y[0], '-1') != '-1':
                    s = s + Dict1[y[0]]
                else:
                    sys.stdout.write(f"{count} Typos in instruction name or register name")
                    str1.clear()
                    break
                s = s + '000'
                if y[1] not in Dict_fin:
                    sys.stdout.write(f"{count} Use of undefined labels")
                    str1.clear()
                    break
                else:
                    q = DB(Dict_fin[y[1]])
                    s = s + q
                    str1.append(s)
                count1 = count1 + 1
                count = count + 1
            elif type == 'B':
                if len(y) != 3:
                    sys.stdout.write(f"{count} Typos in instruction name or register name")
                    str1.clear()
                    break
                if Dict1.get(y[0], '-1') != '-1':
                    if y[0] == 'mov':  # y[0] = mov
                        s = s + Dict1[y[0]][0]
                    else:
                        s = s + Dict1[y[0]]
                else:
                    sys.stdout.write(f"{count} Typos in instruction name or register name")
                    str1.clear()
                    break
                if Dict2.get(y[1], '-1') != '-1':
                    s = s + Dict2[y[1]]
                else:
                    sys.stdout.write(f"{count} Typos in instruction name or register name")
                    str1.clear()
                    break
                # y[2] = $10
                if y[2][0] != '$':
                    sys.stdout.write(f"{count} Typos in instruction name or register name")
                    str1.clear()
                    break
                else:
                    z = y[2][1:]
                    z = int(z)
                    if z < 0 or z > 255:
                        print(f"{count} Illegal Immediate values")
                    else:
                        Y = DB(z)
                        s = s + Y
                        str1.append(s)
                if y != 'hlt' and j == len(b) - 1:
                    sys.stdout.write(f"Missing hlt instruction")
                    str1.clear()
                    break
                count1 = count1 + 1
                count = count + 1
    for p in str1:
        sys.stdout.write(p)
        sys.stdout.write("\n")
