import React from 'react';
import { Router, Route, IndexRoute, browserHistory } from 'react-router';
import { UserAuthWrapper } from 'redux-auth-wrapper';

import App from './containers/app';
import OwlsList from './containers/owlsList';
import OwlView from './containers/owlView';
import Account from './containers/account';

const UserIsAuthenticated = UserAuthWrapper({
  authSelector: state => state.auth.user, // how to get the user state
  failureRedirectPath: '/', // the redux action to dispatch for redirect
  wrapperDisplayName: 'UserIsAuthenticated' // a nice name for this auth check
});

const Routes = () => (
  <Router history={browserHistory}>
    <Route path='/' component={App}>
      <IndexRoute component={OwlsList} />
      <Route path='owls'>
        <IndexRoute component={OwlsList} />
        <Route path=':slug' component={OwlView} />
      </Route>
      <Route path='/account' component={UserIsAuthenticated(Account)} />
    </Route>
  </Router>
);

export default Routes;
