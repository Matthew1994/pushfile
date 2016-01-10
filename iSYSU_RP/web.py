#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import tornado.web
import tornado.wsgi
import tornado.ioloop
import os
import urllib2
from tornado.concurrent import Future
from tornado import gen
from tornado.options import define, options, parse_command_line

define("port", default=8888, help="run on the given port", type=int)


class QueryHandler(tornado.web.RequestHandler):
	def get(self, word):
		dic = {"a":"-1000", "b":"-520", "c":"-0.01", "d":"1",
			   "e":"11.11", "f":"12", "g":"50", "h":"78", "i":"120",
			   "j":"1234", "k":"110", "l":"119", "m":"80", "n":"47", 
			   "o":"59", "p":"666", "q":"15", "r":"2000", "s":"500",
			   "t":"2121", "u":"100000+", "v":"365", "w":"-0.00001",
			   "x":"0", "y":"4", "z":"2333"}
		word = word.lower()
		self.render('result.html', char=word[0], value=dic.get(word[0]));

class RPIndexHandler(tornado.web.RequestHandler):
	def get(self):
		url = "http://isysu.sysu.edu.cn/RPTest"
		post_data = {}
		for key in self.request.arguments:
			post_data[key] = self.get_arguments(key)[0]
		if len(post_data) is not 0:
			print "len(post_data) is not 0"
			url = url+'?'
			for key in post_data:
				url = url + str(key) + "=" + str(post_data[key]) + "&"
			url = url[0:len(url)-1]
		print url
		self.render('RPIndex.html');

class GetWordInfoHandler(tornado.web.RequestHandler):
	def get(self, word):
		res = urllib2.urlopen('https://api.shanbay.com/bdc/search/?word='+word)
		self.write(res.read())

"""
#对于python3的tornado3.1要用下面写法
wsgi_app = tornado.wsgi.WSGIApplication(
	[(r'/QueryWord/([a-zA-Z]+)',QueryHandler),
	 (r'/RPTest',RPIndexHandler),],
	template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
)

#对于python2的tornado4.2要用下面的写法

app = tornado.web.Application(
	[(r'/',QueryHandler),]
)

wsgi_app = tornado.wsgi.WSGIAdapter(app)
"""

if __name__ == "__main__":
    parse_command_line()
    app = tornado.web.Application(
    	[(r'/QueryWord/([a-zA-Z]+)',QueryHandler),
		 (r'/RPTest',RPIndexHandler),
		 (r'/GetWordInfo/([a-zA-Z]+)', GetWordInfoHandler),],
		template_path=os.path.join(os.path.dirname(__file__), "templates"),
    	static_path=os.path.join(os.path.dirname(__file__), "static"),
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()