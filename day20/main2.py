#encoding: utf-8
import os
import re
import string
import sys


def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:	
		lines = [l.strip() for l in f]

	r = re.compile('p=<([ \-\d,+]+)>, v=<([ \-\d,+]+)>, a=<([ \-\d,+]+)>')
	particles = []
	for line in lines:
		m = r.match(line)
		if m:
			pos, vel, acc = m.groups()
			particle = {}
			particle['p'] = [int(x) for x in pos.split(',')]
			particle['v'] = [int(x) for x in vel.split(',')]
			particle['a'] = [int(x) for x in acc.split(',')]
			particles.append(particle)
	
	iterations = 1000
	for i in range(iterations):

		positions = {}

		# update particles
		for particle in particles:
			#increase velocity
			particle['v'] = map(lambda i: particle['v'][i] + particle['a'][i], range(3))
			#increase position
			particle['p'] = map(lambda i: particle['p'][i] + particle['v'][i], range(3))

			pos_key = ','.join([str(x) for x in particle['p']])
			arr = positions.get(pos_key, [])
			arr.append(particle)
			positions[pos_key] = arr
		
		for k, v in positions.iteritems():
			if len(v) > 1:
				map(lambda p: particles.remove(p), v)
	print len(particles)
		

		
	





	

	

if __name__ == '__main__':
	main()