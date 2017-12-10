#encoding: utf-8
import os
import re

def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		lines = [l.strip() for l in f]
	
	r = re.compile('(\w+) (inc|dec) (-?\d+) if (\w+) (>|<|>=|<=|==|!=) (-?\d+)')
	registers = {}

	operations = {
		'inc' : lambda x, y: x + y,
		'dec' : lambda x, y: x - y
	}

	conditions = {
		'>' : lambda x, y: x > y,
		'>=' : lambda x, y: x >= y,
		'<' : lambda x, y: x < y,
		'<=' : lambda x, y: x <= y,
		'==' : lambda x, y: x == y,
		'!=' : lambda x, y: x != y
	}

	max_stored_value = 0
	for l in lines:
		m = r.match(l)
		r1, op, val1, r2, condition, val2 = m.groups()
		val1, val2 = int(val1), int(val2)

		reg1 = registers.get(r1, 0)
		reg2 = registers.get(r2, 0)
		if conditions[condition](reg2, val2):
			registers[r1] = operations[op](reg1, val1)
			max_stored_value = max(max_stored_value, registers[r1])
	
	print max_stored_value

		
			

		


		

		
	

if __name__ == '__main__':
	main()