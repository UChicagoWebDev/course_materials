async function getRelatedSearchesWithAsync(query) {
  if(!query) return;
  const bing_api_endpoint = "https://api.bing.microsoft.com/v7.0/images/search";
  const bing_api_key = BING_API_KEY;
  let queryurl = bing_api_endpoint + "?q=" + encodeURIComponent(query);
  let walkHeaders = new Headers();
  walkHeaders.append("Ocp-Apim-Subscription-Key", BING_API_KEY);
  walkHeaders.append("Accept", "application/json");
  walkHeaders.append("Content-Type", "application/json");
  const myInit = {
    method: "GET",
    headers: walkHeaders,
  };
  let response = await fetch(queryurl, myInit);
  // TODO: Implement the rest
}
function pickRandomSuggestionWithAsync(suggestions) {
  let random = Math.floor(Math.random() * suggestions.length);
  let selected = suggestions[random].text;
  // console.log(next);
  return selected;
}
async function walkFiveWithAsync(query) {
  
}
