#Using the a^p-1 ≡ 1(mod p)#
#Since a and p ae coprimes multiple both sides by a^-1#
#a^p-1 . a^-1 ≡ 1 . a^-1 (mod p)#
#simplifies to a^p-2 ≡ a^-1 (mod p )#
#Therefore 3^13-2 ≡ 3^-1 (mod 13)

D = pow(3, 11, 13)
print(D)