# -*- coding: utf-8 -*-
from models.travel_model import Travel


class UBICApi:
    """
    UBICのAPIにアクセスし、学習/予測を行う
    """
    def __init__(self):
        """
        APIキーやカテゴリIDなどを設定
        :return:
        """
        pass

    def train(self, group_id, travel_feedbacks):
        """
        グループに対して、気に入った/気に入らなかったプランのデータを学習させる
        :param group_id:
        :param travel_feedbacks:
        :return:
        """
        return True

    def predict(self, group_id):
        """
        グループにおける旅行プランのリスト(スコアで降順ソート)を返す
        :param group_id:
        :return:
        """
        candidates = [Travel(
            "1",
            "Marin Travel",
            "http://www.jtb.co.jp/kokunai/pkg/tourdetail.aspx?tourcd=13KZ000751AA01000000&dept=TYO&brand=tourdom&SearchType=standard&TourConFlg=NX&TransType=1",
            "http://dom.jtb.co.jp/yado/photo2/LL/8/8715015/87150151000065600.jpg",
            10000
        )]
        return candidates
