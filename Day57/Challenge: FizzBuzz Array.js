/* When the number is divisible by 3 and 5, the array is pushed with "FizzBuzz"
else if the number is divisble by only 3, the array is pushed with "Fizz"
else if the number is divisble by only 5, the array is pushed with "Buzz"
or else the number in the count is pushed if all the above statements are false */


var output=[]
count=1
function fizzBuzz() {
    if (count%3===0 && count%5===0){
        output.push("FizzBuzz")
    } else if (count%3===0){
        output.push("Fizz")
    } else if (count%5===0){
        output.push("Buzz")
    } else{
        output.push(count)
    }
    count++
    console.log(output)
}

// Output
// fizzBuzz();
// (19) [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19]
