import fetch from 'isomorphic-fetch';

export const REQUEST_OWLS = 'REQUEST_OWLS';
export const RECEIVE_OWLS = 'RECEIVE_OWLS';
export const SELECT_OWL = 'SELECT_OWL';

const requestOwls = () => ({
  type: REQUEST_OWLS,
  isFetching: true,
});

const receiveOwls = ({ json, status = 'success' }) => ({
  type: RECEIVE_OWLS,
  owlList: json,
  fetchStatus: status,
  isFetching: false,
});

export const fetchOwls = () =>
  (dispatch) => {
    dispatch(requestOwls());
    return fetch('/api/owls.json')
      .then(response => response.json())
      .then(json => dispatch(receiveOwls({ json })))
      .catch(err => dispatch(receiveOwls({ json: err, status: 'error' })));
  };

export const selectOwl = (id) => ({
  type: SELECT_OWL,
  selectedOwlId: id < 15 ? id : null,
});
