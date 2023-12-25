import express from "express";
import bodyParser from "body-parser";

const app = express();
const port = 3000;
let fullName = ""
let len = 0

app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.render("index.ejs")
});

function Name(req,res,next){
  fullName = req.body["fName"] + req.body["lName"];
  len = fullName.length;
  next();
}

app.use(Name);

app.post("/submit", (req, res) => {
  res.render("index.ejs", {
    totalChars: len
  });
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
}); 
