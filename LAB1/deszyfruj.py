import string
import sys

text = sys.argv[1]
code = int(sys.argv[2])

print text
print code

code = code % 26
text = list(text)

i=0

for i in range(len(text)):
	a = ord(text[i])
	nowy = a+code

	if a == 32: 
		continue

	if a >= 65 and a <= 90: 
		if nowy > 90:
			nowy = a + code - 26
		text[i] = chr(nowy)

	if a >= 97 and a <= 122:
		if nowy > 122: 
			nowy = a+code - 26
		text[i] = chr (nowy)		

#print '%i - %s' % (a,z) 

text = "".join(text)
print text


