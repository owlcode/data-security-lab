import sys, fileinput, string, random, crypt, hashlib

def changePwd(inString, username, newPassword):
	for line in inString.split('\n'):
		temp = line.split(':')
		if (temp[0] == username):
			if (verifyPassword(temp[1]) == True):
				temp[1] = newPassword
				newline = temp[0] + ":" + temp[1]
				outString = string.replace(inString, line, newline)
				return outString
	print "Bledny login lub haslo"

def checksum(inString):
	for line in inString.split('\n'):
		if (len(line) > 0):
			temp = line.split("  ")
			fileName = temp[1]
			checksum = temp[0]
			sumString = readFile(fileName)
			if (hashlib.md5(sumString).hexdigest() == checksum):
				flag = "OK"
			else:
				flag = "FAILED"
			print "{0}: {1}".format(fileName, flag)

def verifyPassword(pwd):
	salt = pwd[:2]
	print "podaj haslo:"
	p = sys.stdin.readline().strip()
	encrypted = crypt.crypt(p, salt)
	return pwd == encrypted

def readFile(inFile):
	with open(inFile, 'r') as f:
		outString = f.read()
	return outString

def writeFile(outFile, outString):
	with open(outFile, 'w') as f:
		f.write(outString)

if (len(sys.argv) == 4):
	f = sys.argv[1]
	inString = readFile(f)
	username = sys.argv[2]
	newPassword = sys.argv[3]

	salt = ''.join(random.sample(string.ascii_letters, 2))
	protectedPassword = crypt.crypt(newPassword, salt)
	
	result = changePwd(inString, username, protectedPassword)
	if (result != None):
		writeFile(f, result)
		print "Haslo zmienione"
if (len(sys.argv) == 3):
	if (sys.argv[1] == "-c"):
		f = sys.argv[2]
		checksum(readFile(f))
