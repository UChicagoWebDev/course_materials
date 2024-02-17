function Square() {
  return (
    <button className="square">X</button>
  );
}

// ========================================

const rootContainer = document.getElementById("root");
const root = ReactDOM.createRoot(rootContainer);
root.render(<Square />);
