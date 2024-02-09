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
    // DOES NOT WORK: location.replace('/'+animal)
}

function loadAnimal() {
  animal = "";

  // TODO: Check the URL bar on load so e.g. /cat makes cat best
  console.log("Making best animal: " + animal);
  makeBest(animal);
}

