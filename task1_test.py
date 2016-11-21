import random
import string
from unittest import TestCase
from task import reg_replace, split_replace, pos_replace

def add_bracket(s):
	s = list(s)
	l = len(s)
	tp = bool(random.getrandbits(1))
	smb = ('(' if tp else ')')
	s[random.randint(0,l-1)] = smb
	s = ''.join(s)
	return s

def get_string_with_braces(n):
	yield 'asdjlk123j()())((()))(asdasd'
	yield 'asdjlk123j()())((((asdas)))('

	for x in range(n):
		random_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(64)])
		for x in range(random.randint(2,20)):
			random_string = add_bracket(random_string)
		yield random_string

if __name__ == '__main__':
	for s in get_string_with_braces(100):
		s1 = reg_replace(s)
		s2 = split_replace(s)
		s3 = pos_replace(s)
		eq = True if s1==s2==s3 else False

		if not eq:
			print('{} - Input string: \n-----'.format(s))
			print('{} - ({}, replaced with regex): '.format(s1, eq))
			print('{} - ({}, replaced with split): '.format(s2, eq))
			print('{} - ({}, replaced with pos): '.format(s3, eq))


	# for item in get_string_with_braces(50):
	#   print(item)

# # class CommandLineTestCase(TestCase):
# #     """
# #     Base TestCase class, sets up a CLI parser
# #     """
# #     @classmethod
# #     def setUpClass(cls):
# #         parser = create_parser()
# #         cls.parser = parser

# class PingTestCase(TestCase):

#     # def test_with_empty_args():
#     #     """
#     #     User passes no args, should fail with SystemExit
#     #     """                                    
#     #     with self.assertRaises(SystemExit):
#     #         get_string(parse_args)

#     def test_db_servers_ubuntu_ami_in_australia():
#         """
#         Find database servers with the Ubuntu AMI in Australia region
#         """
#         args = self.parser.parse_args(['-i', 'idbs81839'])
#         result = ping(args.tags, args.region, args.ami)
#         self.assertIsNotNone(result)
#         # Do some othe assertions on the result
