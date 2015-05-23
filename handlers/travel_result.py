# -*- coding: utf-8 -*-
import tornado.web
from models.travel_model import Travel
from service.ubic_api import UBICApi


class TravelResultHandler(tornado.web.RequestHandler):
    """
    グループに対し、学習した結果の旅行プランを提示する。
    """

    def get(self, group_id):
        budget = int(self.get_query_argument("budget", "10000"))
        filter = {
            "budget": budget
        }

        result = self.__decide_travel(group_id, filter)
        self.render("travel_result.html", result=result)

    def __decide_travel(self, group_id, filter):
        """
        学習結果を基に、旅行プランを提案する
        :return:
        """
        api = UBICApi()
        # 学習が済んでいるかをチェック
        is_trained = False

        if not is_trained:
            train_data = []  #DBに保管しておいた学習データを取得
            api.train(group_id, train_data)

        candidates = api.predict(group_id)

        # filterとして渡された条件で絞り込み
        filtered = candidates

        # 上位一件を取得
        result = filtered[0]

        return result
