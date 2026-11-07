let makeNobodyBest = () => {
    document.querySelectorAll(".animal").forEach(a => {
        a.classList.remove("best")
    })
}


let showBestAnimal = () => {
    makeNobodyBest();
    let path = window.location.pathname
    if(path.startsWith("/spa/")) {
        let animal = path.slice(5)
        a = document.querySelector(".animal."+animal)
        a.classList.add("best")
    }
}

document.addEventListener("DOMContentLoaded", ()=>{
    animals = document.querySelectorAll(".animal")
    animals.forEach(a => {
        a.addEventListener("click", (e)=>{
            let animal = a.dataset.animal
            history.pushState(null, null, "/spa/"+animal)
            showBestAnimal()
            e.preventDefault();
        });
    })

    showBestAnimal()
});

window.addEventListener("popstate", () => {
    showBestAnimal()
})