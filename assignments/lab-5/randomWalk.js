function getRelatedSearches(query) {  // returns a Promise to a list of suggested searches
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
  let requestPromise = fetch(queryurl, myInit);
  // TODO: Implement the rest
  return requestPromise
    .then(response => response.json())
    .then(json => {
      return json.map(r=>r.word)
    })
}

function pickRandomSuggestion(suggestions) {
  let random = Math.floor(Math.random() * suggestions.length);
  let selected = suggestions[random]
  // TODO: Implement the rest
  return selected
}

function walkFive(query) {
  // TODO: Implement the rest
  console.log(query)
  let plannedListOfWords = getRelatedSearches(query)
  let walkPlan = plannedListOfWords.then(list => {
    nextWord = pickRandomSuggestion(list)
    console.log(nextWord)
    return nextWord
  })

  for(let hops = 1; hops < 15; hops++){
    let newPlan = walkPlan.then(word => getRelatedSearches(word))
      .then(list => {
        nextWord = pickRandomSuggestion(list)
        console.log(nextWord)
        return nextWord
      })
    walkPlan = newPlan
  }
}

document.addEventListener("DOMContentLoaded", ()=>{
  document.querySelector("#walkFive").addEventListener("click", ()=>{
    // get the value from input field
    let v = document.querySelector("#walkInput").value
    walkFive(v)
  })
})