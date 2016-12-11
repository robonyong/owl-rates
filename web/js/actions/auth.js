import fetch from 'isomorphic-fetch';

export const LOGIN = 'LOGIN';
export const LOGOUT = 'LOGOUT';

export const receiveAuth = ({ json, status = 'success' }) => ({
  type: LOGIN,
  user: json || null,
  status,
});

export const authenticate = formData =>
  dispatch =>
    fetch('/login', formData)
      .then(response => response.json())
      .then(json => dispatch(receiveAuth({ json })))
      .catch(err => dispatch(receiveAuth({ json: err, status: 'error' })));
