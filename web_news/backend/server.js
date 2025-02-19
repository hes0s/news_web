require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

// 🌐 Connect to MongoDB Atlas
mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const db = mongoose.connection;
db.on("error", console.error.bind(console, "MongoDB connection error:"));
db.once("open", () => console.log("✅ Connected to MongoDB"));

// 📌 Define Schema and Model
const newsSchema = new mongoose.Schema({
  name: String,
  description: String,
  photo: String, // Image URL
});

const News = mongoose.model("News", newsSchema);

// 📌 API Route to Get All News
app.get("/news", async (req, res) => {
  try {
    const news = await News.find();
    res.json(news);
  } catch (error) {
    res.status(500).json({ message: "Error fetching news", error });
  }
});

// 📌 API Route to Add News (Optional)
app.post("/news", async (req, res) => {
  try {
    const newNews = new News(req.body);
    await newNews.save();
    res.status(201).json(newNews);
  } catch (error) {
    res.status(500).json({ message: "Error adding news", error });
  }
});

// 🏠 Root Route (To Avoid "Cannot GET /" Error)
app.get("/", (req, res) => {
  res.send("Welcome to News API! Use /news to fetch news.");
});

// 🚀 Start Server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`✅ Server running on port ${PORT}`));