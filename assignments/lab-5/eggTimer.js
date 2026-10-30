let timerId = 0;

let setEggTimer = (id, x) => {
    let t = document.createElement("button")
    let label = document.createTextNode(id)
    t.appendChild(label)
    document.querySelector("#timerContainer").appendChild(t)
    // TODO: wait for X seconds, then log "Ding!" and add the "ready" class to t
}

document.addEventListener("DOMContentLoaded", ()=>{
    let timerButton = document.querySelector("#timerButton")
    timerButton.addEventListener("click", ()=>{
        // get X
        let timerInput = document.getElementById("delayInput")
        // TODO: set the egg timer
        setEggTimer(timerId, timerInput.value)
    })
})

