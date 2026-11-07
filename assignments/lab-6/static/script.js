document.addEventListener("DOMContentLoaded", ()=>{
    animals = document.querySelectorAll(".animal")
    animals.forEach(a => {
        a.addEventListener("click", (e)=>{
            let animal = a.dataset.animal
            animals.forEach(otherAnimal => {
                otherAnimal.classList.remove("best")
            })
            a.classList.add("best")
            e.preventDefault();
        });
    })
});