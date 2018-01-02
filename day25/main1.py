#encoding: utf-8
import os
import re
import string
import sys

max_strength = 0

def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		start_state = re.match('Begin in state (\w+)', f.readline()).groups()[0]
		steps = int(re.match('Perform a diagnostic checksum after (\d+) steps.', f.readline()).groups()[0])
		lines = [l.strip() for l in f if l.strip() != '']

		states = {}
		while len(lines):
			state = re.match('In state (\w+):', lines[0]).groups()[0]
			states[state] = {}
			
			del lines[0]
			for i in range(2):
				i = i * 4
				value = int(re.match('If the current value is (\d+):', lines[i]).groups()[0])
				write = int(re.match('- Write the value (\d+).', lines[i + 1]).groups()[0])
				move = re.match('- Move one slot to the (\w+).', lines[i + 2]).groups()[0]
				next_state = re.match('- Continue with state (\w+).', lines[i + 3]).groups()[0]
				states[state][value] = (write, move, next_state)
			lines = lines[8:]
	
	tape = [0] * 1000001
	tape_pos = 0

	def get_tape_value(tape, tape_pos):
		return tape[local_to_world(tape_pos)]

	def set_tape_value(tape, tape_pos, value):
		tape[local_to_world(tape_pos)] = value

	def local_to_world(pos):
		return pos + len(tape) / 2
	
	def print_tape(tape, tape_pos):
		print tape_pos
		x = [str(x) if i != local_to_world(tape_pos) else '[{0}]'.format(x) for i, x in enumerate(tape)]
		print ' '.join(x)
	
	current_state = start_state
	for i in range(steps):
		current_value = get_tape_value(tape, tape_pos)
		write, move, next_state = states[current_state][current_value]
		
		set_tape_value(tape, tape_pos, write)
		tape_pos += 1 if move == 'right' else -1
		current_state = next_state
	print sum(tape)




	





if __name__ == '__main__':
	main()