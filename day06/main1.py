#encoding: utf-8
import os

def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		lines = [l.strip() for l in f]
	
	banks = [int(x) for x in lines[0].split('\t')]

	states = [banks]
	i  = 0
	while True:
		new_state = [s for s in states[-1]]
		i += 1

		#1. find highest bank
		pos = new_state.index(max(new_state))
		#2. empty selected state
		blocks = new_state[pos]
		new_state[pos] = 0
		#3. distribute banks
		while blocks > 0:
			pos = (pos + 1) % len(new_state)
			new_state[pos] += 1
			blocks -= 1
		#print '{0}: {1}'.format(i, ' '.join([str(x) for x in new_state]))
		if new_state in states:
			print i
			break
		else:
			states.append(new_state)
	

if __name__ == '__main__':
	main()