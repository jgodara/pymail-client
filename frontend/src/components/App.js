import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";
import Sidebar from "./layout/Sidebar";
import Inbox from "./layout/Inbox";

export class App extends Component {
  render() {
    return (
      <div className="mail-box">
        <Sidebar/>
        <Inbox/>
      </div>
    );
  }
}

ReactDOM.render(<App/>, document.getElementById("root"));
