import string
import sys
import math

def szyfruj(text, code):
	code = int(code) % 26
	text = list(text)
	
	for i in range(len(text)):
		a = ord(text[i])
		nowy = a+code
		
		if a == 32:
			continue
		if a >= 65 and a <= 90:
			if nowy > 90:
				nowy = a + code -26
			text[i] = chr(nowy)
		if a>=97 and a <= 122:
			if nowy > 122:
				nowy = a + code -26
			text[i] = chr(nowy)
	text = "".join(text)
	return text

def NWD(a,b):
	while b!=0:
		b, a = a%b, b
	return a

def NWW(a,b):
	return abs(a*b / NWD(a,b))

n = int(sys.argv[1])
if n < 1:
	sys.exit(0)

text = "Ala ma kota a kot ma Ale"
wynik = NWW(26,n) / n


print '\n %s \n' % (text)
print 'Odpowiedz to %i' % (int(wynik))

for i in range(int(wynik)):
	text = szyfruj(text,n)
	print '%i. %s'%(i, text)
	


