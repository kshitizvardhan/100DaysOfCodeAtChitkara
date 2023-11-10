var name= prompt("What is your Name");
var chars= name.length;
var firstLetter= name.slice(0,1).toUpperCase();
var remaining= name.slice(1,chars).toLowerCase();
var message= "Hello "+ firstLetter + remaining;
alert(message)
