function getRelatedSearches(query) {
  if(!query) return;
  const bing_api_endpoint = "https://api.bing.microsoft.com/v7.0/images/search";
  const bing_api_key = BING_API_KEY;
  let queryurl = bing_api_endpoint + "?q=" + encodeURIComponent(query);
  let walkHeaders = new Headers();
  walkHeaders.append("Ocp-Apim-Subscription-Key", bing_api_key);
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

function walkFive(query) {
  // suggestionsPromise points to our related searches result
  let suggestionsPromise = getRelatedSearches(query);
  
  randomResultPromise = suggestionsPromise.then((related) => {
    let r = pickRandomSuggestion(related);
    addRelated(r);
    return r;
  });
  // TODO: Implement the rest
}