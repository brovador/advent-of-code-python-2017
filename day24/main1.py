#encoding: utf-8
import os
import re
import string
import sys

max_strength = 0

def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:	
		lines = [map(int, l.strip().split('/')) for l in f]

	ports = sorted([line + [sum(line)] for line in lines], lambda x, y: x[2] > y[2])
	starting_ports = [port for port in ports if port[0] == 0]
	
	def add_port(port_list, remaining_ports):
		global max_strength
		candidates = [port for port in remaining_ports if port[0] == port_list[-1][1] or port[1] == port_list[-1][1]]
		if candidates == []:
			# end of the list
			strength = sum([port[2] for port in port_list])
			if strength > max_strength:
				max_strength = strength
				print port_list
		else:
			for c in candidates:
				new_remaining_ports = [port for port in remaining_ports if port != c]
				c = c if c[0] == port_list[-1][1] else [c[1], c[0], c[2]]
				new_port_list = port_list[:] + [c]
				add_port(new_port_list, new_remaining_ports)
	
	for starting_port in starting_ports:
		port_list = [starting_port]
		remaining_ports = [port for port in ports if port != starting_port]
		add_port(port_list, remaining_ports)
	print max_strength



if __name__ == '__main__':
	main()