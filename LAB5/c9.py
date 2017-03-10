import sys

def trivial_hash(dane):
        hash = 0
        for znak in dane:
                hash += ord(znak)
        return hash % 999

plik = sys.argv[1]

print 'Trivial hash %s' % trivial_hash(plik)
