

import { combineReducers } from 'redux';

import homeOrder from './homeOrder';
import addressList from './addressReducer';
import priceTrend from './priceTrendReducer';
import transListReducer from './transReducer'


export default combineReducers({
	homeOrder,
	addressList,
	priceTrend,
	transListReducer
})