# -*- coding: utf-8 -*-
import uuid
from datetime import datetime, timedelta
import urllib.parse as parse
import tornado.web


class GroupHandler(tornado.web.RequestHandler):
    """
    旅行を検討するためのグループを作成する。
    具体的には、一意のurlを発行する。金額の情報はクエリ引数に込める
    """

    def post(self):
        """
        グループURLの作成
        :return:
        """
        # 一意のグループIDを作成
        group_id = uuid.uuid4().int & (1<<16)-1

        # 旅行プランのフィルタ条件を作成
        budget = int(self.get_argument("budget", "0"))
        deadline = self.get_argument("deadline", "1111/11/11 11:11:11")

        _query = {
            "budget": budget,
            "deadline": deadline
        }
        query = parse.urlencode(_query)

        # urlの作成
        url = '//{0}/travel/{1}?{2}'.format(self.request.host, group_id, query)
        response = {"url": url}
        return self.write(response)
