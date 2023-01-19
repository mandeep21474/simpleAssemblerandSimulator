import os
import collections
"""
Co project A80
Lovleen Kumar Verma 2021471
Mandeep Singh Virdi 2021474
Arnav Gupta         2021453
"""

from sys import stdin
import sys

a = sys.stdin.read().rstrip().split()
b = [i.rstrip() for i in a]

def db(x):
    l=[]
    r=bin(x)
    r=r[2:]
    for i in r:
        l.append(i)
    if(len(l)<8):
        d=8-len(l)
        for i in range(0, d):
            l.insert(i, '0')
    return "".join(l)

def tc(x):  ## recieves bin number
    l = []
    rrl = []
    if x[0] != "-":
        r = x[2:]
        for i in r:
            l.append(i)
        if (len(l) < 16):
            d = 16 - len(l)
            for j in range(0, d):
                l.insert(j, '0')
        return "".join(l)
    elif (x[0] == "-"):
        r = x[3:]
        for i in r:
            l.append(i)
        l.insert(0, "1")
        for i in range(1, len(l)):
            if l[i] == "0":
                l[i] = "1"
            else:
                l[i] = "0"
        rl = "".join(l)
        t = int(rl, 2)
        t = t + int("1", 2)
        li = bin(t)
        y = li[2:]  ## return
        for i in y:
            rrl.append(i)
        if len(rrl) < 16:
            d = 16 - len(rrl)
        for i in range(0, d):
            rrl.insert(i, y[0])
        return "".join(rrl)
Lst = []
Dict = {}
for j in range(len(b)):
    if b[j][0:5] == '11111' or b[j][0:5] == '01100' or b[j][0:5] == '01101':
        Lst.append(b[j][8:16])
    Dict[j] = b[j]
pc = 0

Dict_Type = {'add': 'A', 'sub': 'A', 'movB': 'B', 'movC': 'C', 'ld': 'D', 'st': 'D', 'mul': 'A',
             'div': 'C', 'rs': 'B', 'ls': 'B', 'xor': 'A', 'or': 'A', 'and': 'A', 'not': 'C',
             'cmp': 'C', 'jmp': 'E', 'jlt': 'E', 'jgt': 'E', 'je': 'E', 'hlt': 'F'}

Dict_opcode = {'10000': 'add', '10001': 'sub', '10010': 'movB', '10011': 'movC', '10100': 'ld', '10101': 'st', '10110': 'mul',
                '10111': 'div', '11000': 'rs', '11001':  'ls', '11010':  'xor', '11011': 'or', '11100': 'and', '11101': 'not',
                '11110': 'cmp', '11111': 'jmp', '01100': 'jlt', '01101': 'jgt', '01111': 'je', '01010': 'hlt'}

Dict2_regval = {"R0": '0000000000000000', "R1": '0000000000000000', "R2": '0000000000000000', "R3": '0000000000000000',
         "R4": '0000000000000000', "R5": '0000000000000000', "R6": '0000000000000000', 'FLAGS': "0000000000000000"}

