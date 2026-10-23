const pixabay_api_endpoint = "https://pixabay.com/api/";
const pixabay_api_key = "fake" //PIXABAY_API_KEY
function runSearch() {

  // TODO: Clear the results pane before you run a new search
  openResultsPane();

  // TODO: Delete this line
  addFakeResults();

  // TODO: Build your queries, following the documentation for your chosen endpoints
  let request = new XMLHttpRequest();

  // TODO: Construct the request object and add appropriate event listeners to
  // handle responses. 
  //   - You'll want to specify that you want json as your response type
  //   - Look for your data in event.target.response
  //   - When you get your responses, add elements to the DOM in #resultsImageContainer to
  //     display them to the user
  //   - HINT: Add event listeners to them *after* you add them to the DOM

  // TODO: Send the request

  // TODO: Depending on what API(s) you use, you may need to send a second request to get suggested searches

  return false;  // Keep this; it keeps the browser from sending the event
                  // further up the DOM chain. Here, we don't want to trigger
                  // the default form submission behavior.
}
function openResultsPane() {
  // This will make the results pane visible.
  document.querySelector("#resultsExpander").classList.add("open");
}
function closeResultsPane() {
  // This will make the results pane hidden again.
  document.querySelector("#resultsExpander").classList.remove("open");
}

// You can leave this function in place, just remove the call to it above when you implement adding your *real* results.
function addFakeResults() {
  const c = document.getElementById("resultsImageContainer");
  c.replaceChildren();
  window.setTimeout(()=> {
    const fakeResults = [...document.getElementById("fakeResults").children];
    fakeResults.forEach((r) => {
      const newResult = r.cloneNode(true);
      newResult.addEventListener("click", ()=>{alert("Implement me!")});
      c.appendChild(newResult);
    })
  }, 500);
}

// This will make clicking the search button or hitting enter from the search bar run a search
document.querySelector("#runSearchButton").addEventListener("click", runSearch);
document.querySelector(".search input").addEventListener("keypress", (e) => {
  if (e.key == "Enter") {runSearch()}
});

// This will make clicking the results close button or hitting escape close the results pane
document.querySelector("#closeResultsButton").addEventListener("click", closeResultsPane);
document.querySelector("body").addEventListener("keydown", (e) => {
  if(e.key == "Escape") {closeResultsPane()}
});
