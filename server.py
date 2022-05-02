# --- Important ---
# python-escpos,python-barcode must be install
# pip install python-escpos
# pip install python-barcode
# -----------------

import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import tornado.httpserver
import os
import json
from tornado.options import define, options
import io

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
                    (r"/",MainHandler)
                   ]
        settings = dict(
            cookie_secret="A6r4k4d46r4",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=False,
            debug=True
        )
        super().__init__(handlers, **settings)

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("home.html")

def main():
    app = Application()
    app.listen(2385)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
