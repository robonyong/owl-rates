import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';

import { fetchOwls } from './actions';
import reducers from './reducers';
import Routes from './routes';
import configureStore from './configureStore';

const store = configureStore()

store.dispatch(fetchOwls()).then(() =>
  console.log(store.getState())
);

const root = document.getElementById('root')
if (root) {
  ReactDOM.render(
    <Provider store={store}>
      <Routes />
    </Provider>,
    root
  )
}
