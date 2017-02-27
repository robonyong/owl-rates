import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';

import Header from '../components/header';

import { authenticateToken } from '../actions/auth';

export class App extends Component {
  componentWillMount() {
    if (this.props.auth.token) {
      const { dispatch } = this.props;
      dispatch(authenticateToken(this.props.auth.token));
    }
  }

  render() {
    const { auth, children, dispatch } = this.props;

    return (<div>
      <Header auth={auth} dispatch={dispatch} />
      <div className='container'>
        {children}
      </div>
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
