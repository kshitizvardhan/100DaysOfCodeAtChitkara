var randomNumber1= Math.floor((Math.random()*6)+1);
var randomImage1= "images/dice"+randomNumber1+".png"
var images1= document.querySelectorAll("img")[0].setAttribute("src" , randomImage1);

var randomNumber2= Math.floor((Math.random()*6)+1);
var randomImage2= "images/dice"+randomNumber2+".png"
var images2= document.querySelectorAll("img")[1].setAttribute("src" , randomImage2);

if (randomNumber1===randomNumber2){
    document.querySelector("h1").innerHTML="<em>DRAW !!</em>"
}
else if (randomNumber1>randomNumber2){
    document.querySelector("h1").innerHTML="<em> Player 1 Wins!! </em>"
}
else{
    document.querySelector("h1").innerHTML="<em> Player 2 Wins!! </em>"
}



