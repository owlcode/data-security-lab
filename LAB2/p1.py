import sys
from Crypto.Cipher import ARC4

key = sys.argv[1]
text = sys.argv[2]

cipher = ARC4.new(key)
encrypted = cipher.encrypt(text)

print "\n Zakodowane przez pythona: "
print " ".join(hex(ord(n)) for n in encrypted)
print '\n'

key = list(key)
keyLen = len(key)
text = list(text)
s = {}
stream = []
j = 0

for i in range(256):
	s[i] = i

for i in range(256):
	# tu jest chyba zle ord() zamienia na wysokie liczby
	# a nie wiem czy powinien
	j = (j + s[i] + ord(key[i % keyLen])) % 256
	pomoc = s[i]
	s[i] = s[j]
	s[j] = pomoc


i = 0
j = 0
print 'Strumien klucza:'
for i in range(len(text)):
	i = (i + 1) % 256
	j = (j + s[i]) % 256
	
	pomoc = s[i]
	s[i] = s[j]
	s[j] = pomoc
	
	k = s[(s[i] + s[j]) % 256]	
	
	stream.append(k)	
	sys.stdout.write(hex(k))
	sys.stdout.write(" ")

print "\n\n Zakodowane przeze mnie "

for i in range(len(text)):
	sys.stdout.write(hex(ord(text[i]) ^ stream[i]))
	sys.stdout.write(" ")
print " "
