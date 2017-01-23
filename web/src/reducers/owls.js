import { REQUEST_OWLS, RECEIVE_OWLS, RECEIVE_OWL } from '../actions/owls';

const initState = {
  owlList: [],
  selectedOwl: {
    avgRating: 0.0,
    descriptions: [],
    ratings: [],
  },
  isFetching: false
}
export default function owls(state = initState, action) {
  switch (action.type) {
    case REQUEST_OWLS:
      return Object.assign({}, state, {
        isFetching: true,
      });
      break;
    case RECEIVE_OWLS:
      return Object.assign({}, state, {
        isFetching: false,
        fetchStatus: action.fetchStatus,
        owlList: action.owlList,
      });
      break;
    case RECEIVE_OWL:
      return Object.assign({}, state, {
        isFetching: false,
        fetchStatus: action.fetchStatus,
        selectedOwl: action.selectedOwl,
      });
    default:
      return state;
  }
}
