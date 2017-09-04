#!/usr/bin/env python
# coding:utf-8

from config import ALLPATH
from lib.cmds import cmd_parser
from lib.loader import load_paths

if __name__ == '__main__':
	args = cmd_parser()
	print load_paths(args, ALLPATH)