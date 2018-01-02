'''
Rewritten python optimized code
'''

b = 106700
c = 123700
d = 2
h = 1
d = 0
e = 0
h = 0
while b <= c: #(9-32)
	f = 1
	d = 2
	for d in range(d, b / 2): #(11-24)
		if b % d == 0:
			f = 0
			break
	if f == 0:
		h += 1
	b += 17
print h

			