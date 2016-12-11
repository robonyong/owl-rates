import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';

import Header from '../components/header';

export class App extends Component {
  render() {
    const { auth, children } = this.props;

    return (<div>
      <Header auth={auth} />
      {children}
    </div>);
  }
}

App.propTypes = {
  auth: PropTypes.object.isRequired,
  children: PropTypes.object,
};

function mapStateToProps(state) {
  const { auth } = state;
  return {
    auth,
  };
}

export default connect(mapStateToProps)(App);
