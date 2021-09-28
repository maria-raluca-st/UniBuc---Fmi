// Import packages
const express = require("express");
const morgan = require("morgan");
const bodyParser = require("body-parser");
const cors = require("cors");
const uuid = require("uuid");

const fs = require("fs");

// Aplicatia
const app = express();

// Middleware
app.use(morgan("tiny"));
app.use(bodyParser.json());
app.use(cors());



app.use("/", express.static('public_html'));


// Create
app.post("/gifts", (req, res) => {
  const giftsList = readJSONFile();
  const newGift = req.body;
  newGift.id = uuid.v4();
  const newGiftList = [...giftsList, newGift];
  writeJSONFile(newGiftList);
  res.json(newGift);
});

// Read One
app.get("/gifts/:id", (req, res) => {
  const giftsList = readJSONFile();
  const id = req.params.id;
  let idFound = false;
  let foundGift;

  giftsList.forEach(gift => {
    if (id === gift.id) {
      idFound = true;
      foundGift = gift
    }
  });

  if (idFound) {
    res.json(foundGift);
  } else {
    res.status(404).send(`Gift ${id} was not found`);
  }
});

// Read All
app.get("/gifts", (req, res) => {
  const giftsList = readJSONFile();
  res.json(giftsList);
});

// Update
app.put("/gifts/:id", (req, res) => {
  const giftsList = readJSONFile();
  const id = req.params.id;
  const newGift = req.body;
  newGift.id = id;
  idFound = false;

  const newGiftsList = giftsList.map((gift) => {
     if (gift.id === id) {
       idFound = true;
       return newGift
     }
    return gift
  })
  
  writeJSONFile(newGiftsList);

  if (idFound) {
    res.json(newGift);
  } else {
    res.status(404).send(`Gift ${id} was not found`);
  }

});

// Delete
app.delete("/gifts/:id", (req, res) => {
  const giftsList = readJSONFile();
  const id = req.params.id;
  const newGiftsList = giftsList.filter((gift) => gift.id !== id)

  if (giftsList.length !== newGiftsList.length) {
    res.status(200).send(`Gift ${id} was removed`);
    writeJSONFile(newGiftsList);
  } else {
    res.status(404).send(`Gift ${id} was not found`);
  }
});

// Functia de citire din fisierul db.json
function readJSONFile() {
  return JSON.parse(fs.readFileSync("db.json"))["gifts"];
}

// Functia de scriere in fisierul db.json
function writeJSONFile(content) {
  fs.writeFileSync(
    "db.json",
    JSON.stringify({ gifts: content }),
    "utf8",
    err => {
      if (err) {
        console.log(err);
      }
    }
  );
}

// Pornim server-ul
app.listen("3000", () =>
  console.log("Server started at: http://localhost:3000")
);