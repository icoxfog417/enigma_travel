# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import calendar
import tornado.web
import tornado.websocket
import tornado.escape as escape


class TravelHandler(tornado.web.RequestHandler):

    def get(self):
        deadline = self.get_query_argument("deadline", "")
        self.render("travel.html", deadline=deadline)


class TrainingHandler(tornado.web.RequestHandler):
    """
    旅行プランをランダムに提示し、ユーザーからのフィードバックを受ける。
    フィードバックはデータベースに格納しておく。
    """

    def get(self, group_id):
        """
        ユーザーに旅行プランを提示する
        :param group_key:
        :return:
        """
        pass

    def post(self, group_id):
        """
        ユーザーからのフィードバックを受ける
        :param group_key:
        :return:
        """
        pass
