import os
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
import Crypto.Util.number
def encrypt_file(rsa, input, output):
	secret_key = os.urandom(16)
   
	plaintext_length = (Crypto.Util.number.size(rsa.n) - 2) / 8
	padding = '\xff' + os.urandom(16)
	padding += '\0' * (plaintext_length - len(padding) - len(secret_key))
   
	encrypted_secret_key = rsa.encrypt(padding + secret_key, None)
    
	output.write(str(len(encrypted_secret_key)) + '\n')
	output.write(encrypted_secret_key)
    
	iv = '\x00' * 16
	aes_engine = AES.new(secret_key, AES.MODE_CBC, iv)
	output.write(aes_engine.encrypt(input.read()))
