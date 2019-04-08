import React, { Component } from 'react';

class EmailsBay extends Component {
  state = {
    emails: [
      {
        id: 1,
        from: "Test From",
        subject: "Test Email 1",
        time: "9:27 AM",
        hasAttachment: true,
        read: true,
        starred: false
      },
      {
        id: 2,
        from: "Test From",
        subject: "Test Email 1",
        time: "9:27 AM",
        hasAttachment: false,
        read: false,
        starred: true
      },
      {
        id: 3,
        from: "Test From",
        subject: "Test Email 1",
        time: "9:27 AM",
        hasAttachment: false,
        read: false,
        starred: false
      },
      {
        id: 4,
        from: "Test From",
        subject: "Test Email 1",
        time: "9:27 AM",
        hasAttachment: true,
        read: true,
        starred: false
      },
      {
        id: 5,
        from: "Test From",
        subject: "Test Email 1",
        time: "9:27 AM",
        hasAttachment: false,
        read: true,
        starred: false
      },
    ]
  };

  render() {
    let emails = this.state.emails.map((email) => (
      <tr key={email.id} className={!email.read ? "unread" : ""}>
        <td className="inbox-small-cells">
          <input type="checkbox" className="mail-checkbox"/>
        </td>
        <td className="inbox-small-cells"><i className="fa fa-star"/></td>
        <td className="view-message  dont-show">{email.from}</td>
        <td className="view-message ">{email.subject}</td>
        {email.hasAttachment ?
          <td className="view-message  inbox-small-cells"><i className="fa fa-paperclip"/></td>
          : <td />
        }
        <td className="view-message  text-right">{email.time}</td>
      </tr>
    ));
    return (
      <table className="table table-inbox table-hover">
        <tbody>
        {emails}
        </tbody>
      </table>
    );
  }
}

export default EmailsBay;