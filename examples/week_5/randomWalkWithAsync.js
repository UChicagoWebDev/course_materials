const bing_api_endpoint = "https://api.bing.microsoft.com/v7.0/images/search";
const bing_api_key = BING_API_KEY;

function getRelatedSearchesWithAsync(query) {
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

  let suggestionsPromise = p.then((result) => {
      return result.json();
  })
  .then((data) => {
    let related = data.relatedSearches;
    console.log(related);
    return related;
  });

  return suggestionsPromise;
}

function pickRandomSuggestionWithAsync(suggestions) {
  let random = Math.floor(Math.random() * suggestions.length);
  let selected = related[random].text;
  // console.log(next);
  return selected;
}


function walkFiveWithAsync() {
  let query = document.querySelector("#input").value;
  let suggestionsPromise = getRelatedSearchesWithAsync(query);
  suggestionsPromise.then((suggestions => {
    let selected = pickRandomSuggestionWithAsync(suggestions);
    console.log(selected);
  }))
  // TODO: Do it four more times
}
