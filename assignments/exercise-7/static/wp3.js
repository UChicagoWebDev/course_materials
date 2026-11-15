function Site() {
    return <React.Fragment>
        <h1>Watch Party 3</h1>
        <h2>Chain Reaction</h2>
    </React.Fragment>
}

const rootContainer = document.getElementById("root");
const root = ReactDOM.createRoot(rootContainer);
root.render(<Site />);