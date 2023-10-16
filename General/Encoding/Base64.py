import base64

#hex String
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

#decode Hex to bytes
decoded_bytes = bytes.fromhex(hex_string)

#Encode bytes into Base64
encoded_base64 = base64.b64encode(decoded_bytes)

#Convert base64 into a String 
flag = encoded_base64.decode('utf-8')

print(flag)