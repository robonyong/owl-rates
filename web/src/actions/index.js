/*
 * action types
 */
export const ADD_RATING = 'ADD_RATING';
export const ASSIGN_OWL = 'ASSIGN_OWL';
export const SET_VISIBILITY_FILTER = 'SET_VISIBILITY_FILTER';

/*
 * other constants
 */

export const VisibilityFilters = {
  SHOW_ALL: 'SHOW_ALL',
  SHOW_RATED: 'SHOW_RATED',
  SHOW_UNRATED: 'SHOW_UNRATED',
};

/*
 * action creators
 */

export const assignOwl = ({ owlId, reviewerId }) => ({
  type: ASSIGN_OWL, owlId, reviewerId,
});

export const setVisibilityFilter = filter => ({
  type: SET_VISIBILITY_FILTER, filter,
});

// export const addRating = (rating) => {
//  return dispatch => {
//     dispatch(requestPosts(subreddit))
//     return fetch(`/ratings`)
//       .then(response => response.json())
//       .then(json => dispatch(receivePosts(subreddit, json)))
//   }
//   return { type: 'ADD_RATING', rating };
// };
