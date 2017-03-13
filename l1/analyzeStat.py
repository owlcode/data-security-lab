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

def rot(n, y, text, output):
        alfa = "abcdefghijklmnopqrstuvwxyz"
        rot = ""
	result = ""
        i = 0
        for char in alfa:
                if ord(alfa[i]) + n > ord('z'):
                        char = chr(ord('a') + (n - (ord('z') - ord(alfa[i]))) - 1)
                else:
                        char = chr(ord(alfa[i]) + n)
                rot += char
                i += 1
        #print "Tekst rotujemy {0} raz(y). Alfabet szyfru ROT{1} : ".format(y,n) + rot + "."
	if (output == "output.txt"):
		table = string.maketrans(alfa, rot)
		#print "Rezultat operacji:\n\n"
                for line in text:
               		line = line.rstrip()
			z = y
                	while z > 0:
                        	line = string.translate(line, table)
                        	z-=1
			result += line
		return result

def stats(text):
	stat = [0.000] * 27
	wordcount = 0
	for line in text:
       		for znak in line:
			if(ord(znak) >= ord('a') and ord(znak) <= 'z'):
                       		wordcount+=1
				stat[ord(znak)-ord('a')] += 1
	for i in range(0,26):
		stat[i] = stat[i]/wordcount * 100
	return stat


if ( (len(sys.argv) < 2) or (len(sys.argv) > 4)):
        print "=================================================================================================================="
        print "Sposob uzycia:\n python analyzeStat.py [-x] Podaj przesuniecie oraz plik tekstu zrodlowego, program zaszyfruje tekst z podanym przesunieciem i poda na wyjscie standardowe [-a] Podaj tekst oraz przesuniecie x w ROTx, program policzy ile rotacji nalezy wykonac aby wrocic do tekstu poczatkowego [-b] Odszyfruj tekst z pliku za pomoca analizy statystycznej [-c] Dokonaj analizy statystycznej plikow\n"
        print "=================================================================================================================="
elif (sys.argv[1] == "-a" ):
	#policz ile razy trzeba przerotowac
	if (len(sys.argv) < 3):
		print "=================================================================================================================="
		print "Podaj przesuniecie szyfru!"
		print "=================================================================================================================="
	a = int(sys.argv[2])
	nww = a/nwd(a, 26) * 26
	rot(a, nww/a, f, "x")
elif (sys.argv[1] == "-x"):
	#zaszyfruj
	if (len(sys.argv) != 4):
		print "=================================================================================================================="
		print "Niepoprawne wywolanie. Podaj przesuniecie i plik wejsciowy"
		print "=================================================================================================================="
	else:
		print rot(int(sys.argv[2]), 1, sys.argv[3], "output.txt")
elif (sys.argv[1] == "-b"):
	#dokonaj analizy, odszyfruj
	text = ""
	if (len(sys.argv) == 3):
		print "=================================================================================================================="
		print "Wybrano jezyk {0}. Aby wybrac inny jezyk, wywolaj program z argumentem [-x] gdzie x to indeks tabeli: {1}. Wybrano czytanie z pliku o nazwie {2}".format(languages[0], languages, sys.argv[2])
		print "=================================================================================================================="
		lang = 0
		with open(sys.argv[2]) as f:
                	for line in f.readlines():
                        	line = re.sub(r'\s', '', line)
                        	line = line.lower()
				text += line
	elif (len(sys.argv) == 4):
		print "=================================================================================================================="
		print "Wybrano jezyk {0}. Wybrano czytanie z pliku o nazwie {1}".format(languages[int(sys.argv[2])], sys.argv[3])
		print "=================================================================================================================="
		lang = int(sys.argv[2])
		with open(sys.argv[3]) as f:
                        for line in f.readlines():
                                line = re.sub(r'\s', '', line)
                                line = line.lower()
                                text += line
	analysisResult = stats(text)
	print analysisResult
	frequencyComparison = [0] * 27
	for i in range(0,26):
		summ = 0
		decypherAttempt = rot(i, 1, text, "output.txt")
		decypherAttemptAnalysisResult = stats(decypherAttempt)
		for j in range(0,26):
			if (lang == 0):
				summ += abs(modelFrequencyPolish[j] - decypherAttemptAnalysisResult[j])
			if (lang == 1):
                                summ += abs(modelFrequencyEnglish[j] - decypherAttemptAnalysisResult[j])
			if (lang == 2):
                                summ += abs(modelFrequencyFrench[j] - decypherAttemptAnalysisResult[j])
		frequencyComparison[i] = summ
	shift = modelFrequencyEnglish.index(max(modelFrequencyEnglish)) - decypherAttemptAnalysisResult.index(max(decypherAttemptAnalysisResult))
	if (shift<0): shift = 26+shift
	print shift
	nww = shift/nwd(shift, 26)*26
	output = "output.txt"
	rot(shift, nww/shift - 1, f, "output.txt")
elif (sys.argv[1] == "-c"):
	#dokonaj analizy 3 plikow
	print "c"
else:
	print "=================================================================================================================="
	print "Sposob uzycia:\n python analyzeStat.py [-a] Podaj tekst oraz przesuniecie x w ROTx, program policzy ile rotacji nalezy wykonac aby wrocic do tekstu poczatkowego [-b] Odszyfruj tekst z pliku za pomoca analizy statystycznej [-c] Dokonaj analizy statystycznej plikow\n"
	print "=================================================================================================================="

