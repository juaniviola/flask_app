from flask import Flask, render_template, request, redirect, url_for
import db_app

app = Flask(__name__)

DB_URL = "sqlite:///db.sqlite"
DB_TABLE = "flask"

db = db_app.MyDataBase(dbname=DB_URL)
db.create_table(table_name=DB_TABLE)

@app.route('/')
def index():
	data = db.query_all_data(table=DB_TABLE)
	return render_template('index.html', data=data)

@app.route('/new')
def add_new_member():
	return render_template('new.html')

@app.route('/new', methods=['POST'])
def add_member():
	if request.method == 'POST':
		username = request.form['username']
		fullname = request.form['fullname']
		email = request.form['email']
		age = request.form['age']

		db.execute_query(query="INSERT INTO flask (username, fullname, email, age) VALUES ('{username}', '{fullname}', '{email}', '{age}');".format(username=username, fullname=fullname, email=email, age=age))

		return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete_member(id):
	db.execute_query(query="DELETE FROM flask where id='{}';".format(id))

	return redirect(url_for('index'))

@app.route('/edit/<id>')
def edit(id):
	data = db.query_one(query="SELECT * FROM flask WHERE id='{}';".format(id))

	return render_template('edit.html', user=data[0])

@app.route('/edit/<id>', methods=['POST'])
def edit_data(id):
	if request.method == 'POST':
		username = request.form['username']
		fullname = request.form['fullname']
		email = request.form['email']
		age = request.form['age']
		db.execute_query(query="UPDATE flask SET username='{}', fullname='{}', email='{}', age='{}' WHERE id='{}'".format(username, fullname, email, age, id))

		return redirect(url_for('index'))
