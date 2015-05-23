# -*- coding: utf-8 -*-
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
        # create group id and make unique url for travel
        group_id = "xxx"
        response = {}

        url = '//{0}/travel/{1}'.format(self.request.host, group_id)
        response = {"group_id": group_id, "url": url}

        return self.write(response)
