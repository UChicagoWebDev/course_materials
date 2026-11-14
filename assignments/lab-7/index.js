// import {useState} from 'react'

function Square() {
  // let b = document.createElement("button");
  // b.classList.add("square")
  // b.text = "X"
  // parent.append(b)
  return <button className="square"></button>
}

function Board() {
  return (
    <React.Fragment>
    <div className="board-row">
      <Square />
      <Square />
      <Square />
    </div>
    <div className="board-row">
      <Square />
      <Square />
      <Square />
    </div>
    <div className="board-row">
      <Square />
      <Square />
      <Square />
    </div>
    </React.Fragment>
  );
}
// ========================================
const rootContainer = document.getElementById("root");
const root = ReactDOM.createRoot(rootContainer);
root.render(<Board />);
