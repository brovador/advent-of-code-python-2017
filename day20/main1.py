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

		# update particles
		for particle in particles:
			#increase velocity
			particle['v'] = map(lambda i: particle['v'][i] + particle['a'][i], range(3))
			#increase position
			particle['p'] = map(lambda i: particle['p'][i] + particle['v'][i], range(3))
			#calculate distance
			particle['d'] = sum([abs(x) for x in particle['p']])
		
		min_particle = min(particles, key = lambda x: x['d'])
		min_particle['min_count'] = min_particle.get('min_count', 0) + 1
	

	idx = particles.index(max(particles, key = lambda x: x.get('min_count', 0)))
	print idx
		

		
	





	

	

if __name__ == '__main__':
	main()