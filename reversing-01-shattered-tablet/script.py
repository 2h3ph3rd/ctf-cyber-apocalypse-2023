#!/usr/bin/env python3

s1 = [''] * 8
s2 = [''] * 8
s3 = [''] * 8
s4 = [''] * 8
s5 = [''] * 8
s6 = [''] * 8
s7 = [''] * 8

s4[7] = 'p'
s1[1] = 'T'
s1[7] = 'k'

s5[4] = 'd'
s2[3] = '4'

s3[4] = 'e'
s2[2] = '_'
s1[0] = 'H'
s5[2] = 'r'

s5[3] = '3'
s4[1] = '_'
s1[2] = 'B'

s4[5] = 'r'
s1[3] = '{'

s4[2] = 'b'
s1[5] = 'r'
s2[5] = '4'

s4[6] = '3'
s3[3] = 'v'
s2[4] = 'p'
s5[1] = '1'

s4[3] = '3'
s3[1] = 'n'

s1[4] = 'b'
s5[0] = '4'
s2[1] = 'n'
s3[0] = ','

s2[0] = '3'
s1[6] = '0'
s3[7] = 't'

s2[7] = 't'
s4[0] = '0'

s2[6] = 'r'
s5[5] = '}'
s3[5] = 'r'
s3[6] = '_'

s3[2] = '3'
s4[4] = '_'

s1 = "".join(s1)
s2 = "".join(s2)
s3 = "".join(s3)
s4 = "".join(s4)
s5 = "".join(s5)
s6 = "".join(s6)
s7 = "".join(s7)

flag = "".join([s1, s2, s3, s4, s5, s6, s7])

print(flag)
