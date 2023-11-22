var numberOfDrumBtn= document.querySelectorAll(".drum").length;
for (var i=0; i<numberOfDrumBtn; i++){
    document.querySelectorAll(".drum")[i].addEventListener("click", randomClick);
    function randomClick() {
        var audio= new Audio("sounds/tom-1.mp3"); // Javascript Objects
        audio.play()
    }
}
// On every click sound is played.
