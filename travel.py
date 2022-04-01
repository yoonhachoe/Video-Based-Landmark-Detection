#!/usr/bin/python3
#-*- coding: utf-8 -*-
print("Content-Type: text/html; charset=UTF-8\n")
print()
import cgi
form = cgi.FieldStorage()
print('''<!doctype html>
<html>
<head>
  <title>Travelog - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="travel.py">Travelog</a></h1>
  <p><h3>Type a URL.</h3></p>
  <form action="process_create.py" method="get">
    <p><input type="url" name="link" placeholder=" Type a URL"> <input type="submit" value="Search"></p>
  </form>
</body>
</html>
''')
