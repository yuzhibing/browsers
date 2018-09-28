/**
 * Created by admin on 2017/4/14.
 */

const initState = {isFetching: true, fetched: false, addressList: [],};

export default function addressList(state = initState, action) {
	switch (action.type) {
		case 'fetchAddressList' :
			return Object.assign({}, state, {isFetching: true, fetched: false});
		case 'reciveAddressList':
			return Object.assign({}, state, {isFetching: false, fetched: true, addressList: action.addressList});
		case 'fetchAddressListrErr':
			return Object.assign({}, state, {isFetching: false, fetched: true, err: action.err});
		default :
			return state;
	}
}