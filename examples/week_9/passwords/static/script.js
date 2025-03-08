class SignupAndLogin extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  signup = () => {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    fetch("/api/signup", {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({username: username, password: password})
    }).then((response) => {
      if(response.status == 200) {
        alert("Created user "+username);
      } else {
        alert("A user "+username+" already exists");
      }
    });
  }
  login = () => {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    fetch("/api/login", {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({username: username, password: password})
    }).then((response) => {
      if(response.status == 200) {
        alert("Logged in as "+username);
      } else {
        alert("Incorrect username and password");
      }
    });
  }
  render() {
    return (
      <div className="signup">
        <h1>Signup and Login</h1>
        <div className="signup_form">
          <label htmlFor="username">Username</label>
          <input id="username"></input>
          <label htmlFor="password">Password</label>
          <input id="password" type="password"></input>
          <button className="form_button" onClick={this.signup}>
            Signup
          </button>
          <button className="form_button" onClick={this.login}>
            Login
          </button>
        </div>
      </div>
    );
  }
}

// ========================================

ReactDOM.render(
  React.createElement(SignupAndLogin),
  document.getElementById('root')
);
