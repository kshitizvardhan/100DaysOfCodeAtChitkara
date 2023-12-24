
import express from "express";
import bodyParser from "body-parser";
import { dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const app= express();
const port= 3000;
var pwd=""

app.get("/", (req, res) => {
    res.sendFile(__dirname + "/public/index.html");
});

app.use(bodyParser.urlencoded({extended: true}))

app.post("/check",(req,res) =>{
    console.log(req.body)
    pwd= req.body["password"]
    if (pwd=="ILoveProgramming"){ 
        res.sendFile(__dirname + "/public/secret.html")
    }
    else{
        res.redirect("/");
    }
})

app.listen(port,() => {
    console.log(`Server running on Port ${port}`);
})

