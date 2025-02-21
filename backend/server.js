import express from "express";
import cors from "cors";

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

app.get("/", (req, res) => {
  res.send("Server is running and CORS is fixed!");
});

app.get("/favivon.ico", (req, res) => {
  res.send("favicon.ico");
});

app.get("/news", (req, res) => {
  res.json([{ id: 1, title: "News Title", description: "Example news item" }]);
});

const PORT = process.env.PORT || 5001;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));