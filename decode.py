
def decode(serect):
	s=''
	for c in serect:
		x=ord(c)
		y=chr(x-1)
		s=s+y
	print s[::-1]



h = "~88:36e1bg8438e41757d:29cgeb6e48c`GUDTO|;hbmg"
decode(h)
