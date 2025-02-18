require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

// Connect to MongoDB Atlas
mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const db = mongoose.connection;
db.once("open", () => console.log("Connected to MongoDB"));

// Define Schema
const newsSchema = new mongoose.Schema({
  name: String,
  description: String,
  photo: String, // URL of the photo
});

const Photo = mongoose.model("news_info", newsSchema);

// API to Get All Photos
app.get("/news", async (req, res) => {
  const photos = await Photo.find({}, "name description photo");
  res.json(photos);
});
// Start Server
const PORT = 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
