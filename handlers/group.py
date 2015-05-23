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
        group_id = str(uuid.uuid4())

        # 旅行プランのフィルタ条件を作成
        rank = self.get_argument("rank", 0)
        budget = 10000
        if rank == 1:
            budget = 30000
        elif rank == 2:
            budget = 80000

        _deadline = datetime.now() + timedelta(minutes=3)
        deadline = _deadline.strftime("%Y/%m/%d %H:%M:%S")

        _query = {
            "budget": budget,
            "deadline": deadline
        }
        query = parse.urlencode(_query)

        # urlの作成
        url = '//{0}/travel/{1}?{2}'.format(self.request.host, group_id, query)
        response = {"url": url}
        return self.write(response)
