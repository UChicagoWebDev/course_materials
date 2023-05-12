import MyModule from "/static/module.js"

class ModuleDemo extends React.Component {
  render() {
    return (
      <div className="ModuleDemo">
        I'm going to try to include a module:
        <MyModule />
      </div>
    );
  }
}

// ========================================

ReactDOM.render(
  React.createElement(ModuleDemo),
  document.getElementById('root')
);
