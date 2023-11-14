from pwn import xor
#ciphertext
flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

#We know that the begging of the flag starts with crypto{' as all the other do aswell
#so we are xoring both together with crypto{' encoded as bytes 
result1 = xor(flag, 'crypto{'.encode())
print(result1)

#Our result1 showed us that the rest of flag is myXORkey
##so we are xoring both together with 'myXORkey' encoded as bytes
result2 = xor(flag, 'myXORkey'.encode())
print(result2)