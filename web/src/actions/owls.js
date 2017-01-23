import fetch from 'isomorphic-fetch';
import { snakeToCamel } from '../utilities';

export const REQUEST_OWLS = 'REQUEST_OWLS';
export const RECEIVE_OWLS = 'RECEIVE_OWLS';
export const RECEIVE_OWL = 'RECEIVE_OWL';

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

const receiveOwl = ({ json, status = 'success' }) => ({
  type: RECEIVE_OWL,
  selectedOwl: json,
  fetchStatus: status,
  isFetching: false,
});

export const fetchOwls = () =>
  async (dispatch) => {
    dispatch(requestOwls());
    try {
      const response = await fetch('/api/owls.json');
      const json = await response.json();
      dispatch(receiveOwls({ json: snakeToCamel(json) }));
    } catch(err) {
      dispatch(receiveOwls({ json: err, status: 'error'}));
    }
  };

export const fetchOwlBySlug = owlSlug =>
  async (dispatch) => {
    dispatch(requestOwls());
    try {
      const response = await fetch(`/api/owls/${owlSlug}.json`);
      const json = await response.json();
      dispatch(receiveOwl({ json: snakeToCamel(json) }));
    } catch(err) {
      dispatch(receiveOwl({ json: err, status: 'error'}));
    }
  };
