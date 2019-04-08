import React, { Component } from 'react';

class Labels extends Component {
  state = {
    labels: ["JIRA Stuff", "GitLab Notifications", "AWS Notifications", "Alerts"]
  };

  render() {
    let labels = this.state.labels.map((label, key) => (
      <li key={label}>
        <a href="#">
          <i className="fa fa-sign-blank" />{label}
        </a>
      </li>
    ));
    return (
      <ul className="nav nav-pills nav-stacked labels-info inbox-divider">
        <li><h4>Labels</h4></li>
        {labels}
      </ul>
    );
  }
}

export default Labels;