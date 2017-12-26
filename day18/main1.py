#encoding: utf-8
import os
import re
import string
import sys


def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:	
		lines = [l.strip() for l in f]

	registers = { 'pc': 0, 'last_sound': -1 }

	def get_value(x):
		return int(x) if x.lstrip('-').isdigit() else registers.get(x, 0)

	def op_snd(x):
		registers['last_sound'] = get_value(x)
	
	def op_set(x, y):
		registers[x] = get_value(y)

	def op_add(x, y):
		registers[x] = registers.get(x, 0) + get_value(y)
	
	def op_mul(x, y):
		registers[x] = registers.get(x, 0) * get_value(y)

	def op_mod(x, y):
		registers[x] = registers.get(x, 0) % get_value(y)
	
	def op_rcv(x):
		x = get_value(x)
		if x != 0:
			print registers['last_sound']
			registers['pc'] = sys.maxint
	
	def op_jgz(x, y):
		x, y = get_value(x), get_value(y)
		if x > 0:
			registers['pc'] += y - 1


	operations = [
		(re.compile('snd (\w+)'), op_snd),
		(re.compile('set (\w+) (-?\w+)'), op_set),
		(re.compile('add (\w+) (-?\w+)'), op_add),
		(re.compile('mul (\w+) (-?\w+)'), op_mul),
		(re.compile('mod (\w+) (-?\w+)'), op_mod),
		(re.compile('rcv (\w+)'), op_rcv),
		(re.compile('jgz (\w+) (-?\w+)'), op_jgz),
	]

	def exec_operation(line):
		for op in operations:
			m = op[0].match(line)
			if m:
				op[1](*m.groups())
				break
		else:
			print 'Operation not found: {0}'.format(line)

	def print_state(line):
		print line
		print registers	
		raw_input()

	registers['pc'] = -1
	while True:
		registers['pc'] += 1
		line = lines[registers['pc']]
		exec_operation(line)
		#print_state(line)
		if registers['pc'] >= len(lines):
			break
	

if __name__ == '__main__':
	main()