class Login extends React.Component {
  // constructor(props) {
  //   super(props);
  //   this.state = {
  //     display: true,
  //   }
  // }

  login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    //this.setState({display: false});

    fetch("http://127.0.0.1:5000/api/login", {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({username: username, password: password})
    }).then((response) => {
      if(response.status == 200) {
        response.json().then((data) => {
          window.localStorage.setItem("journal_session_token", data.session_token);
          // document.getElementById("compose").setAttribute('style', 'display: block;');
          // document.getElementById("posts").setAttribute('style', 'display: block;');
          this.props.loginHandler();
        });

      } else {
        console.log(response.status);
        this.logout();
      }
    }).catch((response) =>{
      console.log(response);
      this.logout();
    })
  }

  logout() {
    window.localStorage.removeItem("journal_session_token");
    // this.setState({display: true});
    this.props.logoutHandler();
    // document.getElementById("compose").setAttribute('style', 'display: none;');
    // document.getElementById("posts").setAttribute('style', 'display: none;');
  }

  render() {
    if(!this.props.loggedIn) {
      return (
        <div>
          <h2>Login</h2>
          <div className="login_form">
            <label htmlFor="username">Username</label>
            <input id="username"></input>
            <label htmlFor="password">Password</label>
            <input id="password" type="password"></input>
            <button className="form_button" onClick={() => this.login()}>
              Submit
            </button>
          </div>
        </div>
      );
    }
    else {
      return (
        <div className="logout_button">
          <button onClick={() => {this.logout()}}>
            Logout
          </button>
        </div>
      );
    }
  }
}

class Compose extends React.Component {
  post() {
    const title = document.getElementById("compose_title").value;
    const body = document.getElementById("compose_body").value;
    const session_token = window.localStorage.getItem("journal_session_token");

    fetch("http://127.0.0.1:5000/api/post", {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        session_token: session_token,
        title: title,
        body: body
      })
    }).then(() => {
      document.getElementById("compose_title").value = "";
      document.getElementById("compose_body").value = "";
    });
  }

  render() {
    return (
      <div className="compose" id="compose">
        <h2>Compose</h2>
        <div className="post_form">
          <label htmlFor="compose_title">Title</label>
          <input id="compose_title"></input>
          <label htmlFor="compose_body">Post</label>
          <textarea id="compose_body"></textarea>
          <button className="form_button" onClick={() => this.post()}>
            Post
          </button>
        </div>
      </div>
    );
  }
}

class Posts extends React.Component {
  // constructor(props) {
  //   super(props);
  //   this.state = {
  //     posts: [],
  //   }
  // }

  refresh(){
    const session_token = window.localStorage.getItem("journal_session_token");
    fetch("http://127.0.0.1:5000/api/post", {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({session_token: session_token})
    })
    .then((response) => response.json())
    .then((data) => {
      // this.setState({posts: data});
    });
  }

  render() {
    const posts = this.props.posts.map((post) =>
      <div key={post.id} id={"post_" + post.id}>
        <h3>{post.title}</h3>
        <div>{post.body}</div>
      </div>
    );

    return (
      <div className="posts" id="posts">
        <h2>Posts</h2>
        <button onClick={() => this.refresh()}>Refresh</button>
        {posts}
      </div>
    );
  }
}

Posts.propTypes = {
  posts: window.PropTypes.array
}

class Journal extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isLoggedIn: false,
      posts: [
        {id: 1, title: "ONE", body: "I am first!"},
        {id: 2, title: "2", body: "Better than the original!"}
      ]
    }
  }

  loginHandler() {
    // TODO: update this call by managing State
    this.setState({isLoggedIn: true});
  }

  logoutHandler() {
    // TODO: replace this call by managing State
    this.setState({isLoggedIn: false})

  }

  

  render() {
    return (
      <div className="weblog">
        <TitleBar />
        <Login
          isLoggedIn={this.state.isLoggedIn}
          loginHandler={()=>this.loginHandler()}
          logoutHandler={()=>this.logoutHandler()}
        />
        {this.state.isLoggedIn && <Compose />}
        {this.state.isLoggedIn && <Posts posts={this.state.posts}/>}
      </div>
    );
  }
}

function TitleBar() {
  return (
    <div className="title_bar">
      <h1>Sample Single-Page Journal</h1>
    </div>
  );
}

// ========================================


ReactDOM.render(
  React.createElement(Journal),
  document.getElementById('root')
);
