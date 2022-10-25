let toggled1 = false;
console.log(toggled1)

function toggleDarkMode() {
  if (toggled1) {
    var element = document.getElementById("hidden");
    element.style.opacity = 0;
    toggled1 = false;
  } else {
    var element = document.getElementById("hidden");
    element.style.opacity = 1;
    toggled1 = true;
  }
}