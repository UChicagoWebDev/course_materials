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

function Square({value, clickHandler}) {
  // let b = document.createElement("button");
  // b.classList.add("square")
  // b.text = "X"
  // parent.append(b)
  return <button className="square" onClick={clickHandler}>{value}</button>
}

function Board() {
  const [xIsNext, setXIsNext] = React.useState(true)
  const [squares, setSquares] = React.useState([null,null,null,
                                                null,null,null,
                                                null,null,null])

  const winner = calculateWinner(squares)

  function handleClick(i) {
    if(squares[i] || winner) {return}

    let newSquares = squares.slice()
    newSquares[i] = xIsNext ? "X" : "O"
    setSquares(newSquares)
    setXIsNext(!xIsNext)
  }

  return (
    <React.Fragment>
    <div>
      {winner && <div>{winner} has won the game!</div>}
      {!winner && <div>Next move: {xIsNext ? "X" : "O"}</div>}
    </div>
    <div className="board-row">
      {[0,1,2].map((i)=><Square key={i} value={squares[i]} clickHandler={()=>handleClick(i)} />)}
    </div>
    <div className="board-row">
      <Square value={squares[3]} clickHandler={()=>handleClick(3)}/>
      <Square value={squares[4]} clickHandler={()=>handleClick(4)}/>
      <Square value={squares[5]} clickHandler={()=>handleClick(5)}/>
    </div>
    <div className="board-row">
      <Square value={squares[6]} clickHandler={()=>handleClick(6)}/>
      <Square value={squares[7]} clickHandler={()=>handleClick(7)}/>
      <Square value={squares[8]} clickHandler={()=>handleClick(8)}/>
    </div>
    </React.Fragment>
  );
}
// ========================================
const rootContainer = document.getElementById("root");
const root = ReactDOM.createRoot(rootContainer);
root.render(<Board />);
