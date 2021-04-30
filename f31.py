import struct


def f31(x):
    list_a = {'1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': ''}
    num = 30011
    print(hex(num))
    new_x = struct.unpack('%dB' % len(x), x)
    amount = 0
    count = 0
    for i in range(7, 9):
        print(hex(new_x[i]))
        if amount == 0:
            amount += new_x[i]
            count += 1
        else:
            amount += new_x[i] << (8*count)
            count += 1
        print(hex(amount) + "\n")
    return list_a


print(f31((b'YNFW\xb0;uI\xcc\xfc\xbc\xeb\xbcN\x00\xf9\xe0+?\x93\xb6\xbf\x03\x00')))
