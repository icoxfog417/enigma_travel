# -*- coding: utf-8 -*-


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
        pass

    def predict(self, group_id):
        """
        グループに対して、スコアの高いプランを返す
        :param group_id:
        :return:
        """
        pass
