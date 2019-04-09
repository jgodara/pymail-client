import React, { Component } from 'react';
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getAllEmails } from "../../../actions/emails"

class EmailsBay extends Component {

  static propTypes = {
    emails: PropTypes.array.isRequired,
    getAllEmails: PropTypes.func.isRequired
  };

  componentDidMount() {
    this.props.getAllEmails()
  }

  render() {
    let emails = this.props.emails.map((email) => (
      <tr key={email.id} className={!email.read ? "unread" : ""}>
        <td className="inbox-small-cells">
          <input type="checkbox" className="mail-checkbox"/>
        </td>
        <td className="inbox-small-cells"><i className="fa fa-star"/></td>
        <td className="view-message  dont-show">{email.from}</td>
        <td className="view-message ">{email.subject}</td>
        {email.hasAttachment ?
          <td className="view-message  inbox-small-cells"><i className="fa fa-paperclip"/></td>
          : <td/>
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

const mapStateToProps = state => ({
  emails: state.emails.emails
});

export default connect(mapStateToProps, {getAllEmails})(EmailsBay);