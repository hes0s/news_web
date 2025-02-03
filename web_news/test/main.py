from flask import Flask, render_template
import pymysql

app = Flask(__name__)
# Connect database 
conn = pymysql.connect(host="localhost", user="root", password="root", database="news")
cursor = conn.cursor()

@app.route("/")
def home():
    cursor.execute("SELECT Name, Description, img_url FROM news_info")
    news = cursor.fetchall()
    return render_template("index.html", news=news)


if __name__ == "__main__":
    app.run(debug=True)
