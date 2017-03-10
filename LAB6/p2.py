import sys,math
n=int(sys.argv[1])
tab = []
for i in range (0,n+1):
	tab.append(1)

for i in range(2,int(math.floor(math.sqrt(n+1))+1)):
	if tab[i] == 1:
		j = i
		while j < n:
			j += i
			if j>n:
				break
			tab[j] = 0

if tab[n] == 1:
	print 'Ta liczba jest pierwsza'
else:
	print 'Ta liczba nie jest pierwsza'
	
