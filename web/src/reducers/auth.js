import { LOGIN, LOGOUT } from '../actions/auth';

export default function auth(state = {}, action) {
  switch (action.type) {
    case LOGIN:
      return Object.assign({}, state, {
        user: action.user,
        status: action.status,
        error: action.error,
        token: action.token
      });
      break;
    case LOGOUT:
      return Object.assign({}, state, {
        user: null,
        status: null,
        error: null,
        token: null,
      });
      break;
    default:
      return state;
  }
}
