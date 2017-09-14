#!/usr/bin/env python
# coding:utf-8

import urllib
import requests
import threadpool

class Scanner(object):

	def __init__(self, thread=10, timeout=30):
		if not isinstance(thread, (int, )) or thread < 1 or thread > 15:
			raise ValueError('Invalid threads count')
		self.thread_count = thread
		self.timeout = timeout

	def scan(self, urls, paths):
		for url in urls:
			queue = [url + path for path in paths]
			self.thread_pool = threadpool.ThreadPool(self.thread_count)
			requests_ = threadpool.makeRequests(self._scan, queue)
			[self.thread_pool.putRequest(req) for req in requests_]

			self.thread_pool.wait()

	def _scan(self, url):
		try:
			resp = requests.get(url, timeout=self.timeout)
			# print '%s\t\t%s' % (url, str(resp.status_code))
			if resp.status_code:
				print '%s\t\t%s' % (url, str(resp.status_code))

		except requests.ConnectionError as e:
			print 'sorry, u are blacklisted now!'
			
		except (requests.HTTPError, requests.Timeout) as e:
			print '%s\t\terror' % url
