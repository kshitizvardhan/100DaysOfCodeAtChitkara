/*You are going to write a function which will select a random name from a list of names. 
The person selected will have to pay for everybody's food bill.*/


function whosPaying(names) {
    
    //Write your code here.
    var namesChar= names.length;
    var random= Math.round((Math.random()*namesChar));
    var person= names[random];
    return person+" is going to buy lunch today!";
    

}
