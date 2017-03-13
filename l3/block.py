import sys, math
from Crypto.Cipher import DES,AES
from Crypto.Random import get_random_bytes

def entropy(inputString):
        entropy = {}
        for char in inputString:
                if char in entropy:
                        entropy[char] += 1.0
                else:
                        entropy[char] = 1.0
        result = 0.0
        for char in entropy:
                frequency = entropy[char]/len(inputString)
                result -= frequency * math.log(frequency, 2)
        return result

def entropyH(string, n):
	l = len(string)
	for i in range(l):
		entropy = l * math.log(n, 2)
	return entropy

def pad(text, blocksize):
	if (len(text) % blocksize == 0):
		return text
	padding = blocksize - len(text) % blocksize
	padChar = b'\x00'
	return text + padding * padChar

def unpad(text):
	return text.rstrip(b'\x00')

def readFile(inputFile):
        text = ""
        with open(inputFile, "r") as f:
                text = f.read()
        return text

def writeFile(text, outputFile):
        with open(outputFile, "w") as f:
                f.write(text)

if (len(sys.argv) == 4):
	key = sys.argv[1]
	inFile = sys.argv[2]
	outFile = sys.argv[3]
	text = readFile(inFile)
	
	text = pad(text, 16)

	key = bytes(key)
	iv1 = get_random_bytes(8)
	iv2 = get_random_bytes(16)

	des = DES.new(key, DES.MODE_CBC, iv1)
	encryptedDES = des.encrypt(text)
	writeFile(encryptedDES, outFile + "DES")

	aes = AES.new(key+key, AES.MODE_ECB, iv2)
	encryptedAES0 = aes.encrypt(text)
	writeFile(encryptedAES0, outFile + "AESECB")

	aes = AES.AESCipher(key+key, AES.MODE_CBC, iv2)
	encryptedAES = aes.encrypt(text)
	writeFile(encryptedAES, outFile + "AESCBC")

	print "Entropia tekstu naturalnego: {0}".format(entropy(text))
	print "Entropia kryptogramu: DES: {0}, AESCBC: {1}, AESECB: {2}".format(entropy(encryptedDES), entropy(encryptedAES), entropy(encryptedAES0))
else:
	entropiaAES = 256 * math.log(2,2)

	for i in range(0,256):
		entropia = i * math.log(26,2)
		if(entropia > entropiaAES):
			print 'Dla dlugosci {0} entropia wynosi {1} (alfabet 26 znakow)'.format(i, entropia)
			print 'Jest wieksza od entropii klucza AES ktora wynosi {0}'.format(entropiaAES)
			break
