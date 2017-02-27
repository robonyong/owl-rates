import fetch from 'isomorphic-fetch';
import moment from 'moment';

import { camelToSnake, snakeToCamel } from '../utilities';

export const LOGIN = 'LOGIN';
export const LOGOUT = 'LOGOUT';

const receiveAuth = ({ user, token, status = 'success', error }) => ({
  type: LOGIN,
  user: user || null,
  token: token || null,
  status,
  error,
});

const parseResponseToken = async (response) => {
  const json = await response.json();
  if (!response.ok) {
    throw new Error(json.message);
  }
  const { token } = json;
  const { exp, ...user } = snakeToCamel(JSON.parse(atob(token.split('.')[1])));
  console.log(exp);
  return { user, token };
}

const postAuth = async (dispatch, endpoint, body) => {
  try {
    const response = await fetch(endpoint, { method: 'POST', body });
    const { user, token } = await parseResponseToken(response);
    dispatch(receiveAuth({ user, token }));
  } catch(err) {
    dispatch(receiveAuth({ error: err, status: 'error' }));
  }
}

const refreshToken = async (dispatch, token) => {
  try {
    const response = await fetch('/refresh-token', {
      method: 'GET',
      headers: {
        'Authorization': token
      },
    });
    const { user, token: newToken } = await parseResponseToken(response);
    dispatch(receiveAuth({ user, token: newToken }));
  } catch(err) {
    console.error(err);
    dispatch(expireToken());
  }
}

const expireToken = () => ({
  type: LOGIN,
  user: null,
  token: null,
});

const isTokenExpiringSoon = expMoment => {
  const tomorrow = moment().add(1, 'd');
  return expMoment.isBefore(tomorrow);
}

export const authenticate = formData =>
  dispatch => {
    const body = JSON.stringify(camelToSnake(formData));
    postAuth(dispatch, '/login', body);
  }

export const register = formData =>
  dispatch => {
    const body = JSON.stringify(camelToSnake(formData));
    postAuth(dispatch, '/register', body);
  }

export const authenticateToken = token =>
  dispatch => {
    const { exp, ...user } = snakeToCamel(JSON.parse(atob(token.split('.')[1])));
    const now = moment();
    const expMoment = moment.unix(exp);
    console.log(exp);
    if (now.isBefore(expMoment)) {
      if (isTokenExpiringSoon(expMoment)) {
        refreshToken(dispatch, token);
      } else {
        dispatch(receiveAuth({ user, token }));
      }
    } else {
      dispatch(expireToken());
    }
  }
