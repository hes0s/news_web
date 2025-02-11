import pymysql

# Establish a connection
conn = pymysql.connect(
    host="sql311.infinityfree.com",
    user="if0_38291971",
    password="G2EqQzOrvL0xd",
    database="if0_38291971_wweb_news_site"
)

cursor = conn.cursor()
for table in cursor:
    print(table)


