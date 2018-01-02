#encoding: utf-8
import os
import re
import string
import sys


def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:	
		lines = [l.strip() for l in f]

	registers = { 'pc': 0, 'mul_count' : 0 }

	def get_value(x):
		return int(x) if x.lstrip('-').isdigit() else registers.get(x, 0)

	def op_set(x, y):
		registers[x] = get_value(y)
		registers['pc'] += 1

	def op_sub(x, y):
		registers[x] = registers.get(x, 0) - get_value(y)
		registers['pc'] += 1
	
	def op_mul(x, y):
		registers['mul_count'] += 1
		registers[x] = registers.get(x, 0) * get_value(y)
		registers['pc'] += 1

	def op_jnz(x, y):
		x, y = get_value(x), get_value(y)
		if x != 0:
			registers['pc'] += y
		else:
			registers['pc'] += 1


	operations = [
		(re.compile('set (\w+) (-?\w+)'), op_set),
		(re.compile('sub (\w+) (-?\w+)'), op_sub),
		(re.compile('mul (\w+) (-?\w+)'), op_mul),
		(re.compile('jnz (\w+) (-?\w+)'), op_jnz),
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

	registers['pc'] = 0
	while True:
		line = lines[registers['pc']]
		exec_operation(line)
		#print_state(line)
		if registers['pc'] >= len(lines):
			break
	print registers['mul_count']

if __name__ == '__main__':
	main()