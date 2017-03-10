import sys,math

n = int(sys.argv[1]) 


entropiaAES = 256 * math.log(2,2)

for i in range(256):
	entropia = i * math.log(n,2)
	
	if(entropia > entropiaAES):
		print 'Dla dlugosci %d entropia wynosi %.2f (alfabet %d znakow)' % (i, entropia, n)
		print 'Jest wieksza od entropii klucza AES ktora wynosi %.2f' % (entropiaAES)
		break
