/**
 * Created by admin on 2017/3/3.
 */

import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import { Provider } from'react-redux';
import { createStore, applyMiddleware} from 'redux';
import thunkMiddleware from 'redux-thunk';

import AppRoute from './routes.js';
import reducers from 'reducers/index.js';
import './assets/style.scss';

const store = createStore(reducers,applyMiddleware(thunkMiddleware));



function App() {
    return(
        <Provider store={store}>
            {AppRoute}
        </Provider>
    )
}

ReactDOM.render(<App/>,document.getElementById('app'));