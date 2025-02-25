const express = require("express");
const cors = require("cors"); // ✅ Import CORS
const sqlite3 = require("sqlite3").verbose();

const app = express();
app.use(cors()); // ✅ Allow frontend requests
app.use(express.json()); // ✅ Parse JSON

const db = new sqlite3.Database("./database.db", (err) => {
  if (err) {
    console.error(err.message);
  }
  console.log("Connected to the database");
});

app.get("/news", (req, res) => {
    db.all("SELECT id, newsName, newsDesription, IMG_URL FROM news", [], (err, rows) => {
      if (err) {
        console.error("Database error:", err.message);
        res.status(500).json({ error: "Database query failed" });
        return;
      }
      res.json(rows);
    });
});

app.listen(3000, () => console.log("Server running on port 3000"));