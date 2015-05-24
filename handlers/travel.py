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

        _budget = int(self.get_argument("budget", default=0))
        if  _budget == 0:
            budget = 50000
        elif _budget == 1:
            budget = 100000
        elif _budget == 2:
            budget = 150000

        db = Db()
        result = db.select("select * from travels where price_max <= {0} order by RANDOM() limit 1".format(budget))
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

        db = Db()
        training = db.select("select id, relevant, not_relevant from trainings where group_id = {0}".format(group_id))

        if training is None :
            relevant = []
            not_relevant = []
        else :
            if training[1] == "" :
                relevant = []
            else :
                relevant = training[1].split(",")

            if training[2] == "" :
                not_relevant = []
            else:
                not_relevant = training[2].split(",")

        if is_like :
            relevant.append(travel_id)
        else:
            not_relevant.append(travel_id)

        if training is None :
            db.update("insert into trainings (group_id, relevant, not_relevant) values({0}, '{1}', '{2}')".format(group_id, ",".join(relevant), ",".join(not_relevant)))
        else:
            db.update("update trainings set relevant = '{0}', not_relevant = '{1}' where id = {2}".format(",".join(relevant), ",".join(not_relevant), training[0]))

        # DBへフィードバック結果を保管

        self.write({})
