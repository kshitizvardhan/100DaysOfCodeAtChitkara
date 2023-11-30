// var generateName= require('sillyname')  // Common Js

import generateName from "sillyname";   // EcmaScript (ESM)
var sillyname=generateName()

console.log(`My name is ${sillyname}.`)

import superheroes from "superheroes";
var name= superheroes.random()

console.log(`I am ${name}.`)
