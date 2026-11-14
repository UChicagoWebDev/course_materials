// import {useState} from 'react'

function Square({value, clickHandler}) {
  // let b = document.createElement("button");
  // b.classList.add("square")
  // b.text = "X"
  // parent.append(b)
  return <button className="square" onClick={clickHandler}>{value}</button>
}

function Board() {
  const [squares, setSquares] = React.useState([null,null,null,
                                                null,null,null,
                                                null,null,null])

  function handleClick(i) {
    let newSquares = squares.slice()
    newSquares[i] = "X"
    setSquares(newSquares)
  }

  return (
    <React.Fragment>
    <div className="board-row">
      <Square value={squares[0]} clickHandler={()=>handleClick(0)} />
      <Square value={squares[1]} clickHandler={()=>handleClick(1)}/>
      <Square value={squares[2]} clickHandler={()=>handleClick(2)}/>
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
