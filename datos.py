import mysql.connector

config = {'user': 'juan',
          'password': '123456',
          'host': '127.0.0.1',
          'database': 'cine'}

class Datos:
    def __init__(self):
        self.conn = mysql.connector.connect(**config)
        self.cur = self.conn.cursor()

    def create_database(self):
        pass

    def get_tasks(self):
        pass

    def set_task(self, task):
        pass

    def del_task(self, task_id):
        pass

    def update_task(self, task_id, detalle):
        pass