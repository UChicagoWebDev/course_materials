// import {useState} from 'react'


function Board() {
  const emptyBoard = Array(9).fill(null)


  return (
    // let b = document.createElement("button");
    // b.classList.add("square")
    // b.text = "X"
    // parent.append(b)
    <>
    <div className="board-row">
      <Square value={board[0]} handler={()=>clickHandler(0)}/>
      <Square value={board[1]} handler={()=>clickHandler(1)}/>
      <Square value={board[2]} handler={()=>clickHandler(2)}/>
    </div>
    <div className="board-row">
      <Square value={board[3]} handler={()=>clickHandler(3)}/>
      <Square value={board[4]} handler={()=>clickHandler(4)}/>
      <Square value={board[5]} handler={()=>clickHandler(5)}/>
    </div>
    <div className="board-row">
      <Square value={board[6]} handler={()=>clickHandler(6)}/>
      <Square value={board[7]} handler={()=>clickHandler(7)}/>
      <Square value={board[8]} handler={()=>clickHandler(8)}/>
    </div>
    </>
  );
}
// ========================================
const rootContainer = document.getElementById("root");
const root = ReactDOM.createRoot(rootContainer);
root.render(<Board />);
