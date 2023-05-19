class SignupAndLogin extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  signup = () => {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch("http://127.0.0.1:5000/api/signup", {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({username: username, password: password})
    }).then((response) => {
      if(response.status == 200) {
        alert("Created user "+username);
      } else if (response.status == 302){
        alert("A user "+username+" already exists");
      } else {
        response.json().then((json) => alert(json));
      }
    });
  }

  login = () => {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch("http://127.0.0.1:5000/api/login", {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({username: username, password: password})
    }).then((response) => {
      if(response.status == 200) {
        alert("Logged in as "+username);
      } else if (response.status == 404){
        alert("Incorrect username and password");
      } else {
        response.json().then((json) => alert(json));
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
