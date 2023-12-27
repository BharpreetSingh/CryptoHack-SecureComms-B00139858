#I first thought there was something within the encryption and decryption functions
#.But I didnt see a Ciphertext ,But looking more carefully I did more research about what 
#@chal.route('/block_cipher_starter/decrypt/<ciphertext>/') meant and i was introduced to requests  

import requests


response = requests.get("http://aes.cryptohack.org/block_cipher_starter/encrypt_flag/")
print(response.json())
ciphertext = response.json()['ciphertext']

#Then i put the ciphertext 188bc9522883a992cd99f9b2b8ec84fb150c1abe17e7a8ed04a768ad1d11fc07
#In the website i put this ciphertext and made it into plaintext and got the following 

plaintext = "63727970746f7b626c30636b5f633170683372355f3472335f663435375f217d"

#To see the flag you need to convert the plaintext into ASCII
print(bytearray.fromhex(plaintext).decode())