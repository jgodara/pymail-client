import React, { Component } from 'react';
import MailOptions from "./inbox/MailOptions";
import EmailsBay from "./inbox/EmailsBay";

class Inbox extends Component {
  render() {
    return (
      <aside className="lg-side">
        <div className="inbox-head">
          <h3>Inbox</h3>
          <form action="#" className="pull-right position">
            <div className="input-append">
              <input type="text" className="sr-input" placeholder="Search Mail"/>
              <button className="btn sr-btn" type="button"><i className="fa fa-search"></i></button>
            </div>
          </form>
        </div>
        <div className="inbox-body">
          <MailOptions/>
          <EmailsBay/>
        </div>
      </aside>
    );
  }
}

export default Inbox;