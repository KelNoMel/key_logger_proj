document.addEventListener('DOMContentLoaded', function() {
    // Your event listener setup here
    var element = document.getElementById("playSound");
    if (element) {
        element.addEventListener("click", function() {
            var audio = new Audio("easy.mp3");
            audio.play();
        });
    }
});