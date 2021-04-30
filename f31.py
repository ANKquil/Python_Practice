import pprint
import struct

E_SIZE = 8 + 8 + 4 + 8
D_SIZE = 2 + 4 + E_SIZE + 3 * 2
C_SIZE = 1 + 8
B_SIZE = 2 + 4 * 4 + 2 + 2 + D_SIZE + 4
A_SIZE = 2 + 2 + 4 + 2 + 4 + 3 + 2 + 2


def parse_e(offset, byte_string):
    e_bytes = byte_string[offset:offset + E_SIZE - 8]
    e_parsed = struct.unpack('dQHH', e_bytes)
    e3_parsed = list(struct.unpack('<' + str(e_parsed[2]) + 'q',
                                   byte_string[e_parsed[3]:(e_parsed[3] +
                                                            struct.calcsize('<' + str(e_parsed[2]) + 'q'))]))
    e4_bytes = byte_string[offset + E_SIZE - 8:offset + E_SIZE]
    e4_parsed = struct.unpack('Q', e4_bytes)
    return {
        'E1': e_parsed[0],
        'E2': e_parsed[1],
        'E3': list(e3_parsed),
        'E4': e4_parsed[0],
    }


def parse_d(offset, byte_string):
    d12_bytes = byte_string[offset:offset + 6]
    d12_parsed = struct.unpack('<IH', d12_bytes)
    d3_parsed = parse_e(offset + 6, byte_string)
    d4_bytes = byte_string[offset + 6 + E_SIZE:offset + 6 + E_SIZE + 6]
    d4_parsed = struct.unpack('<3h', d4_bytes)
    return {
        'D1': d12_parsed[0],
        'D2': d12_parsed[1],
        'D3': d3_parsed,
        'D4': list(d4_parsed)
    }


def parse_c(offset, byte_string):
    c_bytes = byte_string[offset:offset + C_SIZE]
    c_parsed = struct.unpack('<bQ', c_bytes)
    return {
        'C1': c_parsed[0],
        'C2': c_parsed[1]
    }


def parse_b(offset, byte_string):
    b1_bytes = byte_string[offset:offset + 2]
    b1_parsed = struct.unpack('<h', b1_bytes)
    b2_bytes = byte_string[offset + 2:offset + 2 + 16]
    b2_parsed = struct.unpack('<4I', b2_bytes)
    b34_bytes = byte_string[offset + 2 + 16:offset + 2 + 16 + 4]
    b34_parsed = struct.unpack('<hH', b34_bytes)
    b5_parsed = parse_d(offset + 2 + 16 + 4, byte_string)
    b6_bytes = byte_string[offset + 2 + 16 + 4 + D_SIZE:offset + D_SIZE + 2 + 16 + 4 + 4]
    b6_parsed = struct.unpack('i', b6_bytes)
    return {
        'B1': b1_parsed[0],
        'B2': [parse_c(b2_parsed[0], byte_string),
               parse_c(b2_parsed[1], byte_string),
               parse_c(b2_parsed[2], byte_string),
               parse_c(b2_parsed[3], byte_string)],
        'B3': b34_parsed[0],
        'B4': b34_parsed[1],
        'B5': b5_parsed,
        'B6': b6_parsed[0],
    }


def parse_a(offset, byte_string):
    a_bytes = byte_string[offset:offset + A_SIZE]
    a_parsed = struct.unpack('<hHiHf3bHH', a_bytes)
    a7_parsed = list(struct.unpack('<' + str(a_parsed[8]) + 'i',
                                   byte_string[a_parsed[9]:(a_parsed[9] +
                                                            struct.calcsize('<' + str(a_parsed[8]) + 'i'))]))
    return {
        'A1': a_parsed[0],
        'A2': a_parsed[1],
        'A3': a_parsed[2],
        'A4': parse_b(a_parsed[3], byte_string),
        'A5': a_parsed[4],
        'A6': [a_parsed[5], a_parsed[6], a_parsed[7]],
        'A7': a7_parsed
    }


def f31(byte_string):
    return parse_a(5, byte_string)
