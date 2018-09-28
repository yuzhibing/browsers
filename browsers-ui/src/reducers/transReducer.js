
const initState = {isFetching: true, fetched: false, transList: [],};

export default function transListReducer(state = initState, action) {
	switch (action.type) {
		case 'fetchTransList' :
			return Object.assign({}, state, {isFetching: true, fetched: false});
		case 'reciveTransList':
			return Object.assign({}, state, {isFetching: false, fetched: true, transList: action.transList});
		case 'fetchTransListrErr':
			return Object.assign({}, state, {isFetching: false, fetched: true, err: action.err});
		default :
			return state;
	}
}