const express = require("express");
const multer = require("multer");
const { exec } = require("child_process");
const path = require("path");

const app = express();
const upload = multer({ dest: "uploads/" });

app.use(express.static("public"));

app.post("/upload", upload.single("log"), (req, res) => {
  const filePath = req.file.path;

  exec(`python parser.py ${filePath}`, (err, stdout, stderr) => {
    if (err) {
      return res.status(500).send("Error processing file");
    }
    res.json(JSON.parse(stdout));
  });
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
