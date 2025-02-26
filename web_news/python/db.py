import sqlite3

conn = sqlite3.connect('/Users/cusnircristian/Desktop/news_web/web_news/server/database.db')
if conn==True:
    print("Connected")

cursor = conn.cursor()


