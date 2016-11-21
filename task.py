#!/usr/bin/python

import sys, getopt
import re 

def get_string(argv, strg='', frmt=False, alg='reg'):
	try:
		opts, args = getopt.getopt(argv,'hfi:',['string='])
	except getopt.GetoptError:
		print ('task1.py -i <string>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('task1.py -i <string:input> -a <string:algo>')
			sys.exit()
		elif opt == '-f':
			frmt = True
		elif opt == '-a':
			alg = arg
		elif opt in ('-i', '--string'):
			strg = arg
		else:
			assert False, 'unhandled option'

	if strg=='':
		assert False, 'empty string'

	return strg, frmt

def reg_replace(s):
	return re.sub('(?!.*\).*)(\(.*)', '', s)

def split_replace(s):
	s = s.split('(')
	n = 0
	gr = len(s)

	for q in range(gr):
		part = s[-(q+1)] 
		if ')' not in part:
			n+=1
		else:
			break

	p = n-1 if n == gr else n

	for x in range(p):
		s.pop() 

	return '('.join(s)


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def pos_replace(s):
	n = len(s)
	cut = n
	opn = list(find_all(s, '('))
	clz = list(find_all(s, ')'))
	n_opn = len(opn)
	n_clz = len(clz)

	if n_opn==0:
		return s
	elif n_clz==0:
		return s[:min(opn)]
	else:
		m_clz = max(clz)
		rev = list(reversed(opn))
		for x in rev:
			if x > m_clz:
				cut = x

	p = cut-1 if cut == n else cut

	return s[:cut]


def main(argv):
	s, frmt = get_string(argv)
	s1 = reg_replace(s)
	s2 = split_replace(s)
	s3 = pos_replace(s)

	if frmt and s1!=s2: 
		print('Input string: {}\n-----'.format(s))
		print('Output string (replaced with regex): {}'.format(s1))
		print('Output string (replaced with split): {}'.format(s2))
	else:
		print ('\n'.join([s1, s2]))


if __name__ == "__main__":
	main(sys.argv[1:])