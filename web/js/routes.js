import React from 'react';
import { Router, Route, IndexRoute, browserHistory } from 'react-router';

import App from './containers/app';
import OwlsList from './containers/owlsList';
import OwlView from './containers/owlView';

const Routes = () => (
  <Router history={browserHistory}>
    <Route path='/' component={App}>
      <IndexRoute component={OwlsList} />
      <Route path='owls'>
        <IndexRoute component={OwlsList} />
        <Route path=':id' component={OwlView} />
      </Route>
    </Route>
  </Router>
);

export default Routes;
