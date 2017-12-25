#encoding: utf-8
import os
import re
import string


def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		lines = [l.strip() for l in f]

	n = 16
	programs = list(string.letters[:n])

	def command_spin(a, n):
		n = int(n)
		return a[-n:] + a[:-n]

	def command_exchange(a, p1, p2):
		p1, p2 = map(int, [p1, p2])
		a[p1], a[p2] = a[p2], a[p1]
		return a

	def command_partner(a, p1, p2):
		ip1 = a.index(p1)
		ip2 = a.index(p2)
		a[ip1], a[ip2] = a[ip2], a[ip1]
		return a

	commands = [
		(re.compile('s(\d+)'), command_spin),
		(re.compile('x(\d+)\/(\d+)'), command_exchange),
		(re.compile('p(\w+)\/(\w+)'), command_partner),
	]
	
	moves = map(string.strip, lines[0].split(','))
	for move in moves:
		command = None
		for expr, command in commands:
			m = expr.match(move)
			if m:
				args = (programs, ) + m.groups()
				programs = command(*args)
				break
	print ''.join(programs)
	



	
	

if __name__ == '__main__':
	main()