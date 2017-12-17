#encoding: utf-8
import os
import operator

def __knot_hash(line):
	n = 256
	rounds = 64
	
	skip_size = 0
	position = 0
	lengths = [ord(x) for x in line]
	lengths += [17, 31, 73, 47, 23]
	numbers = range(n)

	def debug_print():
		result = []
		for i, x in enumerate(numbers):
			if i == position % len(numbers):
				result.append('[{0}]'.format(x))
			else:
				result.append(str(x))
		return ','.join(result)
	
	for r in range(rounds):
		for l in lengths:
			tmp = []
			for i in range(l):
				p = (position + i) % len(numbers)
				tmp.append(numbers[p])
			tmp = tmp[::-1]
			for i in range(l):
				p = (position + i) % len(numbers)
				numbers[p] = tmp[i]
			position += l + skip_size
			skip_size += 1
	
	chunks = zip(*[iter(numbers)] * 16)
	chunks = map(lambda c: reduce(operator.__xor__, c), chunks)
	return ''.join(map(lambda x: '{:02x}'.format(x), chunks))



def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		lines = [l.strip() for l in f]

	key = lines[0]
	rows = ['{0}-{1}'.format(key, i) for i in range(128)]
	count = 0
	for r in rows:
		kh = __knot_hash(r)
		bkh = ''.join(map(lambda x: '{0:04b}'.format(int(x, 16)), kh))
		count += len(filter(lambda x: x == '1', bkh))
	print count
	

if __name__ == '__main__':
	main()