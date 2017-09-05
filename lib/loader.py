#!/usr/bin/env python
# coding:utf-8

import os
import urlparse

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
			print filepath
			raise IOError('FileNotFound!')

		with open(filepath, 'r') as f:
			for _ in f.readlines():
				webpaths.append(_.strip())

	return webpaths


def load_urls(args):
	urls = []
	url = urlparse.urlparse(args.url)
	return geturls(url.scheme, url.netloc, url.path, args.no_recursion)

def geturls(scheme, host, path, flag):
	urls = []
	scheme = getscheme(scheme)
	path_list = path.split('/')
	if '.' in path_list[-1]:
		temp = path_list.pop()
	if flag:
		return scheme + host + '/'.join(path_list)
	else:
		for i in range(len(path_list)):
			urls.append(scheme + host + '/'.join(path_list))
			temp = path_list.pop()
		return urls

def getscheme(scheme):
	if scheme != 'http' and scheme != 'https':
		return 'http://'
	else:
		return scheme + '://'