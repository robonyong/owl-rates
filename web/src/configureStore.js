import { createStore, applyMiddleware } from 'redux';
import thunkMiddleware from 'redux-thunk';
import createLogger from 'redux-logger';
import persistState from 'redux-localstorage';
import reducers from './reducers';

const loggerMiddleware = createLogger();

export default function configureStore(preloadedState) {
  const persistedState = persistState(['auth'], {
    merge: (initialState, persistedState) => {
      const finalInitialState = {...initialState};
      Object.keys(persistedState).forEach(key => {
        let persistedStateValue;
        switch (key) {
          case 'auth':
            persistedStateValue = {
              'token': persistedState['auth']['token']
            };
            break;
          default:
            persistedStateValue = persistedState[key]
        }
        finalInitialState[key] = {
          ...finalInitialState[key],
          ...persistedStateValue,
        };
      });
      return finalInitialState;
    }
  });

  return createStore(
    reducers,
    persistedState,
    applyMiddleware(
      thunkMiddleware,
      loggerMiddleware,
    ),
  );
}
