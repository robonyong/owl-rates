import { REQUEST_OWLS, RECEIVE_OWLS } from '../actions';

export default function owls(state = {owls: [], isFetching: false}, action) {
	switch (action.type) {
		case REQUEST_OWLS:
      return Object.assign({}, state, {
        isFetching: true
      });
      break;
    case RECEIVE_OWLS:
      return Object.assign({}, state, {
        isFetching: false,
        owls: action.owls
      });
    default:
      return state
	}
}