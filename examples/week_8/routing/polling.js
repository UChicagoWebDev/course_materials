class PollingExample extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      unread: {}, // channel_name => number unread messages
      path: "/"
    }
  }

  componentDidMount() { // when this component attached to the DOM - ie on page load on line 65
    this.getUnreadMessages(); // start polling for unread messages
    this.setState({path: get the path from the navigation bar}); // get the correct path on first page load
    window.addEventListener("popstate", () => {  // update the path whenever the user clicks the Back button
      this.setState({path: get the path from the navigation bar});
    })
  }

  getUnreadMessages() {
    f = fetch(to the api for new messages)
    f.then((response) => {return response.getJson()})
    .then((json)=> {
      // update this.state with the new unread messages counts
      this.setState({unread: json[unread]});

      this.getUnreadMessages();
    })
    .catch((exception) => {
      // log the Exception
      this.getUnreadMessages();
    })
  }

  render() {
    var className = "widescreen"
    if () {
      className = "narrow"
    }

    channel = null;
    replies = null;

    // "/my_awesome_channel"
    // "/my_cool_channel/386" -> Show me posts in my_cool_channel and replies to message id 386
    path = this.state.path.split("/")
    if path[2] {channel = path[1]} // "my_cool_channel"
    if path[3] {repliesTo = path[2]} // "386"

    const isLoggedIn = this.state.isLoggedIn;

    return (
      <div className={className}>
        {!isLoggedIn && <LoginComponent />}
        {isLoggedIn && <ChannelComponent unread={this.state.unread} />}
        {isLoggedIn && channel <MessagesComponent channelName={channel} />}
        {isLoggedIn && replies <RepliesComponent repliesTo={repliesTo} />}
      </div>
    );
  }
}

// ========================================

ReactDOM.render(
  React.createElement(PollingExample)),
  document.getElementById('root')
);
