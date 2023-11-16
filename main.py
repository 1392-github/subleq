import sys

DEBUG = False

prg = [int(x) for x in input().split()]
ram = [0]*100
def read(addr):
    if addr >= 0:
        return ram[addr]
    elif addr == -1:
        return 0
    elif addr == -2:
        return sys.stdin.read(1)
    elif addr == -3:
        return 0
    else:
        raise IndexError('Wrong Gate Address')
def write(addr,value):
    if addr >= 0:
        ram[addr] = value
    elif addr == -1:
        print(chr(value), end='')
    elif addr == -2:
        pass
    elif addr == -3:
        sys.exit(value)
    else:
        raise IndexError('Wrong Gate Address')
for a,b in enumerate(prg):
    ram[a] = b
pc = 0
while True:
    if DEBUG:
        print('PC : {0}, RAM : {1}'.format(pc, ram))
    v = read(read(pc+1))-read(read(pc))
    write(read(pc+1),v)
    if v==0:
        pc = read(pc+2)
    else:
        pc += 3
