# from termcolor import colored, cprint
from app import app
import db_app

def main():
  app.run(host='0.0.0.0', port='8000', debug=True)
	db = db_app.MyDataBase(dbname=db_app.DB_URL)
	db.create_table(table_name=db_app.DB_TABLE)

if __name__ == '__main__':
  main()