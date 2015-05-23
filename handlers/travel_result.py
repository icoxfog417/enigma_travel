# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import calendar
import tornado.web
import tornado.websocket
import tornado.escape as escape


class TravelResultHandler(tornado.web.RequestHandler):
    """
    グループに対し、学習した結果の旅行プランを提示する。
    """

    def get(self, group_id):
        result = self.__decide_travel()
        self.render("result.html", result=result)

    def __decide_travel(self):
        """
        学習結果を基に、旅行プランを提案する
        :return:
        """
        pass
