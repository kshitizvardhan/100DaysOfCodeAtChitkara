// var a=23
// var a=28
// console.log(a) In var the var can be updated and redeclared and not shown any errors.

let a=23
{
    let a=30
    console.log(a)
}
console.log(a);
// Here the let can only be updated re-declared not possible.

const b=23
{
    // b=29
    // console.log(b);  Error shown, as in const it can neither be updated nor re-declared.
}
console.log(b);
