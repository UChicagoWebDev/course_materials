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
    history.pushState(null, null, animal);
}

function loadAnimal() {
  animal = "";

  let path = window.location.pathname;
  let parsed = path.split("/")[1];
  if (parsed.length > 1) {
    animal = parsed;
  }

  // TODO: Check the URL bar on load so e.g. /cat makes cat best
  console.log("Making best animal: " + animal);
  showHappyAnimal(animal);
}

window.addEventListener("load", ()=>{
  console.log("load");
  loadAnimal();
});
addEventListener("popstate", ()=>{
  console.log("popstate"); 
  loadAnimal();
});

