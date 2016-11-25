import { combineReducers } from 'redux';

import { VisibilityFilters } from '../actions';
import owls from './owls';
import visibilityFilter from './visibilityFilter';

const reducers = combineReducers({
  visibilityFilter,
  owls
});

export default reducers;