// import {useState} from 'react'

function Square() {
  return <button className="square"></button>
}
function Board() {
  return (
    // let b = document.createElement("button");
    // b.classList.add("square")
    // b.text = "X"
    // parent.append(b)
    <>
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
    </>
  );
}
// ========================================
const rootContainer = document.getElementById("root");
const root = ReactDOM.createRoot(rootContainer);
root.render(<Board />);
