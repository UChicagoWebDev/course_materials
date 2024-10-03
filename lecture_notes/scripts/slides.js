requirejs(["remark-v0.15.0.min"], () => {
    const indexContainer = document.querySelector("#indexContainer");
    const urlParams = new URLSearchParams(window.location.search);
    const week = parseInt(urlParams.get('week'),10); 

    if(isNaN(week) || week < 1 || week > 9) {
        indexContainer.setAttribute("style", "display: block");
        document.querySelectorAll(".slideButtons .selected")
            .forEach(e => e.classList.remove("selected"));
        document.querySelector(".slideButtons li:first-child").classList.add("selected");
        return;
    } // else: week is an integer >= 1 and <= 9 
       
    const notesFile = "week_" + week + ".md";

    document.querySelectorAll(".slideButtons .selected")
        .forEach(e => e.classList.remove("selected"));
    document.querySelector(`.slideButtons li:nth-child(${week+1})`).classList.add("selected");
    indexContainer.setAttribute("style", "display: none");

    let source = document.getElementById("source");
    while (source && source.firstChild) {
        source.removeChild(source.firstChild);
    }
    remark.create({ sourceUrl: notesFile });
});

