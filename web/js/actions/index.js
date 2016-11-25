import fetch from 'isomorphic-fetch';
/*
 * action types
 */
export const REQUEST_OWLS = 'REQUEST_OWLS';
export const RECEIVE_OWLS = 'RECEIVE_OWLS';
export const ADD_RATING = 'ADD_RATING';
export const ASSIGN_OWL = 'ASSIGN_OWL';
export const SET_VISIBILITY_FILTER = 'SET_VISIBILITY_FILTER';

/*
 * other constants
 */

export const VisibilityFilters = {
  SHOW_ALL: 'SHOW_ALL',
  SHOW_RATED: 'SHOW_RATED',
  SHOW_UNRATED: 'SHOW_UNRATED'
};

/*
 * action creators
 */

export const assignOwl = ({owlId, reviewerId}) => {
  return { type: ASSIGN_OWL, owlId, reviewerId };
};

export const setVisibilityFilter = (filter) => {
  return { type: SET_VISIBILITY_FILTER, filter };
};

export const requestOwls = () => {
  return {
    type: REQUEST_OWLS,
    isFetching: true
  };
};

export const receiveOwls = ({json, status='success'}) => {
	return {
    type: RECEIVE_OWLS,
    owls: json,
    status: status,
    isFetching: false
	};
};

export const fetchOwls = () => {
	return dispatch => {
    dispatch(requestOwls())
    return fetch(`/api/owls.json`)
      .then(response => response.json())
      .then(json => dispatch(receiveOwls({json})))
      .catch(err => dispatch(receiveOwls({json: err, status: 'error'})))
  }
}

export const authenticate = () => {
  
}

// export const addRating = (rating) => {
// 	return dispatch => {
//     dispatch(requestPosts(subreddit))
//     return fetch(`/ratings`)
//       .then(response => response.json())
//       .then(json => dispatch(receivePosts(subreddit, json)))
//   }
//   return { type: 'ADD_RATING', rating };
// };