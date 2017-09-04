#!/usr/bin/env python
# coding:utf-8

import os
import argparse

def cmd_parser():
	parser = argparse.ArgumentParser(description='User info')

	parser.add_argument('url', type=str,
						help='target url(e.g. "http://www.site.com/path1/path2...")')
	parser.add_argument('-t', '--threads', type=int, default=10,
						help='thread count of detect webpath')
	parser.add_argument('--jsp', action='store_true',
						help='use .jsp common paths')
	parser.add_argument('--asp', action='store_true',
						help='use .asp common paths')
	parser.add_argument('--aspx', action='store_true',
						help='use .aspx common paths')
	parser.add_argument('--php', action='store_true',
						help='use .php common paths')
	parser.add_argument('--dir', action='store_true',
						help='use webserver common paths')
	parser.add_argument('--no-recursion', action='store_true',
						help='detect path without recursion')

	args = parser.parse_args()
	allpath = [args.dir, args.jsp, args.php, args.asp, args.aspx]
	if not any(allpath):
		parser.print_help()
		raise SystemExit

	return args

if __name__ == '__main__':
	args = cmd_parser()
	print args.asp

