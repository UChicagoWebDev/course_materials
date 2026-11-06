async function getRelatedSearchesWithAsync(query) {
  if(!query) return;
  const api_endpoint = "https://api.datamuse.com/words";
  let queryurl = api_endpoint + "?ml=" + encodeURIComponent(query);
  let walkHeaders = new Headers();
  walkHeaders.append("Accept", "application/json");
  walkHeaders.append("Content-Type", "application/json");
  const myInit = {
    method: "GET",
    headers: walkHeaders,
  };
  let response = await fetch(queryurl, myInit)
  data = await response.json()
  return data.map(r=>r.word)
}

function pickRandomSuggestionWithAsync(suggestions) {
  let random = Math.floor(Math.random() * suggestions.length);
  let selected = suggestions[random];
  // TODO
  return selected
}

async function walkFiveWithAsync(query) {

  for(let i=0; i<15; i++) {
  suggestions = await getRelatedSearchesWithAsync(query)
  nextWord = pickRandomSuggestionWithAsync(suggestions)
  console.log(nextWord)
  query = nextWord
  }
}

document.addEventListener("DOMContentLoaded", ()=>{
  document.querySelector("#walkFiveAsync").addEventListener("click", ()=>{
    // get the value from input field
    let v = document.querySelector("#walkInput").value
    walkFiveWithAsync(v)
  })
})