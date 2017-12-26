#encoding: utf-8
import os
import re
import string
import sys


def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:	
		lines = [l.strip() for l in f]

	registers = {}
	programs = [
		{'idx': 0, 'p': 0, 'pc': 0, 'messages': [], 'deadlock': 0, 'send_count': 0 },
		{'idx': 1, 'p': 1, 'pc': 0, 'messages': [], 'deadlock': 0, 'send_count': 0 }
	]

	def get_value(x):
		return int(x) if x.lstrip('-').isdigit() else registers.get(x, 0)

	def op_snd(x):
		x = get_value(x)
		other_pid = 1 if registers['idx'] == 0 else 0
		programs[other_pid]['messages'].append(x)
		registers['send_count'] += 1
		registers['pc'] += 1
	
	def op_set(x, y):
		registers[x] = get_value(y)
		registers['pc'] += 1

	def op_add(x, y):
		registers[x] = registers.get(x, 0) + get_value(y)
		registers['pc'] += 1
	
	def op_mul(x, y):
		registers[x] = registers.get(x, 0) * get_value(y)
		registers['pc'] += 1

	def op_mod(x, y):
		registers[x] = registers.get(x, 0) % get_value(y)
		registers['pc'] += 1
	
	def op_rcv(x):
		if len(registers['messages']) > 0:
			registers[x] = registers['messages'][0]
			del registers['messages'][0]
			registers['deadlock'] = 0
			registers['pc'] += 1
		else:
			registers['deadlock'] += 1
			return -2
	
	def op_jgz(x, y):
		x, y = get_value(x), get_value(y)
		if x > 0:
			registers['pc'] += y
		else:
			registers['pc'] += 1


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
		result = 0
		for op in operations:
			m = op[0].match(line)
			if m:
				result = op[1](*m.groups())
				break
		else:
			result = -1
		return result or 0

	def print_state(pid, line, result):
		print 'PID: ', pid
		print line, 'return: {0}'.format(result)
		print programs[0]
		print programs[1]
		raw_input()

	pid = 0
	while True:
		registers = programs[pid]
		line = lines[registers['pc']]
		result = exec_operation(line)
		#print_state(pid, line, result)

		if programs[0]['deadlock'] > 1 and programs[1]['deadlock'] > 1:
			break

		if result == -1:
			break
		elif result == -2:
			pid = 1 if pid == 0 else 0
		
		if registers['pc'] >= len(lines):
			break
	
	print programs[1]['send_count']
	

if __name__ == '__main__':
	main()