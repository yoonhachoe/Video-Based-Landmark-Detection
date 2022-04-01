#!/usr/bin/python3
#-*- coding: utf-8 -*-
print("Content-Type: text/html; charset=UTF-8\n")
print()
import cgi
import sys
sys.path.append('/usr/lib/python3.7/dist-packages/')
form = cgi.FieldStorage()
url = form["link"].value
print(url)
print()
