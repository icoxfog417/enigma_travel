# -*- coding: utf-8 -*-
from json_serializable import JsonSerializable


class Travel(JsonSerializable):
    """
    旅行プランを表現するクラス
    """

    def __init__(self, travel_id, title, url, image_url, budget):
        super().__init__()
        self.travel_id = travel_id
        self.title = title
        self.url = url
        self.image_url = image_url
        self.budget = budget
