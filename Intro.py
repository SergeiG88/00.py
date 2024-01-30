# print(ord('H'))
# print(chr(104))

# for ch in 'hello':
#     print(ord(ch))

'''можно её обратно из кода собрать'''
# codes = [104, 101, 108, 108, 111]
#
# out = ''
# for code in codes:
#     out += chr(code)
# print(out)

# for code in range(128):
#     print(code, hex(code), chr(code))

# bb = b'\xd1\x84'
# print(bb)

# bb = b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
# print(bb)
# print(type(bb))
# ''' по сути это неизменяемые последовательности целых чисел,'''
# '''поддерживают те же операции что и str'''
# print(hex(bb[0]))
# print(bb.count(0xd0))
# print(b'he' + b'llo')

# bb = b'\xd1\x84'
# print(bin(0xd1))
# print(bin(0x84))

# code = 0b10000100100
# print(code, hex(code))
# print(chr(code))

print(hex(ord('h')))