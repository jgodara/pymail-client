import React, { Component, Fragment } from 'react';
import { SidebarControls } from "./sidebar/SidebarControls";
import Labels from "./sidebar/Labels";

class Sidebar extends Component {
  render() {
    return (
      <aside className="sm-side">
        <div className="user-head">
          <div className="user-name">
            <h5><a href="#">bucksavage100x</a></h5>
            <span><a href="#">realbuck@savage.com</a></span>
          </div>
          <a className="mail-dropdown pull-right" href="javascript:;">
            <i className="fa fa-chevron-down"></i>
          </a>
        </div>
        <div className="inbox-body">
          <a href="#myModal" data-toggle="modal" title="Compose" className="btn btn-compose">
            Compose
          </a>
        </div>

        <SidebarControls />
        <Labels />
      </aside>
    );
  }
}

export default Sidebar;
