/**
 * Created by admin on 2017/4/14.
 */

const initState = {isFetching: true, fetched: false, list: [],};

export default function priceTrend(state = initState, action) {
	switch (action.type) {
		case 'fetchPriceTrend' :
			return Object.assign({}, state, {isFetching: true, fetched: false});
		case 'recivePriceTrend':
			return Object.assign({}, state, {isFetching: false, fetched: true, list: action.list});
		case 'fetchPriceTrendErr':
			return Object.assign({}, state, {isFetching: false, fetched: true, err: action.err});
		default :
			return state;
	}
}