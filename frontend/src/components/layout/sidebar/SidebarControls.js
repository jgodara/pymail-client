import React, { Component } from 'react';

class SidebarControls extends Component {
  render() {
    return (
      <ul className="inbox-nav inbox-divider">
        <li className="active">
          <a href="#"><i className="fa fa-inbox"></i> Inbox <span className="label label-danger pull-right">2</span></a>

        </li>
        <li>
          <a href="#"><i className="fa fa-envelope-o"></i> Sent Mail</a>
        </li>
        <li>
          <a href="#"><i className="fa fa-bookmark-o"></i> Important</a>
        </li>
        <li>
          <a href="#"><i className=" fa fa-external-link"></i> Drafts <span
            className="label label-info pull-right">30</span></a>
        </li>
        <li>
          <a href="#"><i className=" fa fa-trash-o"></i> Trash</a>
        </li>
      </ul>
    );
  }
}

export default SidebarControls;