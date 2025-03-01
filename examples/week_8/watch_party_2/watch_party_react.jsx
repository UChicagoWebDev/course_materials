// import {useState} from 'react'

function Splash() {
  return (
<div className="splash container"> {/*  TODO: Show me only on "/"  */}
  <div className="splashHeader">
    <div className="loginHeader">
      <div className="loggedOut"> {/*  TODO: Show me only to logged-out users  */}
        <a>Login</a>
      </div>
      <div className="loggedIn"> {/*  TODO: Show me only to logged-in users  */}
        <a className="welcomeBack">
          <span className="username">Welcome back,  Username !</span>
          <span className="material-symbols-outlined md-18">person</span>
        </a>
      </div>
    </div>
  </div>
  <div className="hero">
    <div className="logo">
      <img id="tv" src="tv.jpeg" />
      <img id="popcorn" src="popcorn.png" />
    </div>
    <h1>Watch Party</h1>
    <h2>2</h2>
    <button className="create">Create a Room</button> {/*  TODO: Show me only to logged-in users  */}
    <button className="signup">Signup</button> {/*  TODO: Show me only to logged-out users  */}
  </div>
  <h2>Rooms</h2>
  <div className="rooms">
    <div className="roomList">
      <a>{/*{room.id}*/}: <strong>{/*{room.name}*/}</strong></a>
    </div>
    <div className="noRooms">No rooms yet! You get to be first!</div> {/*  TODO: Show me only if roomList is empty  */}
  </div>
</div>)}

function Profile() {
  return (
<div className="profile"> {/*  TODO: Show me only on "/profile"  */}
  <div className="header">
    <h2><a>Watch Party</a></h2>
    <h4>2</h4>
    <div className="loginHeader">
      <div className="loggedIn">
        <a className="welcomeBack">
          <span className="username"> Username </span>
          <span className="material-symbols-outlined md-18">person</span>
        </a>
      </div>
    </div>
  </div>
  <div className="clip">
    <div className="auth container">
      <h2>Welcome to Watch Party!</h2>
      <div className="alignedForm">
        <label for="update_username">Username: </label>
        <input id="update_username" value=" Username " />
        <button>update</button>
        <label for="update_password">Password: </label>
        <input type="password" id="update_password" />
        <button>update</button>
        <label for="repeat_password">Repeat: </label>
        <input type="password" id="repeat_password" />
        <button className="exit goToSplash">Cool, let's go!</button>
        <button className="exit logout">Log out</button>
      </div>
    </div>
  </div> 
</div>
)}

function Login() {
  return (
<div className="login"> {/*  TODO: Show me only on "/login"  */}
  <div className="header">
    <h2><a>Watch Party</a></h2>
    <h4>2</h4>
  </div>
  <div className="clip">
    <div className="auth container">
      <h3>Enter your username and password to log in:</h3>
      <div className="alignedForm login">
        <label for="login_username">Username</label>
        <input id="login_username" />
        <button>Login</button>
        <label for="login_password">Password</label>
        <input type="password" id="login_password" />
      </div>
      <div className="failed"> {/*  TODO: Hide me by default. Show only on failed login attempts  */}
        <div className="message">
          Oops, that username and password don't match any of our users!
        </div>
        <button>Create a new Account</button>
      </div>
    </div>
  </div>
</div>
)}

function Room() {
  return (
<div className="room"> {/*  TODO: Show me only on "/room" (and its subroutes)  */}
  <div className="header">
    <h2><a>Watch Party</a></h2>
    <h4>2</h4>
    <div className="roomDetail">
      <div className="displayRoomName"> {/*  TODO: Show me by default. Hide when user clicks the edit icon below  */}
        <h3>
          Chatting in <strong> room.name </strong>
          <a><span className="material-symbols-outlined md-18">edit</span></a>
        </h3>
      </div>
      <div className="editRoomName"> {/*  TODO: Hide me by default. Show when user clicks the edit icon above  */}
        <h3>
          Chatting in <input />
          <button>Update</button>
        </h3>
      </div>
      Invite users to this chat at:
      <a>/rooms/ room_id </a>
    </div>
    <div className="loginHeader">
      <div className="loggedIn">
        <a className="welcomeBack">
          <span className="username"> Username </span>
          <span className="material-symbols-outlined md-18">person</span>
        </a>
      </div>
    </div>
  </div>
  <div className="clip">
    <div className="container">
      <div className="chat">
        <div className="comment_box">
          <label for="comment">What do you have to say?</label>
          <textarea name="comment"></textarea>
          <button type="submit" value="Post">Post</button>
        </div>
        <div className="messages"> {/*  TODO: Replace with the content returned by the API  */}
          <message>
            <author>Mr Chatterworth</author>
            <content>Good evening! And how is everyone feeling?</content>
          </message>
          <message>
            <author>big chats</author>
            <content>gr8 lol</content>
          </message>
          <message>
            <author>Mr Chatterworth</author>
            <content>Splendid!</content>
          </message>
          <message>
            <author>Chatty Cat</author>
            <content>
              Meow meow meow meow meow meow meow meow meow meow meow 
              meow meow meow meow meow meow meow meow meow meow meow 
              meow meow meow meow meow meow meow meow meow meow meow 
            </content>
          </message>
          <message>
            <author>Mr Chatterworth</author>
            <content>Indeed, M. Cat. Indeed. 🧐</content>
          </message>
        </div>
      </div>
      <div className="noMessages">
        <h2>Oops, we can't find that room!</h2>
        <p><a>Let's go home and try again.</a></p>
      </div>
    </div> {/*  end .container  */}
  </div> {/*  end .clip  */}
</div>
)}

function App() {
  return (
    <>
    <Splash />
    <Profile />
    <Login />
    <Room />
    </>
  );
}
// ========================================
const rootContainer = document.getElementById("root");
const root = ReactDOM.createRoot(rootContainer);
root.render(<App />);
