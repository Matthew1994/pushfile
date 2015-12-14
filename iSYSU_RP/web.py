#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import tornado.web
import tornado.wsgi
import tornado.ioloop
import os
from tornado.concurrent import Future
from tornado import gen
from tornado.options import define, options, parse_command_line

define("port", default=8000, help="run on the given port", type=int)


class QueryHandler(tornado.web.RequestHandler):
	def get(self, word):
		self.render('RPIndex.html');

class RPIndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('RPIndex.html');

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
		 (r'/RPTest',RPIndexHandler),],
		template_path=os.path.join(os.path.dirname(__file__), "templates"),
    	static_path=os.path.join(os.path.dirname(__file__), "static"),
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()