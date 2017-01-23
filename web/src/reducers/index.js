import { combineReducers } from 'redux';

import owls from './owls';
import auth from './auth';
import visibilityFilter from './visibilityFilter';

const reducers = combineReducers({
  visibilityFilter,
  owls,
  auth,
});

export default reducers;
