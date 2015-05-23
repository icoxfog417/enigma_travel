# -*- coding: utf-8 -*-
import tornado.web
from models.travel_model import Travel


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
        t = Travel(
            "1",
            "Sample Travel",
            "http://www.jtb.co.jp/kokunai/pkg/tourdetail.aspx?tourcd=13KZ000751AA01000000&dept=TYO&brand=tourdom&SearchType=standard&TourConFlg=NX&TransType=1",
            "http://dom.jtb.co.jp/yado/photo2/LL/8/8715015/87150151000065600.jpg",
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
