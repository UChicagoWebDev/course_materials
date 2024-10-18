const bing_api_endpoint = "https://api.bing.microsoft.com/v7.0/images/search";
const bing_api_key = BING_API_KEY;
function getRelatedSearches(query) {
  let queryurl = bing_api_endpoint + "?q=" + encodeURIComponent(query);
  let walkHeaders = new Headers();
  walkHeaders.append("Ocp-Apim-Subscription-Key", BING_API_KEY);
  walkHeaders.append("Accept", "application/json");
  walkHeaders.append("Content-Type", "application/json");
  const myInit = {
    method: "GET",
    headers: walkHeaders,
  };
  let requestPromise = fetch(queryurl, myInit);
  let suggestionsPromise = requestPromise.then((result) => {
      return result.json();
  })
  .then((data) => {
    let related = data.relatedSearches;
    console.log(related);
    return related;
  });
  return suggestionsPromise;
}
function pickRandomSuggestion(suggestions) {
  let random = Math.floor(Math.random() * suggestions.length);
  let selected = suggestions[random].text;
  // console.log(next);
  return selected;
}

function walkFive() {
  let query = document.querySelector("#input").value;
  let suggestionsPromise = getRelatedSearches(query);
  suggestionsPromise.then((suggestions => {
    let selected = pickRandomSuggestion(suggestions);
    console.log(selected);
    return selected;
  }))
  .then((suggestion)=> {
    return getRelatedSearches(suggestion);
  })
  .then((relatedSearches)=> {
    let selected = pickRandomSuggestion(relatedSearches);
    console.log(selected);
    return selected;
  })
  .then((suggestion)=> {
    return getRelatedSearches(suggestion);
  })
  .then((relatedSearches)=> {
    let selected = pickRandomSuggestion(relatedSearches);
    console.log(selected);
    return selected;
  })
  .then((suggestion)=> {
    return getRelatedSearches(suggestion);
  })
  .then((relatedSearches)=> {
    let selected = pickRandomSuggestion(relatedSearches);
    console.log(selected);
    return selected;
  })
  .then((suggestion)=> {
    return getRelatedSearches(suggestion);
  })
  .then((relatedSearches)=> {
    let selected = pickRandomSuggestion(relatedSearches);
    console.log(selected);
    return selected;
  })
  // TODO: Do it four more times
}
