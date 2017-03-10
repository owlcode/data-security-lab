import sys
from Crypto.PublicKey import RSA
from Crypto import Random

filename = sys.argv[1]

rsa = RSA.generate(1024, Random.new().read)
pub = rsa.publickey()
#priv = rsa.privatekey()

with open(filename) as f:
	data = f.read();
	encrypted = pub.encrypt(data, 32)



print encrypted

print '\n\n Odszyfrowane:'
print rsa.decrypt(encrypted)

print pub.exportKey()
print rsa.exportKey()
