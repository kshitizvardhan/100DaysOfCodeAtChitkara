var numberOfDrumBtn= document.querySelectorAll(".drum").length
for (var i=0; i<numberOfDrumBtn; i++){
    document.querySelectorAll(".drum")[i].addEventListener("click", randomClick)
    function randomClick() {
        alert("I got Clicked")
    }
}

// For every click on button now, a alert will be given.
