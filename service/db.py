# -*- coding: utf-8 -*-
import os
import urllib.parse
import psycopg2
import yaml

class Db:
    """
    データベースへのアクセスを行うためのサービス
    """
    def __init__(self):
        # os.path.dirname(__file__)
        try:
            config = yaml.load(open(os.path.join(os.path.dirname(__file__), "../", "database.yml")))
            self.conn = psycopg2.connect(
                database=config["dbname"],
                user=config["user"],
                password=config["password"],
                host=config["host"],
                port=config["port"])
        except Exception as ex:
            # read from env parameter
            url = urllib.parse.urlparse(os.environ["DATABASE_URL"])
            self.conn = psycopg2.connect(
                database=url.path[1:],
                user=url.username,
                password=url.password,
                host=url.hostname,
                port=url.port)

        self.cur = self.conn.cursor()

    def execute(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchone()
