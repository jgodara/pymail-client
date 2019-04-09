import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";
import Sidebar from "./layout/Sidebar";
import Inbox from "./layout/Inbox";

import store from "../store"
import { Provider } from "react-redux";

export class App extends Component {

  render() {
    return (
      <Provider store={store}>
        <div className="mail-box">
          <Sidebar/>
          <Inbox/>
        </div>
      </Provider>
    );
  }
}

ReactDOM.render(<App/>, document.getElementById("root"));
