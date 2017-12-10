#encoding: utf-8
import os
import re

def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		lines = [l.strip() for l in f]
	
	nodes = {}
	# each node is a tuple defined by: name, weight, parent

	def update_node(name, weight = 0, parent = None):
		node = nodes.get(name, {'weight' : weight, 'parent' : parent})
		if parent:
			node['parent'] = parent
		if weight:
			node['weight'] = weight
		nodes[name] = node

	r = re.compile('(\w+) \((\d+)\)')
	for l in lines:
		parts = l.split('->')
		name, weight = r.match(parts[0]).groups()
		children = [] if len(parts) == 1 else [x.strip() for x in parts[1].split(',')]
		map(lambda c: update_node(c, parent = name), children)
		update_node(name, weight)

	root = {k: v for k, v in nodes.iteritems() if v['parent'] is None}.keys()[0]
	print root
	
	# def print_branch(name, indent = 0):
	# 	print '\t' * indent, name
	# 	children = {k: v for k, v in nodes.iteritems() if v['parent'] == name}
	# 	for k in children:
	# 		print_branch(k, indent + 1)
	# print_branch(root)
		

		
	

if __name__ == '__main__':
	main()