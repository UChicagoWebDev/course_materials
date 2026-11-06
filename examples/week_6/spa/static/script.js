function showHappyAnimal(animal) {
  // Make sure no other animals are best
  document.querySelectorAll(".animal.best").forEach((n) => {
    n.classList.remove("best");
  });
  // Add the 'best' class to the selected animal
  if (animal && animal.length > 0) {
    a = document.querySelector(".animal." + animal);
    a.classList.add("best");
  }
}
function makeBest(animal) {
  showHappyAnimal(animal);
  if (animal.length > 0) {
    document.title = animal + " is best!";
  } else {
    document.title = "SPA: Single Page Application";
  }
    // TODO: push /animal to the URL bar and add this page to the history
    // "127.0.0.1/dog"
    // DOES NOT WORK: location.replace('/'+animal)
    history.pushState(null, null, "/"+animal)
}
function loadAnimal() {
  // TODO: Check the URL bar on load so e.g. /cat makes cat best
}
document.addEventListener("DOMContentLoaded", () => {
  // Register a click handler on each animal instead of using onclick="..."
  // attributes in the HTML.
  ["cat", "dog", "bear"].forEach((animal) => {
    document.querySelector(".animal." + animal).addEventListener("click", () => {
      makeBest(animal);
    });
  });
});
window.addEventListener("load", ()=>{
  console.log("load");
  // TODO
});
addEventListener("popstate", ()=>{
  console.log("popstate"); 
  // TODO
});
