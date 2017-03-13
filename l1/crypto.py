import sys, re, string, fileinput

modelFrequencyPolish = [9.56, 1.44, 4.38, 3.06, 8.95, 0.31, 1.26, 0.98, 8.20, 2.48, 3.36, 3.64, 2.72, 5.73, 8.32, 3.03, 0, 4.43, 4.79, 3.96, 2.19, 0.02, 4.51, 0.05, 4.96, 6.25]
modelFrequencyEnglish = [8.17, 1.49, 2.78, 4.253, 12.7, 2.23, 2.01, 6.09, 6.97, 0.15, 0.772, 4.02, 2.406, 6.749, 7.51, 1.93, 0.09, 5.98, 6.33, 9.06, 2.76, 0.97, 2.36, 0.15, 1.97, 0.07]
modelFrequencyFrench = [7.36, 0.9, 3.2, 3.6, 14.7, 1.06, 0.86, 0.737, 7.52, 0.61, 0.05, 5.45, 2.96, 7.09, 5.79, 2.52, 1.36, 6.69, 7.95, 7.24, 6.31, 1.84, 0.07, 0.43, 0.13, 0.326, 0.486, 0.051]
languages = [ "polish", "english", "french" ]

def nwd(a, b):
        while b != 0:
                pom = b
                b = a%b
                a = pom
        return a

def rot(shift, numberOfRots, inputString):
	alfa = "abcdefghijklmnopqrstuvwxyz"
	key, outputString = "", ""
	i = 0
	for char in alfa:
                if ord(alfa[i]) + shift > ord('z'):
                        char = chr(ord('a') + (shift - (ord('z') - ord(alfa[i]))) - 1)
                else:
                        char = chr(ord(alfa[i]) + shift)
                key += char
                i += 1
	table = string.maketrans(alfa, key)
	for line in inputString:
                temp = numberOfRots
                while temp > 0:
	                line = string.translate(line, table)
                        temp-=1
                outputString += line
	return outputString

def stats(inputString):
        stat = [0.0] * 26
        wordcount = 0
	inputString = inputString.lower()
	znak = ""
        for i in range(0, len(inputString)):
        	if(inputString[i].isalpha()):
                	wordcount+=1
                        stat[ord(inputString[i])-ord('a')] += 1
        for i in range(0,25):
                stat[i] = stat[i]/wordcount * 100
        return stat

def compareAnalysisToModel(analysisResult, modelFrequency):
	summ = 0.0
	for i in range(0, 25):
		summ += abs(analysisResult[i] - modelFrequency[i])
	return summ

def readFile(filePath):
	with open(filePath, 'r') as f:
		text = f.read()
	return text

def writeFile(filePath, text):
	with open(filePath, 'w+') as f:
		f.write(text)
	f.close()

mode = ""
inputFile = ""
inputFile1, inputFile2, inputFile3 = "", "", ""
inputString = ""
inputString1, inputString2, inputString3 = "", "", ""
encryptedText = ""
shift = 0
summ = 0
analysisResult = []
if (len(sys.argv) < 3):
	print "Sposob uzycia: "
elif (len(sys.argv) >= 3):
	mode = sys.argv[1]
if (mode == "-x"):
	shift = int(sys.argv[2])
	inputFile = sys.argv[3]
	outputFile = "encryptedText/output.txt"
	inputString = readFile(inputFile)
	encryptedText = rot(shift, 1, inputString)
	writeFile(outputFile, encryptedText)
	print "Tekst {0} zaszyfrowano ROT{1} i zapisano do pliku {2}".format(inputFile, shift, outputFile)
if (mode == "-a"):
	shift = int(sys.argv[2])
	print "Tekst zaszyfrowany ROT{0} nalezy przerotowac {1} razy z przesunieciem {2} aby otrzymac tekst zrodlowy".format(shift, 26/nwd(shift, 26), shift)
elif (mode == "-b"):
	lang = int(sys.argv[2])
	inputFile = sys.argv[3]
        outputFile = "decryptedText/output.txt"
        inputString = readFile(inputFile)
	analysisResult = stats(inputString)

	tempText = ""
	tempStat = []
	sumArray = [0.0] * 26
	for i in range (0,26):
		tempText = rot(i, 1, inputString)
		tempStat = stats(tempText)
		if (lang == 1):
			sumArray[i] = compareAnalysisToModel(tempStat, modelFrequencyPolish)
		if (lang == 2):
			sumArray[i] = compareAnalysisToModel(tempStat, modelFrequencyEnglish)
		if (lang == 3):
			sumArray[i] = compareAnalysisToModel(tempStat, modelFrequencyFrench)
	shift = 26-sumArray.index(min(sumArray))
	decryptedText = rot(shift, 26/nwd(shift, 26)-1, inputString)
	writeFile(outputFile, decryptedText)
	print "Tekst {0} odszyfrowano kluczem ROT{1} i zapisano do pliku {2}".format(inputFile, shift, outputFile)
elif (mode == "-c"):
	inputFile1 = sys.argv[2]
	inputFile2 = sys.argv[3]
	inputFile3 = sys.argv[4]
	stats1, stats2, stats3 = [], [], []
	inputString1 = readFile(inputFile1)
	inputString2 = readFile(inputFile2)
	inputString3 = readFile(inputFile3)
	stats1 = stats(inputString1)
	stats2 = stats(inputString2)
	stats3 = stats(inputString3)

	print "Analiza plikow {0}, {1}, {2}:\n".format(inputFile1, inputFile2, inputFile3)
	print "{0}:".format(inputFile1)
	for i in range (0,26):
		print "{0}: {1}%".format(chr(i+ord('a')), stats1[i])
	print "\n{0}:".format(inputFile2)
        for i in range (0,26):
                print "{0}: {1}%".format(chr(i+ord('a')), stats2[i])
	print "\n{0}:".format(inputFile3)
        for i in range (0,26):
                print "{0}: {1}%".format(chr(i+ord('a')), stats3[i])
