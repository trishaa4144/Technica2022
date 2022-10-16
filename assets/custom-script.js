function fade() {
  var fades = document.querySelectorAll(".fade")
  for (var i = 0; i < fades.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = fade[i].getBoundingClientRect().top;
    var elementVisible = 150;
    if (elementTop < windowHeight - elementVisible) {
      fade[i].classList.add("active");
    } else {
      fade[i].classList.remove("active");
    }
  }
}

window.addEventListener("scroll", fade);




