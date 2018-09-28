/**
 * Created by admin on 2017/4/14.
 */

const initState = {isFetching: true, fetched: false, orders: [],};

export default function homeOrder(state = initState, action) {
	switch (action.type) {
		case 'fetchHomeOrder' :
			return Object.assign({}, state, {isFetching: true, fetched: false});
		case 'reciveHomeOrder':
			return Object.assign({}, state, {isFetching: false, fetched: true, orders: action.orders});
		case 'fetchHomehomeOrderErr':
			return Object.assign({}, state, {isFetching: false, fetched: true, err: action.err});
		default :
			return state;
	}
}