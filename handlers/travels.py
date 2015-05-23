# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import calendar
import tornado.web
import tornado.websocket
import tornado.escape as escape


class TravelsHandler(tornado.web.RequestHandler):
    """

    """

    def get(self, group_key):
        pass