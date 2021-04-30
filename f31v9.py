import pprint
import struct

D_SIZE = 2 + 1 + 8 + 8
C_SIZE = 2 + 2 + 8 + 2 + 2 + 2 + 4
B_SIZE = 2 + 2 + 8 + 2
A_SIZE = 4 * 1 + 8 + 2 * 2 + 1 + 8 + 1 + 4


def parse_d(offset, byte_string):
    d_bytes = byte_string[offset:offset + D_SIZE]
    d_parsed = struct.unpack('>Hbdd', d_bytes)
    return {
        'D1': d_parsed[0],
        'D2': d_parsed[1],
        'D3': d_parsed[2],
        'D4': d_parsed[3]
    }


def parse_c(offset, byte_string):
    c_bytes = byte_string[offset:offset + C_SIZE]
    c_parsed = struct.unpack('>HHdHHhI', c_bytes)
    c4_parsed = list(struct.unpack('>' + str(c_parsed[3]) + 'b',
                                   byte_string[c_parsed[4]:(c_parsed[4] +
                                                            struct.calcsize('>' + str(c_parsed[3]) + 'b'))]))
    return {
        'C1': c_parsed[0],
        'C2': c_parsed[1],
        'C3': c_parsed[2],
        'C4': c4_parsed,
        'C5': c_parsed[5],
        'C6': c_parsed[6]
    }


def parse_b(offset, byte_string):
    b_bytes = byte_string[offset:offset + B_SIZE]
    b_parsed = struct.unpack('>HHqh', b_bytes)
    b1_parsed = list(struct.unpack('>' + str(b_parsed[0]) + 'd',
                                   byte_string[b_parsed[1]:(b_parsed[1] +
                                                            struct.calcsize('>' + str(b_parsed[0]) + 'd'))]))
    return {
        'B1': b1_parsed,
        'B2': b_parsed[2],
        'B3': b_parsed[3]
    }


def parse_a(offset, byte_string):
    a_bytes = byte_string[offset:offset + A_SIZE - 4]
    a_parsed = struct.unpack('>BBBBQHHBQB', a_bytes)
    a7_parsed = parse_c(offset + A_SIZE - 4, byte_string)
    a8_bytes = byte_string[offset + A_SIZE - 4 + C_SIZE:offset + A_SIZE + C_SIZE]
    a8_parsed = struct.unpack('>I', a8_bytes)
    return {
        'A1': [a_parsed[0], a_parsed[1], a_parsed[2], a_parsed[3]],
        'A2': a_parsed[4],
        'A3': [parse_b(a_parsed[5], byte_string),
               parse_b(a_parsed[6], byte_string)],
        'A4': a_parsed[7],
        'A5': a_parsed[8],
        'A6': a_parsed[9],
        'A7': a7_parsed,
        'A8': parse_d(a8_parsed[0], byte_string)
    }


def f31(byte_string):
    return parse_a(4, byte_string)
