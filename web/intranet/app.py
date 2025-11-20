import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, render_template, request


app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        host='db',
        port=5432,
        database='intranet',
        user='postgres',
        password='dbpassword',
        cursor_factory=RealDictCursor
    )


@app.route('/', methods=['GET', 'POST'])
def intranet():
    q = ''
    results = []

    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        q = request.form.get('search', '').strip()
        cur.execute(f"SELECT * FROM employees WHERE name ILIKE '%{q}%' OR department ILIKE '%{q}%' ORDER BY id;")
    else:
        cur.execute('SELECT * FROM employees ORDER BY id;')

    results = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('index.html', results=results, search_query=q)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
