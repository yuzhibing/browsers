import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { Provider } from'react-redux';
import { createStore, applyMiddleware} from 'redux';
import thunkMiddleware from 'redux-thunk';

import AppRoute from './routes';
import reducers from 'reducers/index';

const store = createStore(reducers,applyMiddleware(thunkMiddleware));

function App() {
	return(
		<Provider store={store}>
			{<AppRoute/>}
		</Provider>
	)
}

// ReactDOM.render(<App/>, document.getElementById('app'));
try {
	ReactDOM.render( <App/>, document.getElementById('app'))
} catch (err) {
	console.log ('err:', err)
}