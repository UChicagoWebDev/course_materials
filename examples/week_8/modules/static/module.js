import MyChildDependency from "/static/childDependency.js"

class MyModule extends React.Component {
  render() {
    return (<MyChildDependency />);
  }
}

export default MyModule;
