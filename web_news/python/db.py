import pymysql

# Establish a connection
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="news"
)

cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        telegram_id BIGINT UNIQUE NOT NULL,
        username VARCHAR(255)
    )
""")
for table in cursor:
    print(table)


