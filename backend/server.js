const express = require("express");
const cors = require("cors");
const fs = require("fs");
const cp = require("child_process");

const app = express();

app.use(cors());
app.use(express.json());

app.post("/classify", async (req, res) => {
  const { frame, limit } = req.body;

  await fs.writeFile("../python/sample.json", JSON.stringify(frame), (err) => {
    if (err) console.log(err);
    res.status(503);
    return;
  });

  console.log("Spawning python main.py process");
  const classify = cp.spawn("python", ["../python/main.py", limit || 50]);

  classify.stdout.on("data", (data) => {
    console.log(data.toString());
    const line = data.toString().trim();
    res.status(201).json({ digit: line });
    return;
  });

  classify.stderr.on("data", (data) => {
    console.log("ERROR:", data.toString());
  });

  classify.on("close", (code) => {
    console.log(`Process exit with code ${code}`);
  });

  res.status(503);
});

app.listen(3000, () => console.log("Express.js listening at port 3000"));
