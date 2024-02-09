import numpy as np
import pandas as pd
import mysql.connector
from databases import Database

class LogFillDB():

    def __init__(self, host, user, password, database_name):
        self.mydb = mysql.connector.connect(host=host, user=user, password=password, database=database_name)
        self.mycursor = self.mydb.cursor()

    def sub_table(self, id, table_1: str, table_2: str) -> list:
        query = f"""
        SELECT DISTINCT {id}
        FROM `{table_1}`
        WHERE A NOT IN (
            SELECT DISTINCT {id}
            FROM `{table_2}`
        )
        """
        self.mycursor.execute(query)
        results = self.mycursor.fetchall()
        return results

    # TODO: Take the difference and fill in the missing parts of table_1 with logs.

    def __del__(self):
        self.mycursor.close()
        self.mydb.close()
