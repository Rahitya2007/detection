from flask import Flask, render_template, request
import sqlite3
from model import predict_phishing

app = Flask(__name__)


# Create database
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            result TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        url = request.form['url']
        result = predict_phishing(url)

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO urls (url, result) VALUES (?, ?)", (url, result))
        conn.commit()
        conn.close()

    return render_template('index.html', result=result)

@app.route('/history')
def history():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM urls")
    data = c.fetchall()
    conn.close()

    return render_template('history.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
