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

function makeBest(animal, pushHistory = true) {
  showHappyAnimal(animal);

  if (animal.length > 0) {
    document.title = animal + " is best!";
  } else {
    document.title = "SPA: Single Page Application";
  }

  if (pushHistory) {
    window.history.pushState(
      { animal: animal },
      `${animal} is best!`,
      `/${animal}`
    );
    // TODO: push /animal to the URL bar and add this page to the history
    // DOES NOT WORK: location.replace('/'+animal)
  }
}

function loadAnimal(pushHistory = true) {
  // TODO: Check the URL bar on load so e.g. /cat makes cat best
  path = window.location.pathname; // "/bear"
  animal = path.substring(1); // "bear"

  console.log("Making best animal: " + animal);
  makeBest(animal, pushHistory);
}

window.addEventListener("load", loadAnimal);
window.addEventListener("popstate", (newState) => {
  console.log(newState);
  loadAnimal(false);
});
