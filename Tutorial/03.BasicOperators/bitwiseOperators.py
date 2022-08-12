# a = 00111100
# b = 00001101

# a&b = 00001100    Copies a bit to the result, if it exists in both operands
# a|b = 00111101    Copies a bit, if it exists in either operand
# a^b = 00110001    XOR- If it is set in one operand but not both
# ~a = 11000011     Flippng bits
# a<< = 11110000    Binary left shift - The left operands value is moved left by the number of bits specified by the right operand
# a>> = 00001111    Binary Right shift - The left operands value is moved right by the number of bits specified by the right operand

a = 60          # a = 00111100
b = 13          # b = 00001101

print('a =',a,':',bin(a),',','b =',b,':',bin(b))

c = 0

c = a & b      # 12 = 00001100
print('Result of AND is',c,':',bin(c))

c = a | b       # 61 = 00111101
print('The result of OR is',c,':',bin(c))

c = a ^ b       # 49 = 00110001
print('The result of EXOR is',c,':',bin(c))

c = ~ a         # -61 = 11000011
print('The result of COMPLEMENT is',c,':',bin(c))

c = a << 2      # 240 = 11110000
print('The result of LEFT SHIFT is',c,':',bin(c))

c = a >> 2      # 15 = 0000111
print('The result of RIGHT SHIFT is',c,':',bin(c))