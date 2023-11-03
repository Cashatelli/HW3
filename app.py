from flask import Flask, render_template, jsonify
import psycopg2
from psycopg2 import Error

app = Flask(__name__)

POSTGRES_HOST = '127.0.0.1'
POSTGRES_DB = 'dvdrental'
POSTGRES_USER = 'raywu1990'
POSTGRES_PASSWORD = 'test'

def get_db_connection():
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD
    )
    return conn

@app.route('/api/update_basket_a')
def update_basket_a():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry')")
        conn.commit()
        cur.close()
        conn.close()
        return "Success!"
    except (Exception, Error) as error:
        return str(error), 400

@app.route('/api/unique')
def unique():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT fruit_a FROM basket_a")
        unique_a = cur.fetchall()
        cur.execute("SELECT DISTINCT fruit_b FROM basket_b")
        unique_b = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('unique_fruits.html', basket_a=unique_a, basket_b=unique_b)
    except (Exception, Error) as error:
        return str(error), 400

if __name__ == '__main__':
    app.run(debug=True)
