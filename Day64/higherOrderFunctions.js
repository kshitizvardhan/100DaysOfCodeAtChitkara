// Higher Order Functions and Passing Functions as Arguments
// Creating a Calculator function and Passing functions as arguments
function add(num1,num2) {
    return num1+num2
}
function subtract(num1,num2) {
    return num1-num2
}
function multiply(num1,num2) {
    return num1*num2
}
function divide(num1,num2) {
    return num1/num2
}
function Calculator(num1, num2, operator) {
    return operator(num1,num2)
}
