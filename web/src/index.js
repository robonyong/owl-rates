import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';

import Routes from './routes';
import configureStore from './configureStore';

import '../scss/main.scss';

/* global document */

const store = configureStore();

const root = document.getElementById('root');
if (root) {
  ReactDOM.render(
    <Provider store={store}>
      <Routes />
    </Provider>,
    root,
  );
}
