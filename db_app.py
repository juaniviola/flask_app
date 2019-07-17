from sqlalchemy import create_engine
from sqlalchemy import Column, Table, Integer, String, MetaData, ForeignKey

DB_URL = "sqlite:///db.sqlite"
DB_TABLE = "flask"

class MyDataBase:
  db_engine = None
  def __init__(self, dbname):
    self.db_engine = create_engine(dbname)

  def create_table(self, table_name=''):
    metadata = MetaData()
    table = Table(table_name, metadata,
      Column('id', Integer, primary_key=True, autoincrement=True),
      Column('username', String),
      Column('fullname', String),
      Column('email', String),
      Column('age', Integer)
    )

    try:
      metadata.create_all(self.db_engine)
      print('tables created')
    except Exception as e:
      print('[ErrorDB] {}'.format(e))

  def execute_query(self, query=''):
    if query == '': return
    with self.db_engine.connect() as connection:
      try:
        connection.execute(query)
      except Exception as e:
        print('[ErrorDB] {}'.format(e))

  def query_all_data(self, table=''):
    if table == '': return
    with self.db_engine.connect() as connection:
      try:
        result = connection.execute("SELECT * FROM '{}'".format(table))
        res = result.fetchall()
        return res
      except Exception as e:
        print('[ErrorDB] {}'.format(e))

  def query_one(self, query):
    with self.db_engine.connect() as connection:
      try:
        result = connection.execute(query)
        res = result.fetchall()
        return res
      except Exception as e:
        print('[ErrorDB] {}'.format(e))