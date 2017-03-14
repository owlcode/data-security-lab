import sys, math, binascii
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
                print "x"
                return text
        padding = blocksize - len(text) % blocksize
        padChar = b'\x80'
        return text + padding * padChar

def unpad(text):
        return text.rstrip(b'\x80')

def readFile(inputFile):
        text = ""
        with open(inputFile, "r") as f:
                text = f.read()
        return text

def writeFile(text, outputFile):
        with open(outputFile, "w") as f:
                f.write(text)

if (len(sys.argv) != 2 and len(sys.argv) != 5):
        print "Podaj 4 argumenty: tryb szyfrowania ('-e' lub '-c') klucz, inputFile, outputFile"
elif (len(sys.argv) == 5):
        mode = sys.argv[1]
        key = sys.argv[2]
        inFile = sys.argv[3]
        outFile = sys.argv[4]
        text = readFile(inFile)

        text = pad(text, 16)

        key = bytes(key)
        if (len(key) != 16 and len(key) != 32 and len(key) != 64):
                print "Podaj klucz o dlugosci 16, 32 lub 64 bity"
        else:
                iv = get_random_bytes(16)
                if (mode == "-e"):
                        aes = AES.new(key, AES.MODE_ECB, iv)
                        encryptedAES = aes.encrypt(text)
                        writeFile(encryptedAES, outFile + "AESECB")
                if (mode == "-c"):
                        aes = AES.new(key, AES.MODE_CBC, iv)
                        encryptedAES = aes.encrypt(text)
                        writeFile(encryptedAES, outFile + "AESCBC")
                if (mode == "-ie" or mode == "-ic"):
                        dibheader = ""
                        bmpheader = ""
                        fIn = open(inFile, 'rb')
                        bmpheader = fIn.read(14)
                        dibheader = fIn.read(50)
                        DIBheaderarray = []
                        for i in range(0,80,2):
                                DIBheaderarray.append(int(binascii.hexlify(dibheader)[i:i+2],16))
                        width = sum([DIBheaderarray[i+4]*256**i for i in range(0,4)])
                        height = sum([DIBheaderarray[i+8]*256**i for i in range(0,4)])

                        row_padded = width * height * 3
                        img = fIn.read(row_padded)
                        cleartext = pad(binascii.unhexlify(binascii.hexlify(img)), 16)
                        if (mode == "-ic"):
                                aes = AES.new(key, AES.MODE_CBC, iv)
                        if (mode == "-ie"):
                                aes = AES.new(key, AES.MODE_ECB, iv)
                        encryptedAES = aes.encrypt(cleartext)
                        output = ""
                        output+=bmpheader
                        output+=dibheader
                        output+=encryptedAES
                        writeFile(output, outFile)
                print "Entropia tekstu naturalnego: {0}".format(entropy(text))
                print "Entropia kryptogramu: {0}".format(entropy(encryptedAES))
elif (len(sys.argv) == 2 and sys.argv[1] == "-e"):
        entropiaAES = 256 * math.log(2,2)

        for i in range(0,256):
                entropia = i * math.log(52,2)
                if (entropia > entropiaAES):
                        print 'Dla dlugosci {0} entropia wynosi {1} (alfabet 52 znakow)'.format(i, entropia)
                        print 'Jest wieksza od entropii klucza AES ktora wynosi {0}'.format(entropiaAES)
                        break
