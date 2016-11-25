import React, { PropTypes } from 'react';
import { Provider } from 'react-redux';
import { Router, Route, browserHistory } from 'react-router';
import App from './containers/app';

const Routes = () => (
  <Router history={browserHistory}>
    <Route path="/" component={App} />
  </Router>
);

export default Routes;
