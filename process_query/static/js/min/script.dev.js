"use strict";

// Source: https://www.w3schools.com/js/tryit.asp?filename=tryjs_validation_number
function myFunction() {
  var x, text; // Get the value of the input field with id="numb"

  x = document.getElementById("q").value; // If x is Not a Number or less than one or greater than 10

  if (isNaN(x) || x < 1 || x > 10) {
    text = "Please enter a search term";
  } else {
    text = None;
  }

  document.getElementById("alert").innerHTML = text;
}