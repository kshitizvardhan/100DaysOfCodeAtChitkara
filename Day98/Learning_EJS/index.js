import express from "express";
import { dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const app= express();
const port=3000;


app.get("/", (req, res) => {
    const Day= new Date();
    const today= Day.getDay();
    let dayType= "a weekday";
    let advice= "it's time to work hard.";
    if (today==0 || today==6){
        dayType= "the weekend";
        advice= "it's time to have some fun.";
    }

    res.render("index.ejs",{
        dayType:dayType,
        advice:advice,
    })    
});

app.listen(port, () => {
    console.log(`Server running on port ${port}.`);
  });


  
