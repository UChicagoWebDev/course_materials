let fnAButton, fnBButton, fnCButton, sequenceButton = null

const sequence = () => {
    console.log("starting sequence...")
    // TODO
    fnA();
    fnB();
    fnC();

    if (fnAButton.classList.contains("error") ||
        fnBButton.classList.contains("error") ||
        fnCButton.classList.contains("error")) 
    {
        sequenceButton.classList.add("error")
        console.log("sequence error")
    }
}

const fnA = () => {
    const d = 1+4*Math.random()
    console.log(`fnA waiting ${d} seconds`)
    setTimeout(()=>{
        console.log("... fnA done")
        fnAButton.classList.add("ready")
    }, d*1000)
} 

const fnB = () => {
    if(fnAButton.classList.contains("error") || !fnAButton.classList.contains("ready")) {
        fnBButton.classList.add("error")
        return
    }
    const d = 1+4*Math.random()
    console.log(`fnB waiting ${d} seconds`)
    setTimeout(()=>{
        console.log("... fnB done")
        fnBButton.classList.add("ready")
    }, d*1000)
} 

const fnC = () => {
    if(fnBButton.classList.contains("error") || !fnBButton.classList.contains("ready")) {
        fnCButton.classList.add("error")
        return
    }
    const d = 1+4*Math.random()
    console.log(`fnC waiting ${d} seconds`)
    setTimeout(()=>{
        console.log("... fnC done")
        fnCButton.classList.add("ready")
    }, d*1000)
} 

const reset = () => {
    [fnAButton, fnBButton, fnCButton, sequenceButton].forEach(b => {
        b.classList.remove("ready")
        b.classList.remove("error")
    });
}

document.addEventListener("DOMContentLoaded", ()=>{
    fnAButton = document.getElementById("fnAButton")
    fnBButton = document.getElementById("fnBButton")
    fnCButton = document.getElementById("fnCButton")
    
    fnAButton.addEventListener("click",fnA);
    fnBButton.addEventListener("click",fnB);
    fnCButton.addEventListener("click",fnC);

    sequenceButton = document.querySelector("#sequenceButton")

    document.querySelector("#resetButton").addEventListener("click", reset)
    sequenceButton.addEventListener("click",sequence);
})