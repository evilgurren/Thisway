#!/usr/bin/env python
# coding:utf-8

import os
from lib.webpaths import BASE_DIR

DIR = os.path.join(BASE_DIR, './data/DIR.txt')
JSP = os.path.join(BASE_DIR, './data/JSP.txt')
ASP = os.path.join(BASE_DIR, './data/ASP.txt')
PHP = os.path.join(BASE_DIR, './data/PHP.txt')
ASPX = os.path.join(BASE_DIR, './data/ASPX.txt')

ALLPATH = {'dir':DIR, 'jsp':JSP, 'asp':ASP, 'php':PHP, 'aspx':ASPX}