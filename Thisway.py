#!/usr/bin/env python
# coding:utf-8

from config import ALLPATH
from lib.cmds import cmd_parser
from lib.scanner import Scanner
from lib.loader import load_urls
from lib.loader import load_paths

if __name__ == '__main__':
	args = cmd_parser()
	urls = load_urls(args)
	paths = load_paths(args, ALLPATH)
	scanner = Scanner(args.threads)

	scanner.scan(urls, paths)