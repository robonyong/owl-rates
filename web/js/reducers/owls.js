import { REQUEST_OWLS, RECEIVE_OWLS, SELECT_OWL, } from '../actions/owls';

export default function owls(state = { owlList: [], isFetching: false }, action) {
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
    case SELECT_OWL:
      return Object.assign({}, state, {
        selectedOwl: state.owlList.find(owl => owl.id === action.selectedOwlId),
      });
    default:
      return state;
  }
}
