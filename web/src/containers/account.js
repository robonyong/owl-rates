import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';

export class Account extends Component {
  render() {
    const { user } = this.props;
    console.log(user);
    return (<div></div>);
  }
}

function mapStateToProps(state) {
  const { auth } = state;
  return {
    user: auth.user,
  };
}

export default connect(mapStateToProps)(Account);
