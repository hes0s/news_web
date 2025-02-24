const express = require('express')
const sqlite3 = require('sqlite3')
const cors = require('cors')
const app = express()
const port = 3000


const db = new sqlite3.Database('./database.db', (err) => {
    if (err) {
        console.error('Database connection error:', err.message);
    } else {
        console.log('Connected to the database');
    }
});

db.serialize(() =>{
    db.run(`CREATE TABLE IF NOT EXISTS news(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        newsName VARCHAR(255),
        newsDesription TEXT,
        IMG_URL VARCHAR(255),
        timestapm DATETIME DEFAULT CURENT_TIMESTAMP);`); 
   
    db.run(`INSERT INTO news (newsName, newsDesription, IMG_URL) 
                VALUES ('Test News', 'This is a test description', 'https://via.placeholder.com/150');`);
 })

 app.get("/news", (req, res) => {
    db.all("SELECT * FROM news", [], (err, rows) => {
        if (err) {
            console.error("Database error:", err.message);
            res.status(500).json({ error: err.message });
            return;
        }
        console.log("News Data:", rows); // ✅ Debugging step
        res.json(rows);
    });
});

app.listen(port, () =>{
    console.log("is running")
})