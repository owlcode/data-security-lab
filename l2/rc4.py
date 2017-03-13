import sys, string, math, time
from Crypto.Cipher import ARC4

def initRegister(key):
	S = [0] * 256
	for i in range(0,256):
		S[i] = i
	j = 0
	for i in range(0,255):
		j = (j + S[i] + ord(key[i % len(key)])) % 256
		temp = S[i]
		S[i] = S[j]
		S[j] = temp
	return S

def genStream(S):
	i, j = 0, 0
	while True:
		i = (i + 1) % 256
        	j = (j + S[i]) % 256
        	temp = S[i]
                S[i] = S[j]
                S[j] = temp
        	yield S[(S[i] + S[j]) % 256]

def encrypt(key, sourceText):
	cipher = []
	S = initRegister(key)
	cipherStream = genStream(S)
	for char in sourceText:
		cipherChar = chr(ord(char) ^ cipherStream.next())
		cipher.append(cipherChar)
	return ''.join(cipher)

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

def readFile(inputFile):
	text = ""
	with open(inputFile, "r") as f:
		text = f.read()
	return text

def writeFile(text, outputFile):
	with open(outputFile, "w") as f:
		f.write(text)

def generateKeys(length, inputString):
	keyPool = {}
	from itertools import product
        for combo in product("ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnoprstuvwxyz1234567890", repeat=length):
                keyPool[''.join(combo)] = 0
	for k in keyPool:
		temp = encrypt(k, inputString)
		keyPool[k] = entropy(temp)
	return min(keyPool, key=keyPool.get)

print "Podaj klucz do szyfrowania lub dlugosc klucza ktorym zaszyfrowano tekst."
key = sys.stdin.read()
if (len(sys.argv) == 2):
	inputFile = sys.argv[1]
	print "\nWybrano czytanie z pliku {0}.".format(inputFile)
	inputString = readFile(inputFile)
	result = encrypt(key, inputString)
	print result
elif (len(sys.argv) == 3):
	inputFile = sys.argv[1]
	outputFile = sys.argv[2]
	print "\nWybrano czytanie z pliku {0} i pisanie do pliku {1}".format(inputFile, outputFile)
	inputString = readFile(inputFile)
	result = encrypt(key, inputString)
	writeFile(result, outputFile)
	print "Szyfrowanie zakonczone pomyslnie."
elif (len(sys.argv) == 1):
	while True:
		print "\nPodaj tekst do zaszyfrowania"
		inputString = sys.stdin.read()
		if (inputString == "!quit"):
			break
		result = encrypt(key, inputString)
		outputString = ""
		cipher = ARC4.new(key)
		encrypted = cipher.encrypt(inputString)
		print result
		print "Zgodnosc z ARC4: {0}".format(result == encrypted)
elif (len(sys.argv) == 4 and sys.argv[1] == "-c"):
	inputFile1 = sys.argv[2]
	inputFile2 = sys.argv[3]
	inputString1 = readFile(inputFile1)
	inputString2 = readFile(inputFile2)
	print "Entropia tekstu {0}: {1}. Entropia tekstu {2}: {3}".format(inputFile1, entropy(inputString1), inputFile2, entropy(inputString2))
elif (len(sys.argv) == 4 and sys.argv[1] == "-d"):
	inputFile = sys.argv[2]
        outputFile = sys.argv[3]
        print "\nWybrano deszyfrowanie tekstu z pliku {0} kluczem o dlugosci {1} i pisanie wyniku do pliku {2}".format(inputFile,len(key), outputFile)
	inputString = readFile(inputFile)
	start = time.time()
	decryptedKey = generateKeys(int(key), inputString)
	decryptedText = encrypt(decryptedKey, inputString)
	writeFile(decryptedText, outputFile)
	end = time.time()
	print 'Tekst byl zaszyfrowany kluczem "{0}". Czas deszyfrowania: {1}s'.format(decryptedKey, end-start)
