#!/usr/bin/env python
# coding:utf-8

import os

def load_paths(args, paths):
	filepaths = []

	if args.dir:
		filepaths.append(paths['dir'])
	if args.jsp:
		filepaths.append(paths['jsp'])
	if args.php:
		filepaths.append(paths['php'])
	if args.asp:
		filepaths.append(paths['asp'])
	if args.aspx:
		filepaths.append(paths['aspx'])

	return getpaths(filepaths)

def getpaths(filepaths):
	webpaths = []

	for filepath in filepaths:
		if not os.path.exists(filepath):
			raise IOError('FileNotFound!')

		with open(filepath, 'r') as f:
			for _ in f.readlines():
				webpaths.append(_.strip())

	return webpaths