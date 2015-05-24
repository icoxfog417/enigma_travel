# -*- coding: utf-8 -*-
import tornado.web
from models.travel_model import Travel
from service.db import Db
import json


class TravelHandler(tornado.web.RequestHandler):

    def get(self, group_id):
        deadline = self.get_query_argument("deadline", "")
        # deadline を過ぎていたら、resultの方に遷移

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

        db = Db()
        result = db.execute("select * from travels order by RANDOM() limit 1")
        travel_json = json.loads(result[5])

        t = Travel(
            result[0],
            result[2],
            travel_json["urls"]["mobile"],
            travel_json["img"][0]["l"],
            10000
        )
        self.write(t.to_dict())

    def post(self, group_id):
        """
        ユーザーからのフィードバックを受ける
        :param group_key:
        :return:
        """
        travel_id = self.get_argument("travel_id", default="")
        _is_like = self.get_argument("is_like", default="false")
        is_like = False
        if _is_like == "true":
            is_like = True

        # DBへフィードバック結果を保管

        self.write({})
