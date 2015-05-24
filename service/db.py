# -*- coding: utf-8 -*-
import psycopg2
import yaml
import os

class Db:
    """
    データベースへのアクセスを行うためのサービス
    """
    def __init__(self):
      # os.path.dirname(__file__)
      config = yaml.load(open(os.path.join(os.path.dirname(__file__), "../", "database.yml")))
      self.conn = psycopg2.connect(
        database = config["dbname"],
        user = config["user"],
        password = config["password"],
        host = config["host"],
        port = config["port"])
      self.cur = self.conn.cursor()

    def select(self, sql):
      self.cur.execute(sql)
      return self.cur.fetchone()

    def update(self, sql):
      self.cur.execute(sql)
      self.conn.commit()
