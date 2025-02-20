import express from 'express';
import mysql from 'mysql';
import cors from 'cors';
import dotenv from 'dotenv';
//set up express
dotenv.config();
const app = express();

app.use(cors({
    origin: "https://rainbow-cuchufli-46a42d.netlify.app",
    methods: "GET,POST,PUT,DELETE,OPTIONS",
    allowedHeaders: "Content-Type, Authorization",
    credentials: true
  }));

app.use((req, res, next) => {
    res.header("Access-Control-Allow-Origin", "https://rainbow-cuchufli-46a42d.netlify.app");
    res.header("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE,OPTIONS");
    res.header("Access-Control-Allow-Headers", "Content-Type, Authorization");
    res.header("Access-Control-Allow-Credentials", "true");
    next();
  });
  

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