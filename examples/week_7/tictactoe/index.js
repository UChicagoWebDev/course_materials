// import {useState} from 'react'
function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}
function Square({value, handler}) {
  return <button className="square" onClick={handler}>{value}</button>
}
function Board() {
  const emptyBoard = Array(9).fill(null)
  const [history, setHistory] = React.useState([emptyBoard])
  const [currentTurn, setCurrentTurn] = React.useState(0);
  const board = history[currentTurn]
  // const [board, setBoard] = React.useState([null,null,null,
  //                                           null,null,null,
  //                                           null,null,null]);
  // const [xIsNext, setXIsNext] = React.useState(true)
  const xIsNext = currentTurn % 2 == 0
  const winner = calculateWinner(board);
  const nextMove = xIsNext ? "X" : "O"
  const status = winner ? winner + " won the game!" : nextMove + "'s turn!"
  let clickHandler = (i) => {
    if(board[i] || winner) return;
    let newBoard = board.slice()
    newBoard[i] = nextMove
    let newHistory = history.slice(0,currentTurn+1)
    setCurrentTurn(currentTurn+1);
    newHistory.push(newBoard)
    setHistory(newHistory)
  }
  return (
    // let b = document.createElement("button");
    // b.classList.add("square")
    // b.text = "X"
    // parent.append(b)
    <>
    <div>Current turn: {currentTurn}</div>
    <div className="status">{status}</div>
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
    <div className="history">
      <ol>
        {history.map((board, i)=>{
          return(
            <li><button onClick={()=>setCurrentTurn(i)}>{"Move: "+i}</button></li>
          )})}
      </ol>
    </div>
    </>
  );
}
// ========================================
const rootContainer = document.getElementById("root");
const root = ReactDOM.createRoot(rootContainer);
root.render(<Board />);
