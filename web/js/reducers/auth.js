import { LOGIN, LOGOUT } from '../actions/auth';

export default function auth(state = { user: { name: 'Robin' } }, action) {
  switch (action.type) {
    case LOGIN:
      return Object.assign({}, state, {
        user: action.user,
      });
      break;
    case LOGOUT:
      return Object.assign({}, state, {
        user: null,
      });
      break;
    default:
      return state;
  }
}