Dict_reg = {'000': 'R0', '001': 'R1', '010': 'R2', '011': 'R3', '100': 'R4', '101': 'R5', '110': 'R6', '111': 'FLAGS'}
Dict_mem_Add = {}
str = []
lp = []
Flags = '00000000000000'
count = 0
while pc < 256:
    st = ''
    inst = Dict[pc]
    opcode = inst[0:5]
    if opcode == '01010':
        st = st + db(pc) + ' ' + Dict2_regval['R0'] + ' ' + Dict2_regval['R1'] + ' ' + Dict2_regval['R2'] + ' ' + \
             Dict2_regval['R3'] + ' ' + Dict2_regval['R4'] + ' ' + Dict2_regval['R5'] + ' ' + Dict2_regval['R6'] + ' ' + \
             Dict2_regval['FLAGS']
        str.append(st)
        break
    b = Dict_opcode[opcode]
    type = Dict_Type[b]
    if type == 'A':
        reg1 = Dict_reg[inst[7:10]]
        reg2 = Dict_reg[inst[10:13]]
        reg3 = Dict_reg[inst[13:16]]
        if Dict_opcode[opcode] == 'add':
            lent = len(tc(bin((int(Dict2_regval[reg2], 2) + int(Dict2_regval[reg1], 2)))))
            if lent > 16:
                Dict2_regval["FLAGS"] = "0000000000010000"
            Dict2_regval[reg3] = tc(bin((int(Dict2_regval[reg2], 2) + int(Dict2_regval[reg1], 2))& (2**16-1)))
        elif Dict_opcode[opcode] == 'sub':
            lent = len(tc(bin((int(Dict2_regval[reg2], 2) - int(Dict2_regval[reg1], 2)))))
            if lent > 16:
                Dict2_regval["FLAGS"] = "0000000000010000"
            if Dict2_regval[reg2] > Dict2_regval[reg1]:
                Dict2_regval[reg3] = '0000000000000000'
            else:
                Dict2_regval[reg3] = tc(bin((int(Dict2_regval[reg1], 2) - int(Dict2_regval[reg2], 2))& (2**16-1)))
        elif Dict_opcode[opcode] == 'mul':
            lent = len(tc(bin((int(Dict2_regval[reg2], 2) * int(Dict2_regval[reg1], 2)))))
            if lent > 16:
                Dict2_regval["FLAGS"] = "0000000000010000"
            Dict2_regval[reg3] = tc(bin((int(Dict2_regval[reg2], 2) * int(Dict2_regval[reg1], 2))& (2**16-1)))
        elif Dict_opcode[opcode] == 'xor':
            lent = len(tc(bin((int(Dict2_regval[reg2], 2) ^ int(Dict2_regval[reg1], 2)))))
            if lent > 16:
                Dict2_regval["FLAGS"] = "0000000000010000"
            Dict2_regval[reg3] = tc(bin((int(Dict2_regval[reg2], 2) ^ int(Dict2_regval[reg1], 2))& (2**16-1)))
        elif Dict_opcode[opcode] == 'or':
            lent = len(tc(bin((int(Dict2_regval[reg2], 2) | int(Dict2_regval[reg1], 2)))))
            if lent > 16:
                Dict2_regval["FLAGS"] = "0000000000010000"
            Dict2_regval[reg3] = tc(bin((int(Dict2_regval[reg2], 2) | int(Dict2_regval[reg1], 2))& (2**16-1)))
        elif Dict_opcode[opcode] == 'and':
            lent = len(tc(bin((int(Dict2_regval[reg2], 2) & int(Dict2_regval[reg1], 2)))))
            if lent > 16:
                Dict2_regval["FLAGS"] = "0000000000010000"
            Dict2_regval[reg3] = tc(bin((int(Dict2_regval[reg2], 2) & int(Dict2_regval[reg1], 2))& (2**16-1)))
        st = st + db(pc) + ' ' + Dict2_regval['R0'] + ' ' + Dict2_regval['R1'] + ' ' + Dict2_regval['R2'] + ' ' + Dict2_regval['R3'] + ' ' + Dict2_regval['R4'] + ' ' + Dict2_regval['R5'] + ' ' + Dict2_regval['R6'] + ' ' + Dict2_regval['FLAGS']
        str.append(st)
        pc = pc + 1
    elif type == 'B':
        reg1 = Dict_reg[inst[5:8]]
        imm = inst[8:16]
        if Dict_opcode[opcode] == 'movB':
            Dict2_regval[reg1] = tc(bin(int(imm, 2)))
        elif Dict_opcode[opcode] == 'rs':
            Dict2_regval[reg1] = tc(bin((int(Dict2_regval[reg1], 2) >> int(imm, 2))& (2**16-1)))
        else:
            Dict2_regval[reg1] = tc(bin((int(Dict2_regval[reg1], 2) << int(imm, 2))& (2**16-1)))
            lent = len(tc(bin((int(Dict2_regval[reg1], 2) << int(imm, 2)))))
            if lent > 16:
                Dict2_regval["FLAGS"] = "0000000000010000"
        st = st + db(pc) + ' ' + Dict2_regval['R0'] + ' ' + Dict2_regval['R1'] + ' ' + Dict2_regval['R2'] + ' ' + Dict2_regval['R3'] + ' ' + Dict2_regval['R4'] + ' ' + Dict2_regval['R5'] + ' ' + Dict2_regval['R6'] + ' ' + Dict2_regval['FLAGS']
        str.append(st)
        pc = pc + 1
    elif type == "C":
        reg1 = Dict_reg[inst[10:13]]
        reg2 = Dict_reg[inst[13:16]]
        if Dict_opcode[opcode] == "mov":
            Dict2_regval[reg2] = Dict2_regval[reg1]
        elif Dict_opcode[opcode] == "div":
            Dict2_regval["R0"] = tc(bin((int(int(Dict2_regval[reg1], 2) / int(Dict2_regval[reg2], 2)))& (2**16-1)))
            lent = len(tc(bin(int(int(Dict2_regval[reg1], 2) / int(Dict2_regval[reg2], 2)))))
            if lent > 16:
                Dict2_regval["FLAGS"] = "0000000000010000"
            Dict2_regval["R1"] = tc(bin((int(int(Dict2_regval[reg1], 2) % int(Dict2_regval[reg2], 2)))& (2**16-1)))
            lent = len(tc(bin(int(int(Dict2_regval[reg1], 2) % int(Dict2_regval[reg2], 2)))))
            if lent > 16:
                Dict2_regval["FLAGS"] = "0000000000010000"
        elif Dict_opcode[opcode] == "not":
            Dict2_regval[reg2] = tc(bin((~int(Dict2_regval[reg1]))& (2**16-1)))
            lent = len(tc(bin(int(int(Dict2_regval[reg1], 2) % int(Dict2_regval[reg2], 2)))))
            if lent > 16:
                Dict2_regval["FLAGS"] = "0000000000010000"
        elif Dict_opcode[opcode] == "cmp":
            if Dict2_regval[reg1] == Dict2_regval[reg2]:
                Dict2_regval["FLAGS"] = "0000000000000001"
                Flags = '0000000000000001'
            elif Dict2_regval[reg1] > Dict2_regval[reg2]:
                Dict2_regval["FLAGS"] = "0000000000000010"
                Flags = '0000000000000010'
            elif Dict2_regval[reg1] < Dict2_regval[reg2]:
                Dict2_regval["FLAGS"] = "0000000000000100"
                Flags = '0000000000000100'
        st = st + db(pc) + ' ' + Dict2_regval['R0'] + ' ' + Dict2_regval['R1'] + ' ' + Dict2_regval['R2'] + ' ' + \
             Dict2_regval['R3'] + ' ' + Dict2_regval['R4'] + ' ' + Dict2_regval['R5'] + ' ' + Dict2_regval['R6'] + ' ' + \
             Dict2_regval['FLAGS']
        Dict2_regval['FLAGS'] = '0000000000000000'
        str.append(st)
        pc = pc + 1
    elif type == 'D':
        reg1 = Dict_reg[inst[5:8]]
        mem_address = inst[8:]
        if Dict_opcode[opcode] == 'ld':
            if mem_address not in Dict_mem_Add:
                Dict_mem_Add[mem_address] = '0000000000000000'
            else:
                Dict2_regval[reg1] = Dict_mem_Add[mem_address]
        elif Dict_opcode[opcode] == 'st':
            Dict_mem_Add[mem_address] = tc(bin(int(Dict2_regval[reg1], 2)))
        st = st + db(pc) + ' ' + Dict2_regval['R0'] + ' ' + Dict2_regval['R1'] + ' ' + Dict2_regval['R2'] + ' ' + \
             Dict2_regval['R3'] + ' ' + Dict2_regval['R4'] + ' ' + Dict2_regval['R5'] + ' ' + Dict2_regval['R6'] + ' ' + \
             Dict2_regval['FLAGS']
        str.append(st)
        pc = pc + 1
    elif type == 'E':
        c = inst[8:16]
        if Dict_opcode[opcode] == 'jmp':
            st = st + db(pc) + ' ' + Dict2_regval['R0'] + ' ' + Dict2_regval['R1'] + ' ' + Dict2_regval['R2'] + ' ' + \
                 Dict2_regval['R3'] + ' ' + Dict2_regval['R4'] + ' ' + Dict2_regval['R5'] + ' ' + Dict2_regval[
                     'R6'] + ' ' + \
                 Dict2_regval['FLAGS']
            str.append(st)
            Dict2_regval['FLAGS'] = '0000000000000000'
            pc = int(c, 2)
        elif Dict_opcode[opcode] == 'jgt':
            if Flags == '0000000000000010':
                st = st + db(pc) + ' ' + Dict2_regval['R0'] + ' ' + Dict2_regval['R1'] + ' ' + Dict2_regval[
                    'R2'] + ' ' + \
                     Dict2_regval['R3'] + ' ' + Dict2_regval['R4'] + ' ' + Dict2_regval['R5'] + ' ' + Dict2_regval[
                         'R6'] + ' ' + \
                     Dict2_regval['FLAGS']
                str.append(st)
                Dict2_regval['FLAGS'] = '0000000000000000'
                pc = int(c, 2)
            else:
                st = st + db(pc) + ' ' + Dict2_regval['R0'] + ' ' + Dict2_regval['R1'] + ' ' + Dict2_regval[
                    'R2'] + ' ' + \
                     Dict2_regval['R3'] + ' ' + Dict2_regval['R4'] + ' ' + Dict2_regval['R5'] + ' ' + Dict2_regval[
                         'R6'] + ' ' + \
                     Dict2_regval['FLAGS']
                str.append(st)
                Dict2_regval['FLAGS'] = '0000000000000000'
                pc = pc + 1
        elif Dict_opcode[opcode] == 'jlt':
            if Flags == '00000000000000100':
                st = st + db(pc) + ' ' + Dict2_regval['R0'] + ' ' + Dict2_regval['R1'] + ' ' + Dict2_regval[
                    'R2'] + ' ' + \
                     Dict2_regval['R3'] + ' ' + Dict2_regval['R4'] + ' ' + Dict2_regval['R5'] + ' ' + Dict2_regval[
                         'R6'] + ' ' + \
                     Dict2_regval['FLAGS']
                str.append(st)
                Dict2_regval['FLAGS'] = '0000000000000000'
                pc = int(c, 2)
            else:
                st = st + db(pc) + ' ' + Dict2_regval['R0'] + ' ' + Dict2_regval['R1'] + ' ' + Dict2_regval[
                    'R2'] + ' ' + \
                     Dict2_regval['R3'] + ' ' + Dict2_regval['R4'] + ' ' + Dict2_regval['R5'] + ' ' + Dict2_regval[
                         'R6'] + ' ' + \
                     Dict2_regval['FLAGS']
                str.append(st)
                Dict2_regval['FLAGS'] = '0000000000000000'
                pc = pc + 1
        else:
            if Flags == '00000000000000001':
                pc = int(c, 2)
                st = st + db(pc) + ' ' + Dict2_regval['R0'] + ' ' + Dict2_regval['R1'] + ' ' + Dict2_regval[
                    'R2'] + ' ' + \
                     Dict2_regval['R3'] + ' ' + Dict2_regval['R4'] + ' ' + Dict2_regval['R5'] + ' ' + Dict2_regval[
                         'R6'] + ' ' + \
                     Dict2_regval['FLAGS']
                str.append(st)
                Dict2_regval['FLAGS'] = '0000000000000000'
            else:
                st = st + db(pc) + ' ' + Dict2_regval['R0'] + ' ' + Dict2_regval['R1'] + ' ' + Dict2_regval[
                    'R2'] + ' ' + \
                     Dict2_regval['R3'] + ' ' + Dict2_regval['R4'] + ' ' + Dict2_regval['R5'] + ' ' + Dict2_regval[
                         'R6'] + ' ' + \
                     Dict2_regval['FLAGS']
                str.append(st)
                Dict2_regval['FLAGS'] = '0000000000000000'
                pc = pc + 1
for i in range(len(str)):
    sys.stdout.write(str[i])
    sys.stdout.write("\n")
for k in Dict:
    sys.stdout.write(Dict[k])
    sys.stdout.write("\n")
    count = count + 1
Dict_fin = {}
for p in Dict_mem_Add:
    c = int(p, 2)
    if c not in Dict_fin:
        Dict_fin[c] = Dict_mem_Add[p]
D = sorted(Dict_fin.keys())
for j in D:
    sys.stdout.write(Dict_fin[j])
    sys.stdout.write("\n")
    count = count + 1
while count != 256:
    sys.stdout.write('0000000000000000')
    sys.stdout.write("\n")
    count = count + 1