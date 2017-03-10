from Crypto.Cipher import DES
import sys, struct, os
from Crypto import Random

klucz = sys.argv[1]
plik = sys.argv[2]
out = sys.argv[3]

iv = Random.get_random_bytes(8)
encryptor = DES.new(klucz, DES.MODE_ECB, iv)
filesize = os.path.getsize(plik)
chunksize = 16

with open(plik, 'rb') as inFi:
	with open(out, 'wb') as outFi:
		outFi.write(struct.pack('<Q', filesize))
		outFi.write(iv)

		while True:
			chunk = inFi.read(chunksize)
			if len(chunk) == 0:
				break
			elif len(chunk) % 16 != 0:
				chunk += ' ' * (16 - len(chunk) % 16)

			outFi.write(encryptor.encrypt(chunk))
	

