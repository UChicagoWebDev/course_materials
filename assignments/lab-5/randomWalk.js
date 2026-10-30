function getRelatedSearches(query) {
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
}

function pickRandomSuggestion(suggestions) {
  let random = Math.floor(Math.random() * suggestions.length);
  let selected = suggestions[random]
  // TODO: Implement the rest
}

function walkFive(query) {
  // TODO: Implement the rest
}