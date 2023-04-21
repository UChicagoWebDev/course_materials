const bing_api_endpoint = "https://api.bing.microsoft.com/v7.0/images/search";
const bing_api_key = BING_API_KEY;

function oneStep(query) {
  // go again from here
  let queryurl = bing_api_endpoint + "?q=" + encodeURIComponent(query);
  // request.setRequestHeader("Ocp-Apim-Subscription-Key", bing_api_key);

  let walkHeaders = new Headers();
  walkHeaders.append("Ocp-Apim-Subscription-Key", BING_API_KEY);
  walkHeaders.append("Accept", "application/json");
  walkHeaders.append("Content-Type", "application/json");

  const myInit = {
    method: "GET",
    headers: walkHeaders,
  };

  let nextQuery = fetch(queryurl, myInit);
  // TODO: .then(
}

function walkFive() {
  oneStep();
  // TODO: Four more steps
}
