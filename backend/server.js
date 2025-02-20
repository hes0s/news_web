import express from 'express';
import mysql from 'mysql';
import cors from 'cors';
import dotenv from 'dotenv';
//set up express
dotenv.config();
const app = express();
app.use (cors());
app.use(express.json());

const db = mysql.createConnection({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASS,
    database: process.env.DB_NAME,
  });

db.connect((err) => {
    if(err){
        console.log(err);
    }
    console.log('Database connected!');
});

app.get('/', (req, res) => {
    res.send('its alive');
});

app.get('/news', (req, res) => {
    db.query("SELECT * FROM news", (err, result) => {
        if(err) return console.status(500).json({err});
        res.json(result);
    });
});

app.listen(5000, () => console.log("Server running on port 5000"));