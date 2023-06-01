import express from "express";
import cors from "cors";
import fs from "fs";

const app = express();

app.use(cors());
app.use(express.json());

app.post("/classify", async (req, res) => {
  const { frame, limit } = req.body;

  await fs.writeFile("/shared/sample.json", JSON.stringify(frame), (err) => {
    if (err) console.log(err);
    res.status(503);
    return;
  });

  const args = new URLSearchParams({ limit });

  const pyResponse = await fetch(`http://python/classify?${args.toString()}`);

  if (pyResponse.ok) {
    const data = await pyResponse.json();
    res.status(200).json(data);
  } else {
    res.status(503);
  }
});

app.listen(80, () => console.log("Express.js listening at port 80"));
